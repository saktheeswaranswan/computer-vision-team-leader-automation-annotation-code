import os
import shutil
import time
import keyboard
from PIL import Image

# Folder paths (adjust to your actual locations)
common_folder = r'C:\Users\RITS\Music\common_folder'
folder_a = r'C:\Users\RITS\Music\folder_a'
folder_b = r'C:\Users\RITS\Music\folder_b'

# Create folders if not exist
os.makedirs(common_folder, exist_ok=True)
os.makedirs(folder_a, exist_ok=True)
os.makedirs(folder_b, exist_ok=True)

# Get all images in the common folder
image_files = [f for f in os.listdir(common_folder)
               if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]

print("Starting image sorter. Press 'a' to move to Folder A, 'b' to Folder B.")

for image_file in image_files:
    image_path = os.path.join(common_folder, image_file)

    # Open image using PIL (shows in default viewer)
    img = Image.open(image_path)
    img.show()

    print(f"Sorting: {image_file}")
    while True:
        if keyboard.is_pressed('a'):
            shutil.move(image_path, os.path.join(folder_a, image_file))
            print(f"Moved to folder A")
            break
        elif keyboard.is_pressed('b'):
            shutil.move(image_path, os.path.join(folder_b, image_file))
            print(f"Moved to folder B")
            break
        time.sleep(0.1)

    img.close()
    time.sleep(1)  # Give time to close preview window
