import cv2
import numpy as np

from other import frame_preprocess, frame_diff


class VideoPlayer:
    def __init__(self, video_file, composition):
        self.video_file = video_file
        self.composition = composition

    def run(self):
        prev_frame = None
        cap = cv2.VideoCapture(self.video_file)

        if not cap.isOpened():
            print("Error: Could not open video file")
            return

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if prev_frame is None:
                prev_frame = frame
                continue

            for roi in self.composition:
                points = roi.points

                x1, y1 = points['x2'], points['y2']
                x4, y4 = points['x3'], points['y4']
                prev_roi_region = prev_frame[y1:y4, x1:x4]

                # Extracting the specific region from the current frame
                frame_roi_region = frame[y1:y4, x1:x4]

                # Process ROI
                diff_im = frame_diff(frame_preprocess(prev_roi_region), frame_preprocess(frame_roi_region))

                pts = np.array([(points['x1'], points['y1']),
                                (points['x2'], points['y2']),
                                (points['x3'], points['y3']),
                                (points['x4'], points['y4'])], np.int32)
                pts = pts.reshape((-1, 1, 2))
                #cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

                # Overlay processed ROI on the frame
                frame[y1:y4, x1:x4] = diff_im

            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            prev_frame = frame.copy()

        cap.release()
        cv2.destroyAllWindows()
