from netmiko import ConnectHandler

myserver = {
    'device_type': 'linux',
    'host':   '192.168.253.3',  #Your Server IP
    'username': 'nadie', #your Server Username
    'password': 'yuri2ne1', #your server password
    'port' : 22,
    'secret': '',
}

net_connect = ConnectHandler(**myserver)
output = net_connect.send_command('uname -a')
print(output)
