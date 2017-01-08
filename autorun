import os
import time
from imp import *;

print("test")

import evolution2

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

def autorun():
    target_file = r"C:\Users\TattChee\PycharmProjects\santa_gift/evolution2.py"
    print("Auto-Run Enabled")
    last_save_time = os.path.getmtime(target_file)
    while(True):
        current_save_time = os.path.getmtime(target_file)
        if (last_save_time != current_save_time):
            print(" ===> File Updated, Re-running...")
            # try:
                # reload(evolution2)
                # evolution2.run_test()
            # except ValueError:
                # print("Error in Main File")
            reload(evolution2)
            evolution2.run_test()
            last_save_time = os.path.getmtime(target_file)
            
    return

autorun()
