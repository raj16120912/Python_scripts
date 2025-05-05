import subprocess

output = subprocess.Popen("python3 Identify_seasons.py")
f = open('test.test', "w")
f.write(str(output))
f.close


