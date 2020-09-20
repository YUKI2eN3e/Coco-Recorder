import os
from datetime import datetime
import time

url = "https://www.youtube.com/channel/UCS9uQI-jC3DE0L4IpXyvr6w/live"

def getFileName():
    now = datetime.now() # current date and time
    date_time = now.strftime("%m-%d-%Y,%H;%M;%S")
    file_name ="COCO_LiveStream_{}.mkv".format(date_time)
    return file_name

cont = True
stream_test = "streamlink {}".format(url)
while cont:
    if not os.system(stream_test):
        print("Stream is Live")
        file_name = getFileName()
        command = "streamlink --hls-live-restart {} best -o {}".format(url, file_name)
        os.system(command)
        print("Stream Saved")
        time.sleep(300)
    else:
        print("Waiting for stream to start")
        time.sleep(30)