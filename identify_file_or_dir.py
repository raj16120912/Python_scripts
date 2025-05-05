import os
import sys

path = input("Enter path: ")
if os.path.exists(path):
    df_l = os.listdir(path)
else:
    print('Not a valid path')
    sys.exit()

for each in df_l:
    obj = os.path.join(path,each)
    if os.path.isfile(obj):
        print(f"{obj} is a file")
    else:
        print(f"{obj} is a dir")

