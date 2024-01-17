import os
from reset_env import reset_env

reset_env()
os.system('python video_js.py')
os.system('python hls_js.py')
os.system('python dplayer.py')