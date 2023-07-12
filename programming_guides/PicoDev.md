# **Setting up your Pico Development Environment**

The first step is to open up your terminal. This can be done by searching for it by pressing the windows key and typing in the search bar or pressing `CTRL+ALT+t`

Within your terminal type the following commands:
```bash
sudo apt update

sudo apt install -y build-essential

sudo apt install git

sudo apt install screen minicom

sudo apt install cmake gcc-arm-none-eabi libnewlib-arm-none-eabi build-essential libstdc++-arm-none-eabi-newlib
```
For MACOS:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install cmake

brew tap ArMbed/homebrew-formulae

brew install arm-none-eabi-gcc

git clone -b master --recurse-submodules https://github.com/raspberrypi/pico-sdk.git
```
Now look for a file called ~/.zprofile, ~/.bash-profile (Ask for help with this one)
In that file add the following command by using a text editor:

```bash
open -t ~/.zprofile

export PICO_SDK_PATH ="$/home/pico-sdk"
```

Then in a terminal get to your home directory and type:

```bash
source ~/.zprofile (Ask for help here)
```

Now clone the Pico SDK and setup your environment variables

```bash
sudo git clone https://github.com/raspberrypi/pico-sdk.git /opt/pico-sdk
```
You may need to take ownership of the directory the repository was cloned into (you can check this by seeing if you have permission to make a directory). Make sure you are inside the pico-sdk directory and run: (you can replace the '.' with an absolue or relative path to pico-sdk)

```bash
sudo chown -R <your-username> .
```

Be sure to run these! They provide the pico-sdk with other repositories it depends on
```bash
sudo git -C /opt/pico-sdk/ submodule update --init

echo 'export PICO_SDK_PATH=/opt/pico-sdk' | sudo tee -a /etc/profile.d/pico-sdk.sh

source /etc/profile.d/pico-sdk.sh
```

Lastly, clone the repo:

```bash
sudo git clone https://github.com/robotics-crash-course/rcc-pico.git

cd rcc-pico

sudo chown -R <your-username> .

git submodule update --init --recursive
```

Your repo should be ready to go!

To check if CMake and Make are working, go to `rcc-pico/dev/pico` and create the build directory by typing:
```bash
mkdir build && cd build
cmake ..
```
If this runs without errors, CMake is working properly.

After that, try typing:
```bash
make -j12
```

If that works, you've now compiled a few C++ programs which you can upload to the Pico!