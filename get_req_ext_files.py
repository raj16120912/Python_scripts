import os
req_path = input("Enter path: ")


if os.path.exists(req_path):
    req_ext = input("Enter ext: ")
    if len(req_ext) != 0: 
        all_f = os.listdir(req_path)
        all_ext = []
        for each in all_f:
            if each.endswith(req_ext):
                all_ext.append(each)
        if len(all_ext) == 0:
            print(f"No files with such ext")
        else:
            print(f"Total {len(all_ext)} are found, here's the list {all_ext}")
    else: 
        print("Empty ext")
else:
    print(f"{req_path} Not a valid path")