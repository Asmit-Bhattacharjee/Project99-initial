import os
import time
import shutil
path = "AllFiles"
days = 0
time_sec = time.time()
final_time = days+time_sec
if os.path.exists(path):
    all_files = os.walk(path)
    for file in all_files:
        files = os.path.join()
        ctime = os.stat(path).st_ctime
        if(ctime>time_sec):
            os.remove(path)
        else: 
            shutil.rmtree()
else:
    print("error")