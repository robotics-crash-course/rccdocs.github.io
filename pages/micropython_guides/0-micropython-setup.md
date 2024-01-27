# **Setting up Micropython Development Environment**
## **Overview**
To communicate and write code in MicroPython for the PicoW microcontroller, we will use the MicroPico extension in VS Code. 

Available on [Ubuntu](#ubuntu), [MacOS](#macos), and [Windows](#windows). 

## Ubuntu

### **Clone micropython Repository**
Within your terminal type the following commands:
```
sudo apt-get install git

cd <into where you want to store the repository>

git clone https://github.com/robotics-crash-course/micropython.git

cd micropython
```

### **Download VS Code**

Install VS Code Here: https://code.visualstudio.com/download

Go back to the terminal where you are within the micropython directory, open VS code at this folder with the following command:
```
code .
```
Use `CTRL+Shift+E` to open file explorer on left. To open a terminal, at the top selection bar, under `Terminal`, choose `New Terminal`. 

### **Add USB Permissions** 
```
sudo usermod -a -G dialout $USER
```
### VERY IMPORTANT: RESTART YOUR COMPUTER AFTER THIS STEP !!

### Install MicroPico Extension in VSCode
After restarting your computer, reopen VS Code using the terminal:
```
cd <directory where you cloned micropython repo>

cd micropython

code .
```

Use `CTRL+Shift+X` to open extensions manager

Install `MicroPico` and reccomended additional extensions

### Upload MicroPython to Pico
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

### Configure MicroPico Project
Use `CTRL+Shift+P` to show commands, search for `micropico: configure project`, click to setup the project. 

On the file explorer, click `main.py` to open the python file. At the bottom bar of VS Code, should see that the pico is connected and there should be an option to `Run`. Run main.py to activate the REPL in VS Code. 

## MacOS
### **Clone micropython Repository**

Install git, type this command and follow prompts if not already installed:

```
git --version 
```

Clone repository: 
```
cd <into where you want to store the repository>

git clone https://github.com/robotics-crash-course/micropython.git

cd micropython
```

### **Download VS Code**

Install VS Code Here: https://code.visualstudio.com/download

Add code command to path ([reference](https://code.visualstudio.com/docs/setup/mac)):

1. Launch VS Code
2. Open Command Palette `Cmd+Shift+P`, and type 'shell command' to find 'Shell Command: Install 'code' command in PATH' command. 
3. Go back to terminal where you are within the micropython directory
4. Type the following command to open VS Code:
```
code .
```

Use `Cmd+Shift+E` to open file explorer on left. To open a terminal, use `CTRL+Shift+~`, or use Terminal tab at top of screen.  

### Install MicroPico Extension in VSCode

Use `Cmd+Shift+X` to open extensions manager

Install `MicroPico` and reccomended additional extensions

### Upload MicroPython to Pico
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

```
cp flash_nuke.uf2 /Volumes/RPI-RP2
```
After the flash is nuked, the pico should reappear as a flash drive device, now you can upload micropython. 
```
cp RPI_PICO_W-20231005-v1.21.1.uf2 /Volumes/RPI-RP2
```

### Configure MicroPico Project
Use `Cmd+Shift+P` to show commands, search for `micropico: configure project`, click to setup the project. 

On the file explorer, click `main.py` to open the python file. At the bottom bar of VS Code, should see that the pico is connected and there should be an option to `Run`. Run main.py to activate the REPL in VS Code. 


## Windows
### **Clone micropython Repository**

[Install git from here](https://git-scm.com/download/win)

Clone repository: 
```
cd <into where you want to store the repository>

git clone https://github.com/robotics-crash-course/micropython.git

cd micropython
```

### **Download VS Code**

Install VS Code Here: https://code.visualstudio.com/download

In the terminal (or command prompt), open VS Code from within the micropython directory with the following command:
```
code .
```

### Install MicroPico Extension in VSCode

Open extensions manager, install `MicroPico` and reccomended additional extensions

### Upload MicroPython to Pico
To upload files to the pico, need to put it into BOOT MODE. The three steps are: 
1. Plug in Pico to Computer
2. HOLD BOOT button on pico (teeny white button)
3. (While holding boot button) PRESS RESET Button on the Raft 

Pico should then show up as a flashdrive device on the computer. 

To check the name of the connective device (where the pico mounts within windows) use the file explorer. Commonly, will show up at the letter `E`, but could be any letter. 

Within the VS Code Terminal:
```
cd filestoupload
```
should see two files, flash_nuke.uf2 and RPI_PICO~~~.uf2, first we're going to upload the flash nuke file to prepare the pico for micropython. 

<strong>This is assuming the pico is showing up as `E`</strong>

```
cp flash_nuke.uf2 E:\
```
After the flash is nuked, the pico should reappear as a flash drive device, now you can upload micropython. 
```
cp RPI_PICO_W-20231005-v1.21.1.uf2 E:\
```

### Configure MicroPico Project
Use `CTRL+Shift+P` to show commands, search for `micropico: configure project`, click to setup the project. 

On the file explorer, click `main.py` to open the python file. At the bottom bar of VS Code, should see that the pico is connected and there should be an option to `Run`. Run main.py to activate the REPL in VS Code. 