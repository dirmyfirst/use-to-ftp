import paramiko
import os
'''
从远程服务器下载文件到本地或上传至远程服务器

'''
#服务器信息，主机名（IP地址）、端口号、用户名及密码、获取的远程与本地文件
host_ip = '192.168.112.111'
port = 22
username = 'test'
password = 'test'
remote_path = '/home/tes/20180820/'
local_path = r'D:\test'
if os.path.exists(local_path):
    print('该路径已存在该文件夹...\n')
else:
    print(f'正在创建文件夹{local_path}...\n')
    os.mkdir(local_path)

#下载使用方式
def remote_sftp(host_ip, port, remote_path, local_path, username, password):
    client = paramiko.Transport((host_ip,port))
    client.connect(username = username,password = password)
    print('Login...\n')
    sftp = paramiko.SFTPClient.from_transport(client)
    files = sftp.listdir(remote_path)
    file_list = [f for f in files]
    print(f'该路径下存在的文件如下： {file_list}\n')
    for f in files:
        print(f'开始下载 {f}...\n')
        sftp.get(os.path.join(remote_path,f),os.path.join(local_path,f))
        print(f'{f}下载完成！\n')
    client.close()

#上传使用方式
def put_sftp(host_ip, port, remote_path, local_path, username, password):
    client = paramiko.Transport((host_ip,port))
    client.connect(username = username,password = password)
    print('Login...\n')
    sftp = paramiko.SFTPClient.from_transport(client)
    files = os.listdir(local_path)
    ftp_files = sftp.listdir(remote_path)
    file_list = [f for f in files]
    ft_file_list = [f for f in ftp_files]
    print(f'服务器上存在的文件列表如下：{ft_file_list}\n')
    print(f'待上传的文件列表如下： {file_list}\n')
    for f in files:
        if f in ft_file_list:
            print(f'已存在该文件...\n')
        else:
            print(f'开始上传 {f}...\n')
            sftp.put(os.path.join(local_path,f),os.path.join(remote_path,f))
            print(f'{f}上传完成！\n')
    client.close()
 

if __name__ == '__main__':
    put_sftp(host_ip,port,remote_path,local_path,username,password)
    #remote_sftp(host_ip,port,remote_path,local_path,username,password)
    print('completed！')
