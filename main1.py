import argparse
import paramiko


def main(ip, username, password):
    # Connect to SSH
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip, username=username, password=password)
    
    # Execute command on remote server
    stdin, stdout, stderr = ssh_client.exec_command("sudo ls")
    
    # Open SFTP connection and download file
    ftp_client = ssh_client.open_sftp()
    ftp_client.get("/home/ubuntu/text.txt","test.txt")
    ftp_client.close()
    
    # Print output of command
    # print(stdout.read())

if __name__== '__main__':
    parser = argparse.ArgumentParser(description='Connect to a remote server over SSH and download a file')
    parser.add_argument('--ip', type=str, help='IP address of remote server')
    parser.add_argument('--username', type=str, help='Username for remote server login')
    parser.add_argument('--password', type=str, help='Password for remote server login')
   
    
    args = parser.parse_args()
    
    main(args.ip, args.username, args.password)
    