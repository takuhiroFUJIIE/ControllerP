import sys
import time
import pyvisa as visa

def EmargencyStop():
    rm = visa.ResourceManager()
    usb = rm.open_resource(rm.list_resources()[0])
    order = "L:E"
    ret=usb.query(order)
    #print(ret)
    rm.close()
    return ret

#GoToLimitPosition(0)
