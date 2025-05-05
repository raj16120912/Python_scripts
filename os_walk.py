import os
req_path = "/home/rajp/Backup/"

os_walk = os.walk(req_path)

for p,d,f in os_walk:
    if len(f) != 0:
        for each in f:
            full_p = os.path.join(p,each)
            print(full_p)
        print ("-------------")
