from yt_channel_stats import YTChannelStats
from best_performing_videos import BestPerformingVideos
from recommendations import Recommendations

channel_stats = YTChannelStats().generate()
best_performing_videos = BestPerformingVideos(video_count=3).generate()
recommendations = Recommendations(num_titles_to_check=9, num_titles_to_recommend=9).generate()