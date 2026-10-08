
import cv2

# Step 1: Open the video file
cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    raise RuntimeError("Cannot open input.mp4")

# Step 2: Read video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)#Retrieves width, height and FPS

if fps <= 0:
    fps = 30

# Step 3: Create the output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    fps,
    (width, height)
)

if not out.isOpened():
    cap.release()
    raise RuntimeError("Cannot create output.mp4")

# Step 4: Process every frame
frame_number = 0

while True:
    success, frame = cap.read()

    if not success:
        break

    frame_number += 1

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
        "Assignment 1",
        (30, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    # Display frame number
    cv2.putText(
        frame,
        f"Frame: {frame_number}",
        (30, height - 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    # Save the modified frame
    out.write(frame)

# Step 5: Release resources
cap.release()
out.release()

print("Video processed successfully!")
print(f"Total frames: {frame_number}")
print("Saved as output.mp4")
