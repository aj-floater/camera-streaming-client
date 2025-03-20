import cv2
import tkinter as tk
from tkinter import simpledialog

# Function to get the RTSP URL from user input
def get_server_ip():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    server_ip = simpledialog.askstring("RTSP Stream", "Enter the RTSP Server IP Address:")
    return server_ip

# Ask the user for the server IP
server_ip = get_server_ip()

# Check if the user provided an IP
if not server_ip:
    print("No IP entered. Exiting.")
    exit(1)

# Construct the RTSP URL
rtsp_url = f"rtsp://{server_ip}:8554/mystream"
print(f"Connecting to RTSP stream at: {rtsp_url}")

# Open the RTSP stream using OpenCV
cap = cv2.VideoCapture(rtsp_url)
if not cap.isOpened():
    print("Error: Cannot open RTSP stream. Check the URL and network connectivity.")
    exit(1)

# Create a resizable OpenCV window
window_name = "Client - RTSP Stream"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)  # Allow resizing
cv2.resizeWindow(window_name, 800, 600)  # Set initial size

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