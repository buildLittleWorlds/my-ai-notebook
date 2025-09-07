#!/usr/bin/env python3
import os
import re
import shutil
from datetime import datetime, timedelta

posts_dir = '/Users/familyplate/my-ai-notebook/blog/_posts'
start_date = datetime(2024, 1, 2)  # Starting from January 2, 2024

# Get all post files and sort them by number
post_files = []
for filename in os.listdir(posts_dir):
    if filename.startswith('post-') and filename.endswith('.md'):
        # Extract post number
        match = re.search(r'post-(\d+)\.md', filename)
        if match:
            post_num = int(match.group(1))
            post_files.append((post_num, filename))

# Sort by post number
post_files.sort()

for post_num, filename in post_files:
    file_path = os.path.join(posts_dir, filename)
    
    # Read the file to get the title
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract title from front matter
    title_match = re.search(r'^title:\s*["\']?([^"\']+)["\']?$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else f"Post {post_num}"
    
    # Create a URL-safe slug from the title
    slug = re.sub(r'[^\w\s-]', '', title.lower())  # Remove special chars
    slug = re.sub(r'[-\s]+', '-', slug)  # Replace spaces with hyphens
    slug = slug.strip('-')  # Remove leading/trailing hyphens
    if not slug:
        slug = f"post-{post_num}"
    
    # Calculate the date for this post (sequential dates)
    post_date = start_date + timedelta(days=post_num-1)
    date_str = post_date.strftime('%Y-%m-%d')
    
    # Create new filename
    new_filename = f"{date_str}-{slug}.md"
    new_file_path = os.path.join(posts_dir, new_filename)
    
    # Rename the file
    shutil.move(file_path, new_file_path)
    print(f"Renamed: {filename} -> {new_filename}")

print("Done renaming all posts to Jekyll format!")