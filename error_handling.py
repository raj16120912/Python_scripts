import os

req_path = "/home/rajp/Backup/python/"
chn_dir = "/home/rajp/Backup/python/test/backup.txt"

try:
    print(os.getcwd())
    os.chdir(chn_dir)
    print(f"New cwd is: {os.getcwd()}")
except NotADirectoryError:
    print ("Only provide directory")
except FileNotFoundError:
    print ("Path invalid")
except PermissionError:
    print ("You dont have permission")

