#!/usr/bin/env python3
import os
import re

# Test fix: Update date format to full ISO format with time
test_files = [
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-1.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-2.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-3.md'
]

for file_path in test_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace simple date format with full datetime format
        # Change "date: 2024-01-02" to "date: 2024-01-02 10:00:00 -0500"
        updated_content = re.sub(
            r'^date: (\d{4}-\d{2}-\d{2})$',
            r'date: \1 10:00:00 -0500',
            content,
            flags=re.MULTILINE
        )
        
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            
            print(f"Updated date format in: {os.path.basename(file_path)}")
        else:
            print(f"No change needed in: {os.path.basename(file_path)}")

print("Done testing date format update!")