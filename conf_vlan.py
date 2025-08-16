import os
from netmiko import ConnectHandler

SSH_CONFIG_PATH = os.path.expanduser('your_ssh_config_path')


def connect_to_device(device_ip,username,password):
    device = {
        'device_type' : 'cisco_ios',
        'ip' : device_ip,
        'username' : username,
        'password' : password,
        'ssh_config_file': SSH_CONFIG_PATH
    }

    return device

answer=True
while(answer==True):

    print('/****************CONNECT TO DEVICE*****************/')
    print('\n\n')
    print('DEVICE IP TO CONNECT TO:')
    device_ip=input()
    print('\n\n')
    print('USERNAME FOR CONNECTION:')
    username=input()
    print('\n\n')
    print('PASSWORD FOR CONNECTION:')
    password=input()
    print('\n\n')

    device=connect_to_device(device_ip,username,password)
    net_connect=ConnectHandler(**device)

    print('/****************CONFIGURE VLAN*****************/')
    print('\n\n')

    print('VLAN ID:')
    vlan_id=input()
    print('\n\n')

    
    typo_error=True
    while(typo_error==True):
        print('give the vlan a name [Yes/No]:')
        answer_vlan_name=input()
        if(answer_vlan_name!='Yes'):
            if(answer_vlan_name=='No'):
                typo_error=False
            else:
                print('Please , enter either "Yes" or "No"')
                print('\n\n')
        else:
            typo_error=False
            print('VLAN NAME:')
            vlan_name=input()
            print('\n\n')

    ######################################################################################

    typo_error=True
    while(typo_error==True):
        print('create an associated SVI [Yes/No]:')
        answer_interface_vlan=input()
        if(answer_interface_vlan!='Yes'):
            if(answer_interface_vlan=='No'):
                typo_error=False
            else:
                print('Please , enter either "Yes" or "No"')
                print('\n\n')
        else:
            typo_error=False
            print('SVI IP ADDRESS:')
            svi_ip_address=input()
            print('\n\n')
            print('SVI MASK:')
            svi_mask=input()
            print('\n\n')
            
    ####################################################################################

    typo_error=True
    while(typo_error==True):
        print('configure hsrp [Yes/No]:')
        answer_hsrp_conf=input()
        if(answer_hsrp_conf!='Yes'):
            if(answer_hsrp_conf=='No'):
                typo_error=False
            else:
                print('Please , enter either "Yes" or "No"')
                print('\n\n')
        else:
            typo_error=False
            print('HSRP PRIORITY VALUE:')
            hsrp_priority_value=input()
            print('\n\n')
            print('HSRP VIP ADDRESS:')
            hsrp_vip_address=input()
            print('\n\n')
            

    list_of_commands=["vlan "+vlan_id]
    if(answer_vlan_name=='Yes'):
        list_of_commands.append("name "+vlan_name)
    if(answer_interface_vlan=='Yes'):
        list_of_commands_svi=[
                            "interface vlan "+vlan_id,
                            "no shutdown",
                            "ip address "+svi_ip_address+" "+svi_mask
                            ]
        list_of_commands.extend(list_of_commands_svi)
        if(answer_hsrp_conf=='Yes'):
            list_of_commands_hsrp=[
                                "standby "+vlan_id+" priority "+hsrp_priority_value,
                                "standby "+vlan_id+" preempt",
                                "standby "+vlan_id+" ip "+hsrp_vip_address
                                ]
            list_of_commands.extend(list_of_commands_svi)
    




    net_connect.send_config_set(list_of_commands)
    net_connect.save_config()



    typo_error=True
    while(typo_error==True):
        print('continue configuring another device [Yes/No]:')
        answer_continue=input()
        if(answer_continue!='Yes'):
            if(answer_continue=='No'):
                typo_error=False
                answer=False
            else:
                print('Please , enter either "Yes" or "No"')
                print('\n\n')
        else:
            typo_error=False
            answer=True
            print('\n\n')



    

    
