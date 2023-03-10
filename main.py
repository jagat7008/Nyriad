import paramiko
ssh_client =paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname="16.171.28.203", username= "ubuntu",password= "Jagatjit")
stdin, stdout, stderr = ssh_client.exec_command("sudo ls")

ftp_client=ssh_client.open_sftp()
ftp_client.get("/home/ubuntu/text.txt","test.txt")
ftp_client.close()