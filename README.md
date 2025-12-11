AI-Based Road Accident Detection System (YOLOv8)

This project detects road accidents from video streams using the YOLOv8 object detection model.  
The system processes each frame of the input video, identifies potential accident events, and generates an output video with bounding boxes and labels.


 Project Structure
 
Project/
│
├── main.py # Core accident detection logic
├── generate_video.py # Video processing pipeline
├── requirements.txt # Python dependencies
│
├── data/ # Test video samples (stored externally)
├── yolov8n.pt # YOLOv8 model weights (stored externally)
│
└── venv/ # Virtual environment (excluded from submission)

---

Resources (Model Weights + Dataset)

Due to GitHub's file size limits, heavy resources are uploaded externally.

**Download Resources:**  
https://drive.google.com/https://drive.google.com/drive/folders/1CrlK7Yzs9hG4rRpQvaL2qc0tzkWotkqq?usp=drive_link

This folder contains:
- `yolov8n.pt` — YOLOv8 pre-trained model weights  
- `data/` — sample test videos used for accident detection  



How to Run the Project

1️⃣ Install Dependencies

pip install -r requirements.txt

2️⃣ Run Accident Detection Script

python main.py

3️⃣ Run Video Generation Script (Optional)

python generate_video.py

Workflow

1.Load YOLOv8 model (yolov8n.pt)

2.Read frames from input video

3.Perform inference on each frame

4.Detect accident-triggering objects (vehicles, collisions, etc.)

5.Draw bounding boxes + labels

6.Save output processed video

Features

✔ Real-time accident detection
✔ YOLOv8 state-of-the-art model
✔ Works on video streams & CCTV footage
✔ Lightweight and easy to run
✔ Modular code structure

Future Scope

Live CCTV feed monitoring

Cloud integration (AWS / Azure)

SMS alert system for emergency services

Higher accuracy using custom-trained YOLO models

