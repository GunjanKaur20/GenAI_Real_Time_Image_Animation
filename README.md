
🌀 Real-Time Image Animation using Deep Learning

        **Bring still images to life in real-time!**  

This project brings static images to life by animating them using motion patterns from a driving video, powered by deepfake generation techniques. Based on the First Order Motion Model for Image Animation, it uses advanced deep learning architectures like ResNext CNN and LSTM to animate a source image based on a driving video, creating  realistic facial or body motions - a core concept behind deepfakes.



📌 Features

Real-time animation of any portrait image using a video of a real person's facial expressions.
Leverages **First Order Motion Model** architecture.
Pre-trained deep leaning models (ResNext + LSTM).
No 3D modeling or manual rigging required.
Works with any input image and driving video.
Easy to run locally with minimal setup.
Modular structure to experiment with custom datasets.
Extensible for applications in entertainment, virtual avatars, and deepfake detection.


🧠 Tech Stack

Python
PyTorch (Deep Learning Framework)
OpenCV, FFmpeg (Video frame processing)
NumPy and Matplotlib (Data Handling and Visualization)
ResNext CNN for feature extraction
LSTM for temporal consistency
VS Code, Google Colab / Local Runtime


📂 Project Structure

Real_Time_Image_Animation/ ├── checkpoints/ # Pre-trained model weights (.pth files) │ └── <model_name>.pth │ ├── config/ # Configuration files (YAML) │ └── <model_config>.yaml │ ├── demo.py # Main script to run the animation ├── animate.py # Animation logic (may be called by demo.py) ├── reconstruction.py # For reconstructing videos (optional) ├── requirements.txt # Python dependencies │ ├── inputs/ # Input assets │ ├── source.png # Static image (e.g., Mona Lisa) │ └── driving.mp4 # Driving video with facial motion │ ├── outputs/ # Output folder for generated videos │ └── result.mp4 │ ├── modules/ # Core model modules │ ├── generator.py # Generator network │ ├── keypoint_detector.py # Keypoint detection logic │ └── ... # Other model components │ ├── README.md # Project documentation └── LICENSE # License file (MIT recommended)

🚀 How It Works

Input a static source image and a driving video.
The model extracts key facial landmarks and motion vectors from the driving video.
Motion is transferred to the static image, animating it with realistic expressions and movements.
The Generator Network synthesizes a video where the image mimics the motion in the driving video.

 (Update README with detailed information)

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

**create virtual environment** : ```pip install virtualenv```

**activate virtual environment** : ```virtualenv env```

## Step 2: Activate virtual environment

**For windows** : ```env/Script/activate```

**For Linux** : ```source env/bin/activate```

## Step 3 : Install required modules

**Install modules** : ``` pip install -r requirements.txt ```

**Install pytorch and torchvision** : ```pip install torch===1.0.0 torchvision===0.2.1 -f https://download.pytorch.org/whl/cu100/torch_stable.html ```

## Step 4 : Download cascade file ,weights and model and save in folder named extract

```gdown --id 1wCzJP1XJNB04vEORZvPjNz6drkXm5AUK```
The file is also availible via direct link on Google's Drive:
https://drive.google.com/uc?id=1wCzJP1XJNB04vEORZvPjNz6drkXm5AUK

**On Linux machine** : ```unzip checkpoints.zip```

If on windows platfrom unzip checkpoints.zip using unzipping software like 7zip.

**Delete zip file** : ```rm checkpoints.zip```

## Step 5 : Run the project

**Run application from live camera** : ```python image_animation.py -i path_to_input_file -c path_to_checkpoint```

**Example** : ```python .\image_animation.py -i .\Inputs\Monalisa.png -c .\checkpoints\vox-cpk.pth.tar```

**Run application from video file** : ```python image_animation.py -i path_to_input_file -c path_to_checkpoint -v path_to_video_file```

**Example** : ```python .\image_animation.py -i .\Inputs\Monalisa.png -c .\checkpoints\vox-cpk.pth.tar -v .\video_input\test1.mp4 ```

![test demo](animate.gif)

### TODO:
Tkinter version

Need work on face alignments

Future plans adding deepfake voice and merging with video




📜 License
This project is licensed under the MIT License.


🌟 Acknowledgements

Based on the concepts from First Order Motion Model for Image Animation

Inspired by research in deepfake and motion transfer


Credits

- video explanation to the project <br/>
    * [Video explanation by original author](https://www.youtube.com/watch?v=u-0cQ-grXBQ)
    * [Two min papers](https://www.youtube.com/watch?v=mUfJOQKdtAk)    

- try project on google colab
    * [youtube link](https://www.youtube.com/watch?v=RsOJJd1q6Bg&feature=youtu.be)
    * [link to colab version](https://colab.research.google.com/github/AliaksandrSiarohin/first-order-model/blob/master/demo.ipynb)



🤝 Contributing

Pull requests are welcome!
If you have ideas to improve the animation quality or extend features, feel free to open an issue or submit a PR.


📫 Contact

👩‍💻 Gunjan Kaur
📧 kaurgunjan16@gmail.com
🌐 GitHub Profile

⭐ If you find this project interesting, don’t forget to give it a star! ⭐

