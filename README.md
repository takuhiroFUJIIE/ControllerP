# How to use ControllerP

1. Connect host computer and SHOT403 with GPIB-USB cable

2. run `python ControllerP.py`

3. set stage, command, value if you need, and do exec

***

# Edit motor

1. Open `ControllerP.py`

2. Set infomation of motor on `STAGES`

   1st column is address of GPIB

   2nd column is channel of GPIB (SHOT304 connector)

   3rd column is display name on this program

   4th column is unit per pulse

   5th column is software lower limit

   6th column is software upper limit

if you connent only 3 channel, delete 4th raw

***

# Edit Command

1. add import file you write

2. import this file for `ControllerP.py`

3. Add displayed command name to `CMDLIST`

4. add new command to `Exection` finction

***

#If you get errors

Please check the import funtion and driver...


# Git memo

…or create a new repository on the command line
```
echo "# ControllerP" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/takuhiroFUJIIE/ControllerP.git
git push -u origin main
```

…or push an existing repository from the command line
```
git remote add origin https://github.com/takuhiroFUJIIE/ControllerP.git
git branch -M main
git push -u origin main
```