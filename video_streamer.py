import time
import cv2
import numpy as np

from thresh import process_roi


class VideoPlayer:
    def __init__(self, video_file, roi_comp):
        self.video_file = video_file
        self.roi_comp = roi_comp
        self.timestamps = []

    def run(self):

        cap = cv2.VideoCapture(self.video_file)

        if not cap.isOpened():
            print("Error: Could not open video file")
            return

        while True:
            _, prev_frame = cap.read()
            prev_timestamp = time.time()
            self.timestamps.append(prev_timestamp)

            ret, frame = cap.read()
            if not ret:
                break

            processed_frame = process_roi(self.roi_comp, prev_frame, frame)

            current_time_stamp = time.time()
            frame_time_diff = current_time_stamp - prev_timestamp
            self.timestamps.append(frame_time_diff)
            # print(np.cumsum(self.timestamps))

            cv2.imshow('Video', processed_frame )
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def make_timestamp(self):
        cum_ts = np.cumsum(self.timestamps)
        return cum_ts
