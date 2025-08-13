import os
from netmiko import ConnectHandler

SSH_CONFIG_PATH = os.path.expanduser('your_ssh_config_file_path')

def connect_to_device(device_ip):

    device={
        'device_type' : 'cisco_ios' ,
        'ip' : device_ip ,
        'username' : 'your_username' ,
        'password' : 'your_password' ,
        'ssh_config_file': SSH_CONFIG_PATH
    }

    return device


answer=True
while(answer==True):
    print('/****** ROUTED INTERFACE CONF **********/\n\n')
    print("Enter DEVICE IP you want to connect:")
    device_ip=input()
    print('\n\n')

    print("Enter INTERFACE to configure:")
    interface=input()
    print('\n\n')

    print("Enter IP ADDRESS :")
    ip_address=input()
    print('\n\n')

    print("Enter IP NETMASK :")
    netmask=input()
    print('\n\n')


    device=connect_to_device(device_ip)
    net_connect=ConnectHandler(**device)
    list_of_commands=["interface "+interface,
                      "no switchport",
                      "ip address "+ip_address+" "+netmask,
                      "no shutdown",
                      ]
    net_connect.send_config_set(list_of_commands)
    net_connect.save_config()
    print('\n\n')

    print('/****** ROUTED INTERFACE CONF **********/\n\n')

    output=net_connect.send_command("show running-config interface "+interface)
    print(f'DEVICE IP: {device['ip']}\n\n{output}\n\n')

    print('/*********************************************/\n\n')

    error_typo=True
    while(error_typo == True):
        print('Would you connect to another device [Yes/No]:')
        question=input()
        print('\n')
        if(question != 'Yes'):
            if(question != 'No'):
                print('Please , type either "No" or "Yes"\n')
            else:
                error_typo = False
                answer = False
        else:
            error_typo = False


