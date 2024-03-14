import json


class ROI:
    def __init__(self, **kwargs):
        self.points = kwargs


class ComposeROI:
    """
    calls a json file, iterates over all ROI's.
    ROI key must start with roi
    """
    def __init__(self, json_file):
        self.rois = []
        with open(json_file, 'r') as f:
            data = json.load(f)
            for roi_name, roi_data in data.items():
                if roi_name.startswith("roi"):
                    roi = ROI(**roi_data)
                    self.rois.append(roi)

    def add_roi(self, roi):
        self.rois.append(roi)

    def __iter__(self):
        return iter(self.rois)
