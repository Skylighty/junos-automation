import argparse
import os
import string

def filepath(string):
    if os.path.isfile(string):
        return string
    else:
        raise FileNotFoundError(string)
    
def parsing():
    parser = argparse.ArgumentParser(prog='junos-handler',
                                     fromfile_prefix_chars='@',
                                     description='Options below')
    
    # Not necessary to parse it here.
    """parser.add_argument('-u', '--user',
                        metavar="",
                        help='Sepcify username to log into device')
    parser.add_argument('-p', '--pass',
                        metavar="",
                        help='Specify password for user to log into device')"""


    parser.add_argument('-a', '--address',
                        metavar='',
                        help='Specify IP address of the device or domain name')
    parser.add_argument('-p', '--port',
                        metavar="",
                        help='If you\'re using custom port for NETCONF in the device - specify it',
                        required=False)
    parser.add_argument('-u', '--utility',
                        metavar="",
                        help='Pass the utility you want to perform on the target device')
    args = parser.parse_args()
    return args