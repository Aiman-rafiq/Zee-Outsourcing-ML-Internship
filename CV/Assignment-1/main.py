
import cv2

# Step 1: Open the input video
cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    raise RuntimeError("Error: Cannot open input.mp4")

# Step 2: Read video properties
fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 30

# Step 3: Set output video resolution
output_width = 640
output_height = 360

# Step 4: Configure the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    fps,
    (output_width, output_height)
)

if not out.isOpened():
    cap.release()
    raise RuntimeError("Error: Cannot create output.mp4")

# Step 5: Process the video frame by frame
frame_number = 0

while True:
    success, frame = cap.read()

    if not success:
        break

    frame_number += 1

    # Resize frame to reduce output video size
    frame = cv2.resize(
        frame,
        (output_width, output_height)
    )

    # Draw a green rectangle
    cv2.rectangle(
        frame,
        (50, 70),
        (250, 250),
        (0, 255, 0),
        3
    )

    # Add project title
    cv2.putText(
        frame,
        "Computer Vision - Assignment 1",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2
    )

    # Display current frame number
    cv2.putText(
        frame,
        f"Frame: {frame_number}",
        (30, output_height - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # Save the processed frame
    out.write(frame)

# Step 6: Release resources
cap.release()
out.release()

print("Video processed successfully!")
print(f"Total frames processed: {frame_number}")
print(f"Output resolution: {output_width}x{output_height}")
print("Output saved as output.mp4")
