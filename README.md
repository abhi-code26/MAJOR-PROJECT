#  AI-Based Road Accident Detection System (YOLOv8)

This project detects road accidents in videos using YOLOv8.  
Each frame is processed, potential accident events are identified, and an annotated output video is generated.

---

##  External Resources (Model + Dataset)
Due to GitHub file-size limits, heavy files are stored externally.

**Download Resources:**  
https://drive.google.com/YOUR_LINK_HERE

This contains:
- `yolov8n.pt` (YOLOv8 model weights)
- `data/` (sample test videos)

---

## Recommended Project Layout
After extracting everything, keep files like this:

MAJOR-PROJECT/
   |-
├── main.py
├── generate_video.py
├── requirements.txt
├── resources/
│ ├── yolov8n.pt
│ └── data/
└── README.md


---

##  How to Run

1) Install dependencies:

pip install -r requirements.txt

2) Run accident detection:

python main.py

3) Optional: Run video generator

python generate_video.py

How the System Works:

 1.Load YOLOv8 model

 2.Process video frame-by-frame

3.Detect accident-related events

4.Draw bounding boxes and labels

5.Export final processed video

Future Enhancements:

1.Real-time CCTV monitoring

2.Cloud alerts (AWS/Azure)

3.SMS/Email emergency notifications

4.Training custom dataset





