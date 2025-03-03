import os
import shutil
import random

# Directories for current train and validation images and labels
train_img_dir = r"path\to\train\images"  # Replace with your train image directory
train_lbl_dir = r"path\to\train\labels"  # Replace with your train label directory
valid_img_dir = r"path\to\valid\images"  # Replace with your valid image directory
valid_lbl_dir = r"path\to\valid\labels"  # Replace with your valid label directory

# Combine the images and labels from both train and validation sets
train_images = [os.path.join(train_img_dir, f) for f in os.listdir(train_img_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
train_labels = [os.path.join(train_lbl_dir, f.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')) for f in os.listdir(train_img_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

valid_images = [os.path.join(valid_img_dir, f) for f in os.listdir(valid_img_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
valid_labels = [os.path.join(valid_lbl_dir, f.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')) for f in os.listdir(valid_img_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]

# Combine both datasets into one list of image and label pairs
all_images = list(zip(train_images + valid_images, train_labels + valid_labels))

# Shuffle the combined dataset
random.shuffle(all_images)

# Calculate the split index
total_images = len(all_images)
train_size = int(total_images * 0.60)  # 70% for training
valid_size = total_images - train_size  # 30% for validation

# Create new directories if they don't exist
new_train_img_dir = r"path\to\train\images"  # Replace with your new train image directory
new_train_lbl_dir = r"path\to\train\labels"  # Replace with your new train label directory
new_valid_img_dir = r"path\to\valid\images"  # Replace with your new valid image directory
new_valid_lbl_dir = r"path\to\valid\labels"  # Replace with your new valid label directory

os.makedirs(new_train_img_dir, exist_ok=True)
os.makedirs(new_train_lbl_dir, exist_ok=True)
os.makedirs(new_valid_img_dir, exist_ok=True)
os.makedirs(new_valid_lbl_dir, exist_ok=True)

# Split the images and labels into training and validation sets
train_data_split = all_images[:train_size]
valid_data_split = all_images[train_size:]

# Move the images and labels into the new directories
for img_path, lbl_path in train_data_split:
    shutil.copy(img_path, new_train_img_dir)
    shutil.copy(lbl_path, new_train_lbl_dir)

for img_path, lbl_path in valid_data_split:
    shutil.copy(img_path, new_valid_img_dir)
    shutil.copy(lbl_path, new_valid_lbl_dir)

print(f"Training set size: {len(train_data_split)}")
print(f"Validation set size: {len(valid_data_split)}")
