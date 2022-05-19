import paramiko
import telnetlib


def startssh(host, user, passwd):
 
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=host, username=user, password=passwd)
        return ssh_client

    except:
        return False

def exec_with_ssh(host, username, password, command):

    ssh_client = startssh(host.strip(), username, password)

    if ssh_client:
        output = open('terminaloutput.csv', 'a', encoding='utf-8')
        ssh_stdin, ssh_stdout, ssh_stderr = ssh_client.exec_command(command)
        outputstring = ssh_stdout.read()
        erroout = ssh_stderr.read()
        output.write(outputstring.decode())
        output.write(erroout.decode())
        output.write('\n')
        ssh_client.close()
        print ('Actions Completed Without Errors')
        return True

    else :
        print ('\n Authentication Failed Or Connection Error To Host ' + host)
        return False
    
        


def exec_with_telnet(host, username, password, command):

    tn = telnetlib.Telnet()
    tn.open(host, port=23)
    tn.read_until(b"login: ", 5)
    tn.write(username.encode('ascii') + b"\n")

    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    output = open('terminaloutput.csv', 'a', encoding='utf-8')
    command += "\n"
    tn.write(command.encode('utf-8'))
    tn.write(b"exit\n")
    output.write(tn.read_all().decode())
    print("Finished!")

def main(choice, host, username, password, command):

    ######### SSH #########
    if choice == "1":
        return exec_with_ssh(host, username, password, command)

    ######### Telnet #########
    elif choice == "2":
        
        exec_with_telnet(host, username, password, command)
    else: 
        print("Please Enter A Valid Choice")
