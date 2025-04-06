# 🌀 Real-Time Image Animation using Deep Learning

This project brings static images to life by animating them using motion patterns from a driving video, powered by deepfake generation techniques. Based on the **First Order Motion Model for Image Animation**, it uses advanced deep learning architectures like **ResNext CNN** and **LSTM** to create realistic facial animations.

## 📌 Features
- Real-time animation of any portrait image using a video of a real person's facial expressions.
- No 3D modeling or manual rigging required.
- Works with any input image and driving video.
- Extensible for applications in entertainment, virtual avatars, and deepfake detection.

## 🧠 Tech Stack
- **Python**
- **PyTorch**
- **OpenCV**, **FFmpeg**
- **ResNext CNN** for feature extraction
- **LSTM** for temporal consistency
- **VS Code**, Google Colab / Local Runtime

## 📂 Project Structure
Real_Time_Image_Animation/
├── checkpoints/                 # Pre-trained model weights (.pth files)
│   └── <model_name>.pth
│
├── config/                      # Configuration files (YAML)
│   └── <model_config>.yaml
│
├── demo.py                      # Main script to run the animation
├── animate.py                   # Animation logic (may be called by demo.py)
├── reconstruction.py            # For reconstructing videos (optional)
├── requirements.txt             # Python dependencies
│
├── inputs/                      # Input assets
│   ├── source.png               # Static image (e.g., Mona Lisa)
│   └── driving.mp4              # Driving video with facial motion
│
├── outputs/                     # Output folder for generated videos
│   └── result.mp4
│
├── modules/                     # Core model modules
│   ├── generator.py             # Generator network
│   ├── keypoint_detector.py     # Keypoint detection logic
│   └── ...                      # Other model components
│
├── README.md                    # Project documentation
└── LICENSE                      # License file (MIT recommended)

## 🚀 How It Works
1. **Input** a static source image and a driving video.
2. The model extracts **key facial landmarks** and motion vectors from the driving video.
3. Motion is **transferred to the static image**, animating it with realistic expressions and movements.
4. The **Generator Network** synthesizes a video where the image mimics the motion in the driving video.
