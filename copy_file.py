import os

s_f = "/home/rajp/Backup/python/test.txt"

d_f = "/home/rajp/Backup/python/test/backup.txt"

s_f_o = open(s_f)
content = s_f_o.read()
s_f_o.close()

d_f_o = open(d_f, "w")
d_f_o.write(content)
d_f_o.close()

