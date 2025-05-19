import os
import re

# Define the target replacement href
new_href = "../index.html"

# Get the list of all HTML files in the current directory
html_files = [file for file in os.listdir() if file.endswith(".html")]

for file in html_files:
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()

    # Find and replace the first href
    updated_content = re.sub(r'href="[^"]+"', f'href="{new_href}"', content, count=1)

    with open(file, "w", encoding="utf-8") as f:
        f.write(updated_content)

print("All files updated successfully!")
