import cv2 as cv

def eventloop(cap_source: int | str) -> None:
    cap = cv.VideoCapture(cap_source)
    cap.set(cv.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv.CAP_PROP_FRAME_HEIGHT, 1080)
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break

        cv.imshow("Visualization", frame)
        if cv.waitKey(1) == ord("q"):
            cv.destroyAllWindows()
            break