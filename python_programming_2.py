from paramiko import AutoAddPolicy, SSHClient




def check_for_nmap(ssh):
    stdin, stdout, stderr = ssh.exec_command('nmap --version')

    for line in stdout:
        print(line)
    return True

def run_nmap_sl(ssh, ip, filename=None):
    if filename is not None:

        stdin, stdout, stderr = ssh.exec_command('nmap  -vvvvv -sL {0} > {1}'.format(ip, filename))

        for line in stdout:
            print(line)
        return True

    else:

        stdin, stdout, stderr = ssh.exec_command('nmap  -vvvvv -sL {0}'.format(ip))

        for line in stdout:
            print(line)
        return True


if __name__ == '__main__':

    options = '''1. Scan and map devices if nmap is on the device '''

    host = ""
    port = 22
    username = ""
    pwd = ""

    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=host, port=port, username=username, password=pwd)

    stdin, stdout, stderr = ssh.exec_command('echo "Signed in as:" && whoami')


    for line in stdout:
        print(line)

    print(options)

    selected = input("Pick a action: ")
    if selected == "1":

        if check_for_nmap(ssh=ssh):
            ip = input("input IP address with CIDR: ")
            filename = input("If you wish to save to a file on the machine enter a filename: ")

            run_nmap_sl(ssh=ssh, ip=ip, filename=filename)

