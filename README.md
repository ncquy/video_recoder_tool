# Simple Video Recorder using OpenCV

## Overview

This project implements a simple video recorder using OpenCV, allowing you to capture and record video from your webcam or any connected camera. The recorder has two modes: `Preview` and `Record`, and it can apply filters to smooth and brighten the video in real-time.

## Features

1. **Display live camera feed**: The current camera's video is displayed in a window.
   - Uses OpenCV's `cv2.VideoCapture` to capture the camera feed (supports both webcam and IP cameras with proper URL input).
2. **Record and save video**: Save the recorded video to a file in `.avi` format.
   - OpenCV's `cv2.VideoWriter` is used to write video to file.
3. **Switch between Preview and Record mode**:
   - Space key toggles between preview and recording modes.
   - A red "REC" indicator is displayed when recording.
4. **Exit the program**:
   - Press `ESC` to stop recording and close the application.

## Additional Features 

1. **Filter Application**: Apply a smoothing and brightening filter to the video.
   - Smoothing is done with `cv2.GaussianBlur`, and brightness is increased using `cv2.convertScaleAbs`.
2. **Custom FPS**: Adjust the frames per second (FPS) of the recording via command-line arguments.
3. **Change Video Codec**: Use MJPG codec (or any custom codec) by modifying the `fourcc` argument.

## Usage

### Requirements

- Python 3.x
- OpenCV (Python version)
- NumPy

## Command-line Arguments

- `--camera_id`: Camera ID to use (default: 0 for the primary webcam).
- `--fps`: Frames per second (FPS) for recording (default: 10).
- `--filter`: Enable filter for smoothing and brightening the video.
- `--output`: Output filename for the recorded video (default: `output.avi`).

## Example Commands

1. **Preview mode**: Start the recorder in preview mode without recording.
   ```bash
   python video_recoder_tool.py --camera_id 0 --fps 20

