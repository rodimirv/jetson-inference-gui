# Author: Rodimir Vilale

# Current Revision: 2.1

# Revision 1	- May 2, 2021	- First draft
# Revision 2	- May 4, 2021	- Added Swapfile
# Revision 2.1	- May 7, 2021	- Added Tkinter install when Tkinter does not exist in the device
#				                      - Added print colors

This application is specifically made for NVIDIA-Jetson devices as supplemental to the HELLO AI WORLD tutorial made by dusty-nv for object detection.

https://github.com/dusty-nv/jetson-inference

This GUI is made using Tkinter - Install Tkinter on your system first before use.

Once cloned to your system, you can change the name of the Python file fAME.py to your liking and also change the title of the Tkinter window root.title('FLEX AME')

installSwapfile by JetsonHacks is also included in the application and in this repo. To use install:

cd gui-inference/installSwapfile

bash installSwapfile.sh

To customize install as per JetsonHacks documentation: 

bash installSwapFile.sh [[[-d directory ] [-s size] -a] | [-h]]

-d | --dir [directoryname] Directory to place swapfile (defaults to /mnt)

-s | --size [gigabytes] (defaults to 6 )

-a | --auto Enable swap on boot in /etc/fstab (default: "Y")

-h | --help This message

Defaults to creating a 6GB Swapfile in the current directory

Note: If you enable swap on boot, you should also automount the drive that you're using

Automount
Automount a device given the label

autoMount.sh - Automount a device, useful for external media like USB drives

bash autoMount.sh [ [-l label] | [-h]]

-l | --label [labelname] Label to lookup

-h | --help This message

Example usage:

$ ./shellScript.sh -l RaceUSB

where RaceUSB is the label of the device mounted at /media/jetsonhacks/RaceUSB

Tool to help automount the device given from the label The script looks up the device, mounting point and UUID for the given label Optionally add it to /etc/fstab
