from ultralytics import YOLO
import cv2

# Load YOLOv8 model and use CPU
model = YOLO("yolov8n.pt")
model.to('cpu')

# Open video file
video_path = "cow2.mp4"
cap = cv2.VideoCapture(video_path)

# Save output video
save_output = True
output_path = "output_with_cows2.mp4"
if save_output:
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = 640
    height = 384
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (640, 384))
    results = model(frame)
    annotated_frame = results[0].plot()

    # Cow detection
    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            if cls_id == 20:
                print(f"🐄 Cow detected in frame {frame_count}")

    # Optional: Save a single frame preview image
    if frame_count == 0:
        cv2.imwrite("preview_frame.jpg", annotated_frame)
        print("Saved preview_frame.jpg")

    # Save to video
    
    if save_output:
        out.write(annotated_frame)

    frame_count += 1

cap.release()
if save_output:
    out.release()

print("✅ Detection complete. Output saved to:", output_path)



