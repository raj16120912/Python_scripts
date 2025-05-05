import csv

req_path = "/home/rajp/Backup/python/test/dmn1.csv"

fo = open(req_path)
read_csv = csv.reader(fo)
for each in read_csv:
    print(each)

fo.close()