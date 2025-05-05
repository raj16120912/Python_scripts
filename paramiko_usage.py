import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(username='rajp',hostname='rajp.test',key_filename='/home/rajp/.ssh/id_rsa')
stdin,stdout,stderr = ssh.exec_command('df -h')

print (f"Output: {stdout.readlines()} \n ---------------------- \n Error: {stdout.readlines()}")

