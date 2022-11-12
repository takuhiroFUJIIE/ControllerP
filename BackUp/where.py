#機械原点を0点とする
import sys
import time
import pyvisa as visa
if len(sys.argv)!=1:
  print('usage: python3.9 where.py')
  quit()
rm = visa.ResourceManager()
rm.list_resources()
usb = rm.open_resource(rm.list_resources()[0])
time.sleep(1)
pos=usb.query("Q:")
pos=pos.replace(' ','')
pos_list=pos.split(',')
for num in range(2):
  current_pulse=int(pos_list[num])
  print('AXIS : '+str(num+1))
  print('current pulse : '+str(current_pulse))
  if num==0:
    print('current position : '+str(current_pulse*0.0025)+' deg')
  elif num==1:
    print('current position : '+str(current_pulse*0.002)+' mm')
  else:
    print('????????')
print('finish')
