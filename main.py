from RoiClass import ComposeROI
from video_streamer import VideoPlayer

comp_roi = ComposeROI("params.json")
video_player = VideoPlayer("./data/crusher_bin_bridge.mkv", comp_roi)
video_player.run()


print(video_player.make_timestamp())

