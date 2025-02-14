# Aiplane Tracking with YOLO
## Demo Video
Check out the demo video of the project:

![Aircraft Tracking Demo](demo_video.mp4)
## Installation Guide

### Step 1: Download and Install Miniconda
Download Miniconda from the official website and install it on your system.

### Step 2: Create a Conda Environment
Open Anaconda Command Prompt and run the following command:
```sh
conda create -n myenv python=3.9 --yes
```

### Step 3: Activate the Environment
```sh
conda activate myenv
```

### Step 4: Install YOLO (Ultralytics)
```sh
pip install ultralytics
```

## Running the Tracker

### Run on Camera
Make sure to specify the correct camera address in the `track_aircraft_cam.py` file before running:
```sh
python detect_and_track_on_camera.py
```

### Run on Video
Modify the `detect_and_track_on_video.py` file to specify the correct video file name and then run:
```sh
python detect_and_track_on_video.py
