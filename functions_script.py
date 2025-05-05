import os
import time

def run_command(cmd):
    print(f"Running {cmd}....")
    time.sleep(5)
    os.system(cmd)

run_command('ls')

run_command('df -h')

