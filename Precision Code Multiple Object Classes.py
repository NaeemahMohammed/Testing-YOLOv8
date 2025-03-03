from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO(path to yollo model)

# Define the test dataset
test_data_path = path to test dataset
# Run validation on the test dataset
results = model.val(data=test_data_path)

# Access confusion matrix (this will be a multi-class confusion matrix)
confusion_matrix = results.confusion_matrix

# Display the confusion matrix
print("Confusion Matrix (18 Classes):\n", confusion_matrix.matrix)

# Calculate metrics for each class (0 to 17 for 18 classes)
num_classes = 18

for class_id in range(num_classes):
    tp = confusion_matrix.matrix[class_id, class_id]  # True Positives for class_id
    fp = confusion_matrix.matrix[:, class_id].sum() - tp  # False Positives for class_id
    fn = confusion_matrix.matrix[class_id, :].sum() - tp  # False Negatives for class_id
    tn = confusion_matrix.matrix.sum() - (tp + fp + fn)  # True Negatives for class_id

    # Print the results for each class
    print(f"\nClass {class_id}:")
    print(f"True Positives (TP): {tp}")
    print(f"False Positives (FP): {fp}")
    print(f"False Negatives (FN): {fn}")
    print(f"True Negatives (TN): {tn}")

# Optionally: Compute Precision, Recall, F1 for each class
for class_id in range(num_classes):
    tp = confusion_matrix.matrix[class_id, class_id]
    fp = confusion_matrix.matrix[:, class_id].sum() - tp
    fn = confusion_matrix.matrix[class_id, :].sum() - tp
    
    # Precision and Recall (avoid division by zero)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    
    # F1 Score
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"\nClass {class_id} Metrics:")
    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1_score:.4f}")
