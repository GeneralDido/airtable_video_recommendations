import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from pyairtable.api.table import Table

load_dotenv()
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY', "")
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID', "")
YT_STATS_TABLE = os.getenv('YT_STATS_TABLE', "")

class YTChannelStats:
    # getting the channel statistics
    def __get_channel_stats(self, channel_id: str) -> dict:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        channels_response = youtube.channels().list(
            id=channel_id,
            part='snippet,statistics'
        ).execute()
        channel = channels_response['items'][0]
        stats = {
            'description': channel['snippet']['description'],
            'view_count': int(channel['statistics']['viewCount']),
            'subscriber_count': int(channel['statistics']['subscriberCount']),
            'video_count': int(channel['statistics']['videoCount'])
        }
        return stats
    
    # generating the stats and updating the airtable table
    def generate(self):
        table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, YT_STATS_TABLE)
        records = table.all()
        for record in records:
            try:
                if (record['fields'].get("Description")):
                    continue
                print('Updating record: ' + record['fields']['Channel Name'] + ' and channel ID: ' + record['fields']['ChannelID'])
                channel_id = record['fields']['ChannelID']
                channel_stats = self.__get_channel_stats(channel_id)
                table.update(record['id'], {
                    'Description': channel_stats['description'],
                    'View count': channel_stats['view_count'],
                    'Subscriber count': channel_stats['subscriber_count'],
                    'Video count': channel_stats['video_count']
                })
            except Exception as e:
                print(e)
                continue