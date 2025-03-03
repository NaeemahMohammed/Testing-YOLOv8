from ultralytics import YOLO

# Path to the dataset configuration YAML file
dataset_yaml = 'C:/Users/naeem/yolomodel/data.yaml'  # Replace with your actual path

# Initialize the YOLO model
model = YOLO("yolov8n.yaml")  # Use YOLOv8 model (e.g., yolov8n.yaml for small model)

# Train the model
model.train(
    data=dataset_yaml,  # Path to the dataset YAML file
    epochs=50,           # Number of epochs (you can adjust this)
    batch=16,            # Batch size (adjust based on your hardware)
    imgsz=640,        # Image size
    project='runs/train',  # Directory to save the results
    name='yolov8_model',   # Name for the experiment
    exist_ok=True,         # Overwrite the experiment if it exists
)

# You can also specify other hyperparameters (lr, optimizer, etc.)
model.save(r"C:\Users\naeem\OneDrive - Liverpool John Moores University\Third year\Final year Project\YOLO trained model 70\trained70.pt")  # Specify your custom path here
print("Model saved as 'trained70.pt' in the specified directory")