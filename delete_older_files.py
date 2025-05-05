import os
import sys
import datetime
req_path = input("Enter path: ")
age = 1
if not os.path.exists(req_path):
    print("Not a valid path")
    sys.exit(1)

elif os.path.isfile(req_path):
    print("It is a file, provide dir")
    sys.exit(2)

else:
    list_f = os.listdir(req_path)
    today = datetime.datetime.now()
    for each in list_f:
        full_p = os.path.join(req_path,each)
        creat_t = datetime.datetime.fromtimestamp(os.path.getctime(full_p))
        no_of_d = (today-creat_t).days
        if no_of_d >= age: 
            #os.remove(full_p)
            print(full_p, no_of_d)


