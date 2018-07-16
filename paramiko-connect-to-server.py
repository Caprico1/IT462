from paramiko import AutoAddPolicy, SSHClient


host = "192.168.1.108"
port = 22
username = ""
pwd = ""

ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=host, port=port, username=username, password=pwd)
stdin, stdout, stderr = ssh.exec_command('echo "You have signed in as:" && whoami')

for line in stdout:
    print(line)

ssh.close()
