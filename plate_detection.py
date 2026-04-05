import cv2

def detect_plate(frame):
    plate_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_russian_plate_number.xml"
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

    plate_images = []

    for (x, y, w, h) in plates:
        plate = frame[y:y+h, x:x+w]
        plate_images.append(plate)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)

    return frame, plate_images