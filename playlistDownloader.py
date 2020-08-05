import pyyoutube
import os
import envkey

# my_var = envkey.get("YOUTUBE_PLAYLIST_API_key")

print(os.environ) # need to fix envkey config

api_key = os.environ('YOUTUBE_API')

def get_videos(channel_name):
    api = pyyoutube.Api(api_key=api_key)
    channel_res = api.get_channel_info(channel_name=channel_name)
    playlist_id = channel_res.items[0].contentDetails.relatedPlaylists.uploads

    playlist_item_res = api.get_playlist_items(
        playlist_id=playlist_id, count=10, limit=6
    )
    videos = []
    for item in playlist_item_res.items:
        video_id = item.contentDetails.videoId
        video_res = api.get_video_by_id(video_id=video_id)
        videos = video_res.items
        print(videos)
    return videos


