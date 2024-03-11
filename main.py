# main.py

from RoiClass import ComposeROI
from other import process_roi
from video_streamer2 import VideoStream
import cv2


def main():
    video_path = "./data/crusher_closeup.mp4"

    compose_roi = ComposeROI("params2.json")
    roi_points = [roi.points for roi in compose_roi]

    vs = VideoStream(cam_name="Video Stream", path=video_path, roi_points=roi_points, transform=process_roi)
    vs.start()

    while True:
        if not vs.running():
            break

        vs.show_frame()

    vs.stop()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
