import cv2
import numpy as np
import argparse


def draw_info(frame, recording):
    if recording:
        cv2.putText(frame, "REC", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.circle(frame, (10, 30), 5, (0, 0, 255), -1)

def apply_filter(frame):
    # Smooth and brighten the video
    # Apply GaussianBlur to smooth the image
    frame = cv2.GaussianBlur(frame, (15, 15), 0)

    # Increase brightness by adding a value to each pixel
    # Limit the maximum value to 255 to avoid over-brightening
    bright_frame = cv2.convertScaleAbs(frame, alpha=1, beta=50)
    
    return bright_frame

def record_video(camera_id=0, fps=20, apply_filter_option=True, output_filename='output.avi'):
    cap = cv2.VideoCapture(camera_id)

    # Check if the webcam opened successfully
    if not cap.isOpened():
        print(f"Error: Could not open camera with ID {camera_id}.")
        return
    
    # Thiết lập FPS
    cap.set(cv2.CAP_PROP_FPS, fps)

    # Lấy kích thước khung hình từ camera
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define codec and create VideoWriter object (MJPG codec and 20 FPS)
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter(output_filename, fourcc, fps, (width, height))

    # Mode (preview or recording)
    recording = False

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            # Apply filter or not
            if apply_filter_option:
                frame = apply_filter(frame)

            # Display red circle if recording                
            draw_info(frame, recording)

            # Show the current frame
            cv2.imshow('Video Recorder', frame)
            draw_info(frame, recording)

            # Write the frame to file if recording
            if recording:
                out.write(frame)

            # Check for key presses
            key = cv2.waitKey(1) & 0xFF

            if key == 27:  # ESC key to exit
                break
            elif key == ord(' '):  # Space key to switch modes
                recording = not recording
                if recording:
                    print("Recording started...")
                else:
                    print("Recording paused...")

        else:
            print("Error: Failed to grab frame.")
            break

    # Release the camera and close all windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
        # Create an argparse object to parse command-line arguments
    parser = argparse.ArgumentParser(description="Simple Video Recorder with OpenCV.")
    
    # Add an argument for the camera ID
    parser.add_argument('--camera_id', type=int, default=0, help="ID of the camera to use (default is 0).")
    
    # Add an argument for FPS
    parser.add_argument('--fps', type=int, default=10, help="Frames per second for recording (default is 20).")
    
    # Add an argument to enable/disable the filter
    parser.add_argument('--filter', action='store_true', help="Apply a filter to smooth and brighten the video.")

    # Add an argument for the output filename
    parser.add_argument('--output', type=str, default='output.avi', help="Name of the output video file (default is output.avi).")
    
    
    # Parse the input arguments
    args = parser.parse_args()
    
    # Call the record_video function with the parsed command-line arguments
    record_video(camera_id=args.camera_id, fps=args.fps, apply_filter_option=args.filter, output_filename=args.output)
