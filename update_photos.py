import os
import re
import json

def update_photos():
    photos_dir = 'arraia_fotos'
    html_file = 'cronograma_app.html'

    # Get list of valid images and videos
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.mp4', '.webm', '.ogg', '.mov', '.avi')
    try:
        files = os.listdir(photos_dir)
        photos = [f"{photos_dir}/{f}" for f in files if f.lower().endswith(valid_extensions)]
    except FileNotFoundError:
        photos = []

    # Sort for consistency
    photos.sort()

    # Format the array as a JavaScript array string
    photos_js_array = json.dumps(photos) if photos else "[]"

    # Read the HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find and replace the photos array
    # Looking for: const photos = [...];
    pattern = r"const\s+photos\s*=\s*\[.*?\];"
    replacement = f"const photos = {photos_js_array};"

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)

    if count > 0:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated {html_file} with {len(photos)} photos.")
    else:
        print(f"Warning: Could not find the photos array in {html_file}.")

if __name__ == '__main__':
    update_photos()
