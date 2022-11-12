import sys
import time
import pyvisa as visa

def GoToLimitPosition(ch):
    rm = visa.ResourceManager()
    usb = rm.open_resource(rm.list_resources()[0])
    order = "H:"+str(ch)
    ret=usb.query(order)
    print(ret)
    rm.close()
    return ret

#GoToLimitPosition(0)
