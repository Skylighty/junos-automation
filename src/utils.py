import sys
from lxml import etree

def select_utility(utility, dev):
    if utility == 'fib':
        fib(dev)
    elif utility == 'rib':
        rib(dev)
    elif utility == 'devinfo':
        devinfo(dev)
    if utility == 'help':
        help(dev)
    elif utility == 'exit':
        exit()

def fib(dev):
   sw = dev.rpc.get_route_information({'format':'text'})
   print(etree.tostring(sw, encoding='unicode')) 

def rib(dev):
    pass

def devinfo(dev):
    print(dev.facts)
    
def help():
    print('devinfo - display information about the device')
    print('fib - show the FIB table')
    print('rib - show the RIB table for')
    print('help - display this list of commands')

def exit():
    sys.exit()