#!/usr/bin/env python3
"""
Quick start example for dbbasic-video

This example shows how to:
1. Download a YouTube video
2. Extract keyframes
3. Create a thumbnail grid
4. Get the transcript
5. Analyze with AI
"""

from dbbasic_video.download_video import download_video
from dbbasic_video.extract_keyframes import extract_keyframes
from dbbasic_video.make_grid import create_thumbnail_sheet
from dbbasic_video.get_transcript import download_transcript
from dbbasic_video.analyze_visuals import analyze_grid

# Configuration
YOUTUBE_URL = "https://www.youtube.com/watch?v=VIDEO_ID"
VIDEO_ID = "VIDEO_ID"

# Step 1: Download video
print("Downloading video...")
video_file = download_video(YOUTUBE_URL, "my_video.mp4")

# Step 2: Extract keyframes
print("\nExtracting keyframes...")
extract_keyframes(video_file, "keyframes/")

# Step 3: Create thumbnail grid
print("\nCreating thumbnail grid...")
create_thumbnail_sheet("keyframes/", "thumbnail_grid.jpg")

# Step 4: Download transcript
print("\nDownloading transcript...")
download_transcript(VIDEO_ID, "transcript.json")

# Step 5: Analyze visuals (requires OPENAI_API_KEY in .env)
print("\nAnalyzing visuals with AI...")
analyze_grid("thumbnail_grid.jpg", "analysis.txt")

print("\n✓ Done! Check the output files.")
