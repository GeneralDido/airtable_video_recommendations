import os
from dotenv import load_dotenv
from typing import List
from dataclasses import dataclass
from pyairtable.api.table import Table
from googleapiclient.discovery import build


load_dotenv()
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', "")
AIRTABLE_API_KEY = os.getenv('AIRTABLE_API_KEY', "")
AIRTABLE_BASE_ID = os.getenv('AIRTABLE_BASE_ID', "")
YT_STATS_TABLE = os.getenv('YT_STATS_TABLE', "")
BEST_PERFORMING_VIDEOS_TABLE = os.getenv('BEST_PERFORMING_VIDEOS_TABLE', "")


@dataclass
class BestPerformingVideos:
    video_count: int 


    def __get_most_viewed_videos(self, channel_id: str) -> list:
        youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
        search_response = youtube.search().list(
            channelId=channel_id,
            type='video',
            part='id,snippet',
            order='viewCount',
            maxResults=self.video_count
        ).execute()
        videos = []
        for search_result in search_response.get('items', []):
            video_id = search_result['id']['videoId']
            video = {
                'title': search_result['snippet']['title'],
                'video_id': video_id
            }
            videos.append(video)
        return videos
    

    def __create_records(self, videos: List[dict], channel_name: str):
        airtable = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, BEST_PERFORMING_VIDEOS_TABLE)
        for video in videos:
            print("Inserting video: " + video['title'] + " for channel: " + channel_name)
            record = {
                'Title': video['title'],
                'Video ID': video['video_id'],
                'YT Channel': channel_name
            }
            airtable.create(record)

    
    def generate(self):
        table = Table(AIRTABLE_API_KEY, AIRTABLE_BASE_ID, YT_STATS_TABLE)
        for record in table.all():
            channel_id = record['fields']['ChannelID']
            channel_name = record['fields']['Channel Name']
            videos = self.__get_most_viewed_videos(channel_id)
            self.__create_records(videos, channel_name)