
# Author: Rodimir Vilale
# Revision 1
# May 3, 2021

from tkinter import *
from subprocess import call
import getpass

root = Tk()
root.title('FLEX AME')
root.resizable(False, False)

# Gets the requested values of the height and width.
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
 
# Gets both half the screen width/height and window width/height
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
 
# Positions the window in the center of the page.
root.geometry("+{}+{}".format(positionRight, positionDown))

currentUser = getpass.getuser()
folderEmpty = 'Please enter folder name'
folderName = ''

def btnInstallers_click():
	installers = Tk()
	installers.title('INSTALLERS')
	installers.resizable(False, False)
	
	# Gets the requested values of the height and width.
	windowWidth = installers.winfo_reqwidth()
	windowHeight = installers.winfo_reqheight()
 
	# Gets both half the screen width/height and window width/height
	positionRight = int(installers.winfo_screenwidth()/2 - windowWidth/2)
	positionDown = int(installers.winfo_screenheight()/2 - windowHeight/2)
 
	# Positions the window in the center of the page.
	installers.geometry("+{}+{}".format(positionRight, positionDown))


	insLabel1 = Label(installers, text='Required to be connected to the internet when running installers' +'\nAlways check for updates before running installers'+'\nInstall in numerical order'+'\nEnter password when prompted', pady=10)

	btnInsChkUpd = Button(installers, text="0. Check For Updates", command=btnInsChkUpd_click)

	btnInsCMake = Button(installers, text="1. Install CMake", command=btnInsCMake_click)

	btnInsVl4 = Button(installers, text="2. Install VL4-Utils", command=btnInsVl4_click)

	btnClnGit = Button(installers, text="3. Clone Jetson-Inference Github Repo", command=btnClnGit_click)

	btnMkdir = Button(installers, text="4. Create Folder Inside Jetson-Inference called build", command=btnMkdir_click)

	btncompileCM = Button(installers, text="5. Compile CMake into build folder", command=btncompileCM_click)

	btnBldCpplibs = Button(installers, text="6. Build underlying cpp libraries into build folder", command=btnBldCpplibs_click)

	btnInsCpplibs = Button(installers, text="7. Install underlying cpp libraries into the system", command=btnBldCpplibs_click)

	btnClnConf = Button(installers, text="8. Clean Configurations", command=btnClnConf_click)

	# Show Labels,Entry, and Buttons
	insLabel1.grid(row=1, column=0, columnspan=8)
	btnInsChkUpd.grid(row=2, column=0, columnspan=8)
	btnInsCMake.grid(row=3, column=0, columnspan=8)
	btnInsVl4.grid(row=4, column=0, columnspan=8)
	btnClnGit.grid(row=5, column=0, columnspan=8)
	btnMkdir.grid(row=6, column=0, columnspan=8)
	btncompileCM.grid(row=7, column=0, columnspan=8)
	btnBldCpplibs.grid(row=8, column=0, columnspan=8)
	btnClnConf.grid(row=9, column=0, columnspan=8)

# Installer Controls
def btnInsChkUpd_click():
	call('sudo apt-get update',shell=True)

def btnInsCMake_click():
	call('sudo apt-get install git cmake libpython3-dev python3-numpy',shell=True)

def btnInsVl4_click():
	call('sudo apt-get install v4l-utils',shell=True)

def btnClnGit_click():
	call('git clone --recursive https://github.com/dusty-nv/jetson-inference',shell=True)

def btnMkdir_click():
	call('mkdir /home/' +currentUser+ '/jetson-inference/build',shell=True)

def btncompileCM_click():
	call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/build', '--', 'cmake', '../'])

def btnBldCpplibs_click():
	call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/build', '--', 'make'])

def btnInsCpplibs_click():
	call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/build', '--', 'sudo', 'make install'])

def btnClnConf_click():
	call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/build', '--', 'sudo', 'ldconfig'])

# Root Controls
def btnCap_click():
	cameraDir = camDirInput.get()
	call(['gnome-terminal', '--', 'camera-capture', '/dev/' +cameraDir])

def btnShowCamLst_click():
	call('v4l2-ctl --list-devices',shell=True)

def btnTrain_click():
	global folderName
	folderName = trInput1.get()
	batchSize = trInput2.get()
	workers = trInput3.get()
	epoch = trInput4.get()
	if (folderName != ''):
		call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/python/training/detection/ssd', '--command=python3 train_ssd.py --dataset-type=voc --data=data/' +folderName+ ' --model-dir=models/' +folderName+ ' --batch-size=' +batchSize+ ' --workers=' +workers+ ' --epoch=' +epoch])
	else:
		trainLabel.grid(row=9, column=0, columnspan=8)

def btnExport_click():
	global foldername
	folderName = trInput1.get()
	if (folderName != ''):
		call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/python/training/detection/ssd', '--command=python3 onnx_export.py --model-dir=models/' +folderName])
	else:
		exportLabel.grid(row=11, column=0, columnspan=8)

# Buttons, Entry, and Labels

installersLabel = Label(root, text='If running for the first time, Install necessary tools and apps in the "Installers" window')

btnInstallers = Button(root, text="Installers", command=btnInstallers_click, padx=58)

cameraCaptureLabel = Label(root, text='Enter device directory | e.g. /dev/video0' + '\nUse the "Show List of Cameras Detected" button if unknown')

camDirInputLabel = Label(root, text='Camera Directory:   /dev/')

camDirInput = Entry(root, width=9)

btnCap = Button(root, text="Capture Camera", command=btnCap_click, padx=35)

btnShowCamLst = Button(root, text="Show List of Cameras Detected", command=btnShowCamLst_click)

trLabel1 = Label(root, text='Set the following requirements then click on the "Train Annotated Models" button to start training custom model', pady=10)
trInputLabel1 = Label(root, text='Folder Name:')
trInputLabel2 = Label(root, text='Batch Size:')
trInputLabel3 = Label(root, text='Workers:')
trInputLabel4 = Label(root, text='Epoch:')

trInput1 = Entry(root, width=10)
trInput2 = Entry(root, width=10)
trInput3 = Entry(root, width=10)
trInput4 = Entry(root, width=10)

trInput2.insert(0, '2')
trInput3.insert(0, '1')
trInput4.insert(0, '1')

btnTrain = Button(root, text="Train Annotated Models", command=btnTrain_click)

trainLabel = Label(root, text=folderEmpty, fg="red")

btnExport = Button(root, text="Export Trained Models to ONNX", command=btnExport_click)

exportLabel = Label(root, text=folderEmpty, fg="red")

# Show Labels,Entry, and Buttons
installersLabel.grid(row=1, column=0, columnspan=8)
btnInstallers.grid(row=2, column=0, columnspan=8)
cameraCaptureLabel.grid(row=3, column=0, columnspan=8)
camDirInputLabel.grid(row=4, column=0, columnspan=2)
camDirInput.grid(row=4, column=0, columnspan=5)
btnCap.grid(row=4, column=0, columnspan=8)
btnShowCamLst.grid(row=4, column=5, columnspan=8)
trLabel1.grid(row=5, column=0, columnspan=8)
trInputLabel1.grid(row=7, column=0)
trInputLabel2.grid(row=7, column=2)
trInputLabel3.grid(row=7, column=4)
trInputLabel4.grid(row=7, column=6)
trInput1.grid(row=7, column=1)
trInput2.grid(row=7, column=3)
trInput3.grid(row=7, column=5)
trInput4.grid(row=7, column=7)
btnTrain.grid(row=8, column=0, columnspan=8)
btnExport.grid(row=10, column=0, columnspan=8)


root.mainloop()
