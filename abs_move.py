#機械原点を0点とする
import sys
import time
import pyvisa as visa

def ABS_MOVE(AXIS, destination, unit):
  # connect controller
  rm = visa.ResourceManager()
  # rm.list_resources()
  usb = rm.open_resource(rm.list_resources()[0])
  
  # set command
  order='A:'
  order+=str(AXIS)
  pulse=int(destination/unit)
  if pulse>=0:
    order+='+P'
  elif pulse<0:
    order+='-P'
    pulse*=-1
  order+=str(pulse)
  print(order)
  
  # send command
  result=usb.query(order)
  if result=='NG\r\n':
    print('command error')
    quit()

  result=usb.query("G:")
  if result=='NG\r\n':
    print('command error')
    quit()
  
  # get current position
  # time.sleep(1)
  # pos=usb.query("Q:")
  # pos=pos.replace(' ','')
  # pos_list=pos.split(',')
  
  # while pos_list[-1]!='R\r\n':
  #   current_pulse=int(pos_list[AXIS-1])
  #   print('\rcurrent position : '+str(current_pulse*unit), end='')
  #   time.sleep(1)
  #   pos=usb.query("Q:")
  #   pos=pos.replace(' ','')
  #   pos_list=pos.split(',')
    
  #   # Get moved position
  # current_pulse=int(pos_list[AXIS-1])
  # print('\rcurrent position : '+str(current_pulse*unit), '   ')
  
  # saigo
  rm.close()
  #print('finish')
  
#ABS_MOVE(int(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
