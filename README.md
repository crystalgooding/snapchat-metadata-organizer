# Snapchat Metadata Organizer

Organizes downloaded Snapchat images by correcting their metadata so they appear on the correct date in your camera roll.

## Why This Exists

Recent Snapchat updates limit Memories storage. When you mass-download your Snapchat Memories, all images and videos are saved with the **download date**, causing them to appear at the end of your camera roll.

This tool fixes that by updating each file’s metadata to match the **original date the photo or video was taken**, keeping your camera roll properly organized.

## What It Does

- Reads Snapchat Memories export data  
- Extracts the original capture date from Snapchat JSON files  
- Updates image metadata accordingly  
- Ensures photos appear in the correct chronological order

## How to Use

1. **Download your Snapchat Memories**
   - Follow Snapchat’s official guide:  
     https://help.snapchat.com/hc/en-us/articles/7012305371156-How-do-I-download-my-data-from-Snapchat
   - Select:
     - **Export your Memories**
     - **Export JSON Files**

2. **Set up the project**
   - Download this repository
   - Extract the Snapchat ZIP file into the same folder as the project

3. **Run the script**
   ```bash
   python main.py
