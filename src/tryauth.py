import sys
from cmd import Cmd
from utils import select_utility
from parser import parsing
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError

"""ARGS
   address - ip address/dns name
   port - custom port for accessing NETCONF over SSH
   utility - utility you want to perform on device 
"""




# Get data and parse the input 
def get_credentials():
    #hostname = input("Device hostname: ")
    junos_user = input('JunOS user: ')
    junos_pass = getpass('JunOS or SSH key password: ')
    return junos_user, junos_pass


def connect_to_device(host_address, usr, passwrd, custom_port=None):
    if custom_port != None:
        dev = Device(host=host_address, user=usr, passwd=passwrd, port=custom_port)
    else:
        dev = Device(host=host_address, user=usr, passwd=passwrd)
    try:
        dev.open()
        print(f'Successfully connected to device {host_address}')
    except ConnectError as err:
        print(f'Connection ERROR - {err}')
    except Exception as e:
        print(f'Unsuspected behavior, ERROR : {e}')
    return dev
    



def main():
    args = parsing()
    print(args)
    user, passwd = get_credentials()
    host = args.address
    port = args.port
    dev = connect_to_device(host, user, passwd, port)
    if args.utility != None:
        utility = args.utility
        select_utility(utility, dev)
    while True:
        utility = input('\nPlease - type in utility you wany to perform on the device (\'help\' for description): ')
        select_utility(utility, dev)
    """try:
        # Opens the connection tunnel to device through NETCONF
        dev.open()
    
    # ConnectionError is treeaten different than any other
    except ConnectError as err:
        print(f'Cannot connect to device: ERROR - {err}')
        sys.exit()
        
    # Include Exception handling
    except Exception as e:
        print(e)
        sys.exit()
    print(dev.facts)"""
    
    # Closes the connection tunnel to device through NETCONF
    #dev.close()


if __name__ == "__main__":
    main()