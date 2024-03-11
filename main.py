from RoiClass import ComposeROI
from video_streamer import VideoPlayer

comp_roi = ComposeROI("params2.json")
video_player = VideoPlayer("./data/crusher_closeup.mp4", comp_roi)
video_player.run()
