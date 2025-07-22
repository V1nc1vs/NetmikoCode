import threading
from netmiko import ConnectHandler

#------------------------------------------------------------------------------#

def port_access_vlan(device , vlan_id , interface , description):

    net_connect=ConnectHandler(**device)

    try:
        commands=[
                "interface "+interface ,
                "description "+description,
                "switchport mode access" ,
                "switchport access vlan "+vlan_id,
                "spanning-tree portfast",
                "spanning-tree bpduguard enable",
                "storm-control action shutdown",
                "storm-control broadcast level 20.00 2.00",
                "shutdown",
                "no shutdown"
            ]

        net_connect.send_config_set(commands)
        net_connect.save_config()
        print(f"\n\n******************VERIFY CONFIGURATION*********************")
        print(net_connect.send_command("show running-config interface "+interface))
    except Exception as e:
        print(f'Failed to connect to device with {device["ip"]} with error {e}')



#-----------------------------------------------------------------------------#



i=True

devices_arguments=[]

while( i is True ):

    print("\n\n*************BEGIN CONFIGURATION*****************")

    print("\n\ninsert IP of device : ")
    device_ip=input()
    print("insert VLAN ID: ")
    vlan_id=input()
    print("insert interface :")
    interface=input()
    print("insert description:")
    description=input()


    device={
        "device_type" : "cisco_ios" ,
        "ip" : device_ip ,
        "username" : "your username" ,
        "password" : "you password"
    }

    device_arguments={
        "device" : device ,
        "vlan_id" : str(vlan_id) ,
        "interface" : str(interface) ,
        "description" : str(description)
    }

    devices_arguments.append(device_arguments)


    print("\n\nConfigure another interface? ('Yes' o 'No') :")
    answer=input()
    if(answer!= 'Yes'):
        i=False


th=[]
for dev_arg in devices_arguments:
    th=threading.Thread(target=port_access_vlan,args=(dev_arg["device"],dev_arg["vlan_id"],dev_arg["interface"],dev_arg["description"],))
    th.start()
    th.join()