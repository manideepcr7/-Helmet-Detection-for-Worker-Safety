# Helmet Detection for Worker Safety using YOLOv5

This project uses a pre-trained YOLOv5 model to detect safety helmets on construction workers.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

1. Place your YOLOv5 helmet detection model in the `models/` directory (e.g., `helmet_yolov5.pt`)
2. Put your test images in the `images/` directory
3. Run the detection script:

```bash
python helmet_detection.py
```

## Notes

- You must download the appropriate YOLOv5 custom-trained model for helmet detection.
- This script uses `torch.hub` to load YOLOv5.
