from dotenv import load_dotenv
import os

load_dotenv()

# time variables
times = os.getenv('TIMES', 1)
total_time = os.getenv('TOTAL_TIME', 180)

# URL variables
src = os.getenv('ORIGIN_SRC')
configURL = os.getenv('CONFIG_URL')

# throughput variables
min_download = os.getenv('MIN_DOWNLOAD', 100 * 1024)
max_download = os.getenv('MAX_DOWNLOAD', 500 * 1024)
upload = os.getenv('UPLOAD', 500 * 1024)

# possibility to change network speed
possibility = os.getenv('POSSIBILITY', 0.1)