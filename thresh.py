import cv2
import numpy as np

from utils import write_csv


def frame_diff(first_frame, prev_frame):
    diff_im = cv2.absdiff(prev_frame, first_frame)

    intensity = np.sum(diff_im)
    # write_csv(intensity)
    # if intensity > 2000000:

    # diff_im = first_frame
    conv_gray = cv2.cvtColor(diff_im, cv2.COLOR_RGB2GRAY)
    _, mask = cv2.threshold(conv_gray, 200, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    diff_im_colored = cv2.cvtColor(diff_im, cv2.COLOR_RGB2BGR)
    diff_im_colored[mask != 255] = [0, 0, 255]

    return diff_im_colored


def frame_preprocess(frame_ref):
    return cv2.cvtColor(frame_ref, cv2.COLOR_BGR2RGB)


def process_roi(roi_comp, prev_frame, frame):
    for roi in roi_comp:
        points = roi.points

        x1, y1 = points['x2'], points['y2']
        x4, y4 = points['x3'], points['y4']
        prev_roi_region = prev_frame[y1:y4, x1:x4]
        frame_roi_region = frame[y1:y4, x1:x4]

        diff_im = frame_diff(frame_preprocess(prev_roi_region), frame_preprocess(frame_roi_region))

        frame_roi_region = diff_im[:, :, 2]
        frame[y1:y4, x1:x4][frame_roi_region == 255] = [0, 0, 255]

        return frame
