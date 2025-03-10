import customtkinter as ctk
import qrcode
from PIL import Image, ImageTk
import cv2
import numpy as np

# Initialize App
app = ctk.CTk()
app.geometry("500x600")
app.title("QR Code Scanner & Generator")

# Function to Generate QR Code
def generate_qr():
    text = entry_text.get()
    if text.strip() == "":
        result_label.configure(text="Enter text to generate QR")
        return

    qr = qrcode.make(text)
    qr.save("generated_qr.png")

    img = Image.open("generated_qr.png")
    img = img.resize((200, 200))
    img = ImageTk.PhotoImage(img)
    qr_label.configure(image=img)
    qr_label.image = img
    result_label.configure(text="QR Code Generated!")

# Function to Scan QR Code
def scan_qr():
    cap = cv2.VideoCapture(0)  # Open webcam
    detector = cv2.QRCodeDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        data, bbox, _ = detector.detectAndDecode(frame)
        if data:
            result_label.configure(text=f"Scanned: {data}")
            break

        cv2.imshow("QR Code Scanner - Press Q to Exit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# UI Elements
ctk.CTkLabel(app, text="QR Code Generator", font=("Arial", 16)).pack(pady=10)
entry_text = ctk.CTkEntry(app, width=300)
entry_text.pack(pady=5)
generate_btn = ctk.CTkButton(app, text="Generate QR", command=generate_qr)
generate_btn.pack(pady=5)

qr_label = ctk.CTkLabel(app, text="Your QR will appear here", width=200, height=200, fg_color="gray")
qr_label.pack(pady=10)

scan_btn = ctk.CTkButton(app, text="Scan QR", command=scan_qr)
scan_btn.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Run App
app.mainloop()



