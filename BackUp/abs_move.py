#機械原点を0点とする
import sys
import time
import pyvisa as visa
if len(sys.argv)!=4:
  print('usage: python3.9 abs_move.py [AXIS] [value] [unit]')
  quit()
rm = visa.ResourceManager()
rm.list_resources()
usb = rm.open_resource(rm.list_resources()[0])
AXIS=int(sys.argv[1])
destination=float(sys.argv[2])
unit=sys.argv[3]
pulse=int(0)
order='A:'
if AXIS==1 or AXIS==2:
  order+=str(AXIS)
  if AXIS==1 and unit=="deg":
    pulse=int(destination/0.0025)
  elif AXIS==2 and unit=="mm":
    pulse=int(destination/0.002)
  else:
    print('I can only treat AXIS 1 with [deg] or AXIS 2 with mm on 2021A@BL10 EDM experiment.')
    quit()
else:
  print('ima tsukatterunoha 2ziku dake')
  quit()
if pulse>=0:
  order+='+P'
elif pulse<0:
  order+='-P'
  pulse*=-1
order+=str(pulse)
print(order)
result=usb.query(order)
if result=='NG\r\n':
  print('command error')
  quit()
result=usb.query("G:")
if result=='NG\r\n':
  print('command error')
  quit()
time.sleep(1)
pos=usb.query("Q:")
pos=pos.replace(' ','')
pos_list=pos.split(',')
while pos_list[-1]!='R\r\n':
  current_pulse=int(pos_list[AXIS-1])
  print('current pulse : '+str(current_pulse))
  if AXIS==1:
    print('current position : '+str(current_pulse*0.0025)+' deg')
#    0.005 deg/pulse? 0.0025 deg/pulse?
#    print('current position : '+str(current_pulse*0.005)+' deg')
  elif AXIS==2:
    print('current position : '+str(current_pulse*0.002)+' mm')
  else:
    print('AXIS error')
  time.sleep(1)
  pos=usb.query("Q:")
  pos=pos.replace(' ','')
  pos_list=pos.split(',')
current_pulse=int(pos_list[AXIS-1])
print('current pulse : '+str(current_pulse))
if AXIS==1:
  print('current position : '+str(current_pulse*0.0025)+' deg')
#  0.005 deg/pulse? 0.0025 deg/pulse?
#  print('current position : '+str(current_pulse*0.005)+' deg')
elif AXIS==2:
  print('current position : '+str(current_pulse*0.002)+' mm')
else:
  print('AXIS error')
print('finish')
