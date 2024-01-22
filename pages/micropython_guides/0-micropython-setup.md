# **Setting up Micropython Development Environment**
## **Overview**
To communicate and write code in MicroPython for the PicoW microcontroller, we will use the MicroPico extension in VS Code running in **Ubuntu**. 

## **Clone micropython Repository**
Within your terminal type the following commands:
```
sudo apt update

sudo apt install git

cd <into where you want to store the repository>

git clone https://github.com/robotics-crash-course/micropython.git

cd micropython
```

## **Download VS Code**

Install VS Code Here: https://code.visualstudio.com/download

Go back to the terminal where you are within the micropython directory, open VS code at this folder with the following command:
```
code .
```
Use `CTRL+Shift+E` to open file explorer on left. To open a terminal, at the top selection bar, under `Terminal`, choose `New Terminal`. 

## **Run Permissions Script to allow USB communication** 

Within the terminal in VS Code, run the solve permissions script:
```
./solvePermissions.sh
```

If after this step the pico does not connect when the project is configured (later step), can try running this command instead:
```
sudo usermod -a -G dialout <username>
```
#### VERY IMPORTANT: RESTART YOUR COMPUTER AFTER THIS STEP !!

## Install MicroPico Extension in VSCode
After restarting your computer, reopen VS Code using the terminal:
```
cd <directory where you cloned micropython repo>

cd micropython

code .
```

Use `CTRL+Shift+X` to open extensions manager

Install `MicroPico` and reccomended additional extensions

## Upload MicroPython to Pico
To upload files to the pico, need to put it into BOOT MODE. The three steps are: 
1. Plug in Pico to Computer
2. HOLD BOOT button on pico (teeny white button)
3. (While holding boot button) PRESS RESET Button on the Raft 

Pico should then show up as a flashdrive device on the computer

Within the VS Code Terminal:
```
cd filestoupload

ls
```
should see two files, flash_nuke.uf2 and RPI_PICO~~~.uf2, first we're going to upload the flash nuke file to prepare the pico for micropython. 

Use your computer's username! 
```
cp flash_nuke.uf2 /media/<username>/RPI_RP2
```
After the flash is nuked, the pico should reappear as a flash drive device, now you can upload micropython. 
```
cp RPI_PICO_W-20231005-v1.21.1.uf2 /media/<username>/RPI-RP2 
```

## Configure MicroPico Project
Use `CTRL+Shift+P` to show commands, search for `micropico: configure project`, click to setup the project. 

On the file explorer, click `main.py` to open the python file. At the bottom bar of VS Code, should see that the pico is connected and there should be an option to `Run`. Run main.py to activate the REPL in VS Code. 