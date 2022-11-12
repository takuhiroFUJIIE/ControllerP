import numpy
import tkinter
from tkinter import ttk
import time

########################
import where
import abs_move
import GoToLimitPosition
import ChangeHostMode
import EmargencyStop

# address, ch, name, unit per pulse, software low limit, up limit
STAGES = [[0, 1, 'Theta', 0.0025, 0, 180],
          [0, 2, 'X'    , 0.0020, 0, 100],
          [0, 1, 'dami1', 0.0025, 0, 20],
          [0, 1, 'dami2', 0.0025, 0, 20]]

STAGE_NAME = [r[2] for r in STAGES]
STAGE_UNIT = [r[3] for r in STAGES]
STAGE_SLL  = [r[4] for r in STAGES]
STAGE_SUL  = [r[5] for r in STAGES]

label_pos  = [0] * len(STAGES)
label_name = [0] * len(STAGES)

#####################################

CMDLIST = ['MoveTo',
           'GoToLimitPosition',
           'ChangeHostMode']

def Exection():
    global cmdlist
    stage = combo_ch.get()
    cmd = combo_cmd.get()
    val = entry_cmd.get()
    if stage in STAGE_NAME :
        ch = int(STAGE_NAME.index(stage))
    print(stage, cmd, val)

    if cmd=='ChangeHostMode':
        ChangeHostMode.ChangeHostMode()

    if cmd=='GoToLimitPosition':
        GoToLimitPosition.GoToLimitPosition(ch+1)

    if cmd=='MoveTo':
        if val.isdigit() and float(val)>STAGE_SLL[ch] and float(val)<STAGE_SUL[ch]:
            abs_move.ABS_MOVE(ch+1, float(val), float(STAGE_UNIT[ch]))
        else:
            print('enter correct values!!')
    else:
        # GetPosition(0)
    return

#############################

def GetPosition(temp):
    global label_pos
    rm = visa.ResourceManager()
    usb = rm.open_resource(rm.list_resources()[0])
    return
    for i in range(len(STAGES)):
        pos = where.WHERE(int(STAGES[i][0]), i) * STAGES[i][3]
        label_pos[i].config(text=pos)
    root.after(1000, GetPosition, 0)
    return

######################################
# Set Window and label
root = tkinter.Tk()
root.title("Controller P")
root.geometry("800x200")

label_name_header = tkinter.Label(root, text='axis')
label_name_header.grid(row=0, column=0)
label_pos_header = tkinter.Label(root, text='position')
label_pos_header.grid(row=0, column=1)

for i in range(len(STAGES)):
    label_name[i] = tkinter.Label(root, text=STAGES[i][2])
    label_name[i].grid(row=i+1, column=0)
    label_pos[i] = tkinter.Label(root, text=0)
    label_pos[i].grid(row=i+1, column=1)

GetPosition(0)

###############################
# Set Botton and input box

label_com = tkinter.Label(root, text='Command')
label_com.grid(row=5, column=0)

combo_ch = ttk.Combobox(root, values=STAGE_NAME)
combo_ch.grid(row=5, column=1)

combo_cmd = ttk.Combobox(root, values=CMDLIST)
combo_cmd.grid(row=5, column=2)

entry_cmd = tkinter.Entry(root, textvariable='null')
entry_cmd.grid(row=5, column=3)

button_do = tkinter.Button(text = "exec", command = Exection)
button_do.grid(row=5, column=4)

button_quit = tkinter.Button(text = "Quit", command = root.quit)
button_quit.grid(row=6, column=0)

button_quit = tkinter.Button(text = "EmargencyStop",
                             command = EmargencyStop.EmargencyStop)
button_quit.grid(row=6, column=1)

root.mainloop()
print('Bye!')
