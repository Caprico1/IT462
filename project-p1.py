from paramiko import SSHClient, AutoAddPolicy


'''
configures routers by sshing into them and taking the data provided by the 
user to configure connections on fa0/0


'''
router1 = input("Input address for Router 1 to SSH to: ")
r1_user = input("Username for Router 1: ")
r1_pass = input("Password for Router 1: ")
r1_ip = input("Enter IP for router 1: ")
r1_subnet = input("Enter NetMask for route 1: ")


router2 = input("Input address for Router 2 to SSH to: ")
r2_user = input("Username for Router 2: ")
r2_pass = input("Password for Router 2: ")
r2_ip = input("Enter IP for router 2: ")
r2_subnet = input("Enter NetMask for route 2: ")


ssh = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=router1, port=22, username=r1_user, password=r1_pass)
ssh.exec_command('en')
ssh.exec_command('conf t')
ssh.exec_command('interface FastEthernet0/0')
ssh.exec_command('no shutdown')
ssh.exec_command('media-type 100BaseX')
ssh.exec_command('full-duplex')
ssh.exec_command('ip address {0} {1}'.format(r1_ip, r1_subnet))
ssh.close()


ssh2 = SSHClient()
ssh.set_missing_host_key_policy(AutoAddPolicy())
ssh.connect(hostname=router2, port=22, username=r2_user, password=r2_pass)
ssh.exec_command('en')
ssh.exec_command('conf t')
ssh.exec_command('interface FastEthernet0/0')
ssh.exec_command('no shutdown')
ssh.exec_command('media-type 100BaseX')
ssh.exec_command('full-duplex')
ssh.exec_command('ip address {0} {1}'.format(r2_ip, r2_subnet))
ssh.close()

