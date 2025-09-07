#!/usr/bin/env python3
import re
import os

# List of files with triple --- pattern that need fixing
files_to_fix = [
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-106.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-105.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-99.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-98.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-97.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-59.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-58.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-57.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-56.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-55.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-54.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-36.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-32.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-31.md',
    '/Users/familyplate/my-ai-notebook/blog/_posts/post-23.md'
]

for file_path in files_to_fix:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Pattern to find YAML front matter with extra --- and content after
        # This will match: --- (yaml content) --- (some content) ---
        pattern = r'^---\n(.*?\n)---\n(.*?)\n---\n'
        match = re.match(pattern, content, re.MULTILINE | re.DOTALL)
        
        if match:
            yaml_content = match.group(1)
            extra_content = match.group(2).strip()
            remaining_content = content[match.end():]
            
            # Reconstruct with proper YAML front matter
            if extra_content:
                # Add the extra content to the yaml if it looks like a yaml field
                if ':' in extra_content and '\n' not in extra_content:
                    new_content = f"---\n{yaml_content}{extra_content}\n---\n{remaining_content}"
                else:
                    # Put extra content after the yaml block
                    new_content = f"---\n{yaml_content}---\n\n{extra_content}\n{remaining_content}"
            else:
                new_content = f"---\n{yaml_content}---\n{remaining_content}"
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"Fixed: {os.path.basename(file_path)}")
        else:
            print(f"No match found in: {os.path.basename(file_path)}")

print("Done fixing triple YAML front matter issues!")