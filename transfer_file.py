#Import module for ssh,sftp through python
import paramiko

#Connect to sshclient
ssh = paramiko.SSHClient()
#Auto add host key checking
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Create connection to remote
ssh.connect(username='rajp',hostname='rajp.test',key_filename='/home/rajp/.ssh/id_rsa')
#open sftp connection
sftp_client = ssh.open_sftp()
#changing remote directory
sftp_client.chdir('/home/users/rajp/bind')
#getting remote dir
print(sftp_client.getcwd())
#Download from remote
sftp_client.get('/home/users/rajp/script','/home/rajp/Backup/python/test/script_dw')
#send to remote
sftp_client.put('/home/rajp/Backup/python/test/dmn1.csv','/home/users/rajp/dmn.csv')
#close remote sftp
sftp_client.close()
#close ssh connection
ssh.close()
