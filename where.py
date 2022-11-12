#機械原点を0点とする
import sys
import time
import pyvisa as visa

def WHERE(add, ch):
  rm = visa.ResourceManager()
  usb = rm.open_resource(rm.list_resources()[0])
  pos=usb.query("Q:")
  pos=pos.replace(' ','')
  pos_list=pos.split(',')
  # print(pos_list[ch])
  rm.close()
  return int(pos_list[ch])
#WHERE(0, 0)
