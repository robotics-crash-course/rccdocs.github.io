# **Building, Uploading and Monitoring the Pico**
## **Building**
To upload code to the Pico you must build it using CMake and Make.

### **CMake and Make**
CMake gathers libraries and file contignencies that your C/C++ program needs to be able to operate. It links all of these files together and passes them off to Make, which compiles them in the form of a `.uf2` file.

To build a program you must first add the program to your CMakeLists.txt file which is located in the `rcc-pico/dev/pico` direcotry.

At the bottom of the file you will use the macro called `make_exec(arg1 arg2)` and enter your specific arguments

`arg1` should be the name you want your `.uf2` file to be.

`arg2` should be the location of your file relative to `rcc-pico/dev/pico`.

Now, you need to create a build directory where you will run the CMake command (the build directory should be in `rcc-pico/dev/pico/build`). Type the following:
```bash
mkdir build && cd build
cmake ..
```
Next, run:
```bash
make -j4
```
There we go, you should now have .uf2 files for each of the `make_exec` files you specified in your `CMakeLists.txt` file!


---

The Raspberry Pi Pico W has three modes
+ RUN
    + Microcontroller is running the code copied to it.
+ BOOT
    + Microcontroller is accepting code from the user.
+ OFF
    + Microcontroller is off.

---
## **Uploading**
The process of uploading code to the Pico is as follows. It starts off in the OFF State, transitions to BOOT and then to RUN.

To put the pico into BOOT mode hold down the white button near the USB port on the Pico. Keep it pressed while you insert the USB cable into the Pico (assuming it's already plugged into your laptop). Once it's plugged in, release the boot button and the Pico should be ready to accept `.uf2` files (the files that contain your programs).


### **Steps for a VM**
---
In a VM there are extra steps needed to recognize the BOOT and RUN modes of the Pico.
+ Open up the settings of your VM and go to the USB section.
+ Plug the Pico in without pressing any buttons and hit the green USB button to the right of the settings menu. You should see **RPI-RP2**, click on it to add the device.
+ Now remove the Pico from the USB and replug it in BOOT mode. Repeat the steps for adding it as a device.
---

First off, we must check to see if the Pico has been recognized as a boot device. To do so, type in:
```
sudo blkid -o list | grep RPI-RP2
```
If an output along these lines appears, your pico is being recognized.
```
/dev/sdb1   vfat    RPI-RP2    /media/user/RPI-RP2  0000-0000
```
At this point a **two things can happen**.

+ Everything goes smoothly and the Pico "mounts" to `/media/user/RPI-RP2`
    +  Enter the **build** directory which sould contain the made .uf2 files.
    + Type the following command
```
cp my_file.uf2 /media/user/RPI-RP2
```
That's it, you've now uploaded the program to the Pico and it'll automatically enter the run state.

**OR**
+ It doesn't mount to that location and you must create it yourself.
    + The first time this error occurs, you must create the mounting point. Do so by typing the following command.
```
sudo mkdir /mnt/pico
```

The above command is only done the first time you encounter this issue, from then out the mounting point has already been created and you only need to perform the instructions below.

+ Now that you've created the mounting point, you need to associate the pico's device that you found from the **blkid** command to this mounting point. Type:

```
sudo mount /dev/sd__ /mnt/pico
```

+ You're now ready to copy over the file to the pico. Type the following commands:

```
sudo cp my_file.uf2 /mnt/pico
sudo sync
```

Hopefully this won't happen too often, but you've now uploaded the program to the Pico and it'll automatically enter the run state.

---

### **Steps for WSL**
---
Uploading to WSL is as follows:

+ Build the code within WSL (generate the `.uf2` you want to upload).
+ Put the Pico into boot mode. 
+ Drag and drop `.uf2` into the Pico (it will pop us as a USB device on Windows).

To find the `.uf2` file, within your file explorer copy and paste the following: `\\wsl.localhost\Ubuntu` into the top tab and you can navigate through the Ubuntu file structure within Windows.
 
It will generally look like this: `Linux > Ubuntu > home > user > rcc-pico > dev > pico > build `.

Add the folder to quick access in your file explorer to find it easier in the future.
### **Steps for MAC OS**
---
Simply type:
```bash
cp [file-name.uf2] Volumes/RPI-RP2
```
## **Monitoring Output VM + MACOS**
To monitor the output, we'll be using tio.

Whenever the pico is in the **run** mode, it'll be identifiable as a USB device called `ttyACM0`. To find this device type:

```
ls /dev/tty* | grep ACM0
```

If `ttyACM0` is present, you can type the following command to read the serial output from the Pico.

```
tio /dev/ttyACM0
```

To exit screen you could do three things:
+ Remove the USB cable from the Pico
+ Press the reset button on the Pico
+ Press `CTRL+t`, then `q`


## **Monitoring Output WSL**
To monitor the serial output of the Pico using WSL you need to download USBIPD.

It can be found here: https://github.com/dorssel/usbipd-win/releases

Then within `Ubuntu`, install the USBIPD tools and hardware database.

```bash
sudo apt install linux-tools-generic hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/*-generic/usbip 20
```
When the Pico is in run mode, it will appear as a USB bus on Windows and we need to attach that to Ubuntu.

Within `PowerShell` type:
```PowerShell
usbipd wsl list
```

The Pico should show up as a `USB Serial Communication Device`. You need to attach that device, it should have a bus ID associated with it, to WSL.

```PowerShell
usbipd wsl attach --busid <busid>
```

Within `Ubuntu` type:
```bash
lsusb
```
To see if the device was attached. If it was attached, you can use tio as instructed above.

**Note: You need to do this each time you reattach your Pico in run mode to see the output!**

Source: https://learn.microsoft.com/en-us/windows/wsl/connect-usb#install-the-usbip-tools-and-hardware-database-in-linux