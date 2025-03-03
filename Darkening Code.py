import os
from PIL import Image, ImageEnhance

# Path to your test images and the folders to save the results
test_images_folder = path to test photos
evening_folder = path to save evening photos
night_folder = path to save night photos

# Ensure the save folders exist
os.makedirs(evening_folder, exist_ok=True)
os.makedirs(night_folder, exist_ok=True)

# Get the list of all image file names in the test folder
image_files = os.listdir(test_images_folder)

# Loop through each image in the folder
for image_file in image_files:
    # Only process JPG or PNG files (adjust if needed)
    if image_file.endswith(('.jpg', '.jpeg', '.png')):
        # Construct the full file path
        base_image_path = os.path.join(test_images_folder, image_file)

        # Open the base image
        base_img = Image.open(base_image_path)

        # Enhance the image for "evening" (slightly darker)
        enhancer = ImageEnhance.Brightness(base_img)
        evening_img = enhancer.enhance(0.7)  # Reduce brightness to 70%

        # Enhance the image for "night" (much darker)
        night_img = enhancer.enhance(0.3)  # Reduce brightness to 30%

        # Save the results with the same name in the appropriate folders
        evening_save_path = os.path.join(evening_folder, image_file)
        night_save_path = os.path.join(night_folder, image_file)

        evening_img.save(evening_save_path)
        night_img.save(night_save_path)

        print(f"Processed {image_file}, saved to {evening_save_path} and {night_save_path}")

print("All images processed and saved successfully!")
