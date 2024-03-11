import cv2
import numpy as np


def frame_diff(first_roi, second_roi):
    diff_im = cv2.subtract(second_roi, first_roi)
    conv_gray = cv2.cvtColor(diff_im, cv2.COLOR_RGB2GRAY)
    ret, mask = cv2.threshold(conv_gray, 100, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

    # Ensure proper datatype and dimensions of mask
    mask = mask.astype(np.uint8)

    # Create a copy of the difference image
    diff_im_colored = cv2.cvtColor(diff_im, cv2.COLOR_RGB2BGR)

    # Set pixels where the mask is true to red in the colored difference image
    diff_im_colored[mask != 255] = [0, 0, 255]

    return diff_im_colored

def frame_preprocess(frame_ref):
    return cv2.cvtColor(frame_ref, cv2.COLOR_BGR2RGB)
