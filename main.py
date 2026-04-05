import cv2
from plate_detection import detect_plate
from ocr import read_text

# Open video
video = cv2.VideoCapture("videos/test1.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    # Detect number plates
    frame, plates = detect_plate(frame)

    print("Plates found:", len(plates))

    for plate in plates:

        texts = read_text(plate)

        for text in texts:
            print("Detected Text:", text)

            # Show text on screen
            cv2.putText(frame, text, (50,50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1, (0,255,0), 2)

    # Show video frame
    cv2.imshow("Traffic OCR", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()