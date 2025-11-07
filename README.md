# Semi-Auto Labeling Pipeline with CVAT + YOLO

## 📌 Overview

Manual labeling is one of the slowest and most expensive steps in building AI datasets.
This project shows how I used a **YOLO-based model + CVAT** to cut labeling time by **5–6x** using **AI-assisted annotations**.

Instead of drawing boxes from scratch, my pipeline:

1. Runs a trained detection model on raw images.
2. Exports predictions into a CVAT-supported format.
3. Uploads them into CVAT for **human correction**.

---

## 🎯 Problem

* Labeling 1 image manually: \~3 mins.
* 1000 images = \~50 hours of boring work.
* Teams waste **time + money** doing repetitive labeling.

---

## ✅ Solution

* Use a **trained YOLO model** to generate bounding boxes automatically.
* Convert results into **COCO/YOLO JSON/XML format** (CVAT-supported).
* Import pre-labeled images into **CVAT**.
* Humans only **fix AI mistakes**, instead of labeling from scratch.

---

## 🔧 Tools Used

* **YOLOv8** (Ultralytics) – detection model
* **Python** – scripts for format conversion
* **CVAT** – annotation & correction
* **CUDA / PyTorch** – for inference

---

## ⚡ Pipeline

1. **Train model**

   ```bash
   yolo detect train data=dataset.yaml model=yolov8s.pt epochs=50
   ```

2. **Run inference on raw images**

   ```bash
   yolo detect predict model=best.pt source=raw_images/ save_txt=True
   ```

3. **Convert predictions → CVAT import format**

   * Example: YOLO TXT → CVAT support YOLO format
   * Python script included in `ModelTo_YOLO.py`

4. **Upload into CVAT**

   * Import annotations in **YOLO format**.
   * See pre-labeled bounding boxes in the interface.

5. **Correct mistakes**

   * Faster than labeling everything manually.

---

## 📊 Results

| Method           | Time per image | Notes                |
| ---------------- | -------------- | -------------------- |
| Manual labeling  | \~1.30 mins       | Draw every box       |
| Semi-auto (this) | \~10 secs      | Just tweak + relabel |

➡️ **10–20x faster** dataset creation 🚀

---

## 📸 Demo Screenshots


1. **Raw image (unlabeled)**
2. **After importing auto-labels into CVAT**
3. **Corrected final labels**

---

## 💡 Portfolio Impact

* Shows ability to **integrate AI + annotation tools**.
* Demonstrates **real-world data engineering skills**.
* Cuts costs for any team working on computer vision datasets.

---

## 📂 Repository Structure

```
├── raw_images/          # Sample unlabeled images  
├── predictions/         # Model predictions (YOLO)  
├── annotations/         # Converted annotations (YOLO)  
├── ModelTo_YOLO.py      # Script to convert YOLO → CVAT format  
└── README.md            # This file  
```

---

## 🚀 How to Run

1. Clone repo

   ```bash
   git clone https://github.com/Kalana-Gayan/semi-auto-labeling-pipeline.git
   cd semi-auto-labeling-pipeline
   ```
2. Install dependencies

   ```bash
   pip install ultralytics opencv-python
   ```
3. ```bash
   yolo detect predict model=best.pt source=raw_images/ save_txt=True
   ```
4. Run conversion script
   ```bash
   python ModelTo_YOLO.py
   ```
   Edit OUTPUT_LABELS_FOLDER,MODEL_PATH,IMAGES_BASE_FOLDER in the script.
   This will save train.txt files that need to make the zip file 
   
5. Make the zip file that containes data.yaml,labels,train.txt
<img width="964" height="528" alt="image" src="https://github.com/user-attachments/assets/25ea2472-0879-40fa-898f-7f3c894ce89b" />

6. Import into CVAT → Correct → Export final dataset 🎉



🔥 That’s it.


