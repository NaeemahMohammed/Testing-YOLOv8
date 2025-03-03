from ultralytics import YOLO

# Load the trained YOLOv8 model
model = YOLO(path to YOLO model)

# Define the test dataset
test_data_path = path to test dataset

# Run validation on the test dataset
results = model.val(data=test_data_path)

# Access confusion matrix
confusion_matrix = results.confusion_matrix

# Display the confusion matrix
print("Confusion Matrix:\n", confusion_matrix.matrix)

# Parse the confusion matrix
# confusion_matrix.matrix is a NumPy array where:
# Row 0: TP, FN (ground truth)
# Row 1: FP, TN (predictions)
matrix = confusion_matrix.matrix

# True Positives, False Positives, False Negatives
tp = matrix[0, 0]
fn = matrix[0, 1]
fp = matrix[1, 0]
tn = matrix[1, 1]

print(f"True Positives (TP): {tp}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"True Negatives (TN): {tn}")
# Access confusion matrix
confusion_matrix = results.confusion_matrix

# Display the confusion matrix
print("Confusion Matrix:\n", confusion_matrix.matrix)

# Parse the confusion matrix
# confusion_matrix.matrix is a NumPy array where:
# Row 0: TP, FN (ground truth)
# Row 1: FP, TN (predictions)
matrix = confusion_matrix.matrix

# True Positives, False Positives, False Negatives
tp = matrix[0, 0]
fn = matrix[0, 1]
fp = matrix[1, 0]
tn = matrix[1, 1]

print(f"True Positives (TP): {tp}")
print(f"False Positives (FP): {fp}")
print(f"False Negatives (FN): {fn}")
print(f"True Negatives (FN): {tn}")
# Metrics calculations
precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

# Print results
print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 Score: {f1_score:.4f}")
