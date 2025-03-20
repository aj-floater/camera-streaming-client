import cv2

# Replace <server-ip> with the actual server IP.
rtsp_url = "rtsp://<server-ip>:8554/mystream"
print(f"Connecting to RTSP stream at: {rtsp_url}")

# Open the RTSP stream using OpenCV
cap = cv2.VideoCapture(rtsp_url)
if not cap.isOpened():
    print("Error: Cannot open RTSP stream. Check the URL and network connectivity.")
    exit(1)

# Create a fullscreen window to display the stream
window_name = "Client - RTSP Stream"
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to retrieve frame from RTSP stream")
        break

    # Display the live stream
    cv2.imshow(window_name, frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Cleanup resources
cap.release()
cv2.destroyAllWindows()