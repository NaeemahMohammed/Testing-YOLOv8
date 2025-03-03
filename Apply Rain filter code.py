import os
from PIL import Image

# Path to your test images and the folder to save the results
test_images_folder = path to test photos
save_folder = path to desired saved photos

# Path to the overlay image
overlay_image_path =  Path to the overlay image (should be a PNG with transparency)

# Get the list of all image file names in the test folder
image_files = os.listdir(test_images_folder)

# Loop through each image in the folder
for image_file in image_files:
    # Only process JPG or PNG files (adjust if needed)
    if image_file.endswith(('.jpg', '.jpeg', '.png')):
        # Construct the full file path
        base_image_path = os.path.join(test_images_folder, image_file)
        
        # Open the base image and the overlay image
        base_img = Image.open(base_image_path)
        overlay_img = Image.open(overlay_image_path)

        # Resize overlay to match base image dimensions (if needed)
        overlay_img = overlay_img.resize(base_img.size, Image.Resampling.LANCZOS)

        # Ensure the overlay image has an alpha channel (transparency)
        overlay_img = overlay_img.convert("RGBA")

        # Adjust the opacity of the overlay (e.g., reduce opacity by 50%)
        overlay_data = overlay_img.getdata()
        new_overlay_data = []
        for item in overlay_data:
            r, g, b, a = item
            new_a = int(a * 0.5)  # Adjust this value for more/less transparency
            new_overlay_data.append((r, g, b, new_a))

        # Put the new data back into the overlay image
        overlay_img.putdata(new_overlay_data)

        # Combine the images
        combined_img = Image.alpha_composite(base_img.convert("RGBA"), overlay_img)

        # Convert back to RGB if you don't need alpha transparency in the final image
        combined_img = combined_img.convert("RGB")

        # Save the result with the same name in the save folder
        save_path = os.path.join(save_folder, image_file)
        combined_img.save(save_path)

        print(f"Processed {image_file}, saved to {save_path}")

print("All images processed and saved successfully!")
