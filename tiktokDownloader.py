from TikTokApi import TikTokApi
import asyncio
import os

async def download_videos(username: str, amount: int = 50):
    async with TikTokApi() as api:
        user = await api.user(username=username)
        videos = []
        async for video in user.videos(count=amount):
            videos.append(video)

        os.makedirs(username, exist_ok=True)
        for video in videos:
            video_data = await video.bytes()
            with open(f"{username}/{video.id}.mp4", "wb") as f:
                f.write(video_data)
            print(f"✅ Heruntergeladen: {video.id}")

if __name__ == "__main__":
    username = input("🔍 TikTok-Username: @").strip().lstrip("@")
    asyncio.run(download_videos(username))
