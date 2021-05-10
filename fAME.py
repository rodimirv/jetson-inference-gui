
# Author: Rodimir Vilale

# Current Revision: 2.1

# Revision 1	- May 2, 2021	- First draft
# Revision 2	- May 4, 2021	- Added Swapfile
# Revision 2.1	- May 7, 2021	- Added Tkinter install when Tkinter does not exist in the device
#				- Added print colors

import time
from subprocess import call
import getpass

class bcolors:
	WARNING = '\033[93m'
	OKGREEN = '\033[92m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	
# Try to import Tkinter, if Tkinter does not exist in the system the installation of Tkinter will run
while True:
	try:
		from tkinter import *
	except ImportError:
		print(bcolors.WARNING + 'Tkinter is required to run this file, please enter password when prompted to install TKinter')
		time.sleep(2)
		call('sudo apt-get install python3-tk',shell=True)

			
	try:
		root = Tk()
		root.configure(background='white')
		root.title('AME IIoT')
		root.resizable(False, False)
		ico = PhotoImage(file = 'flex_logo.png')
		bnr = PhotoImage(file = 'AME IIoT.png')
		root.iconphoto(True, ico)
		banner = Label(root, image=bnr, bg='white')

		# Gets the requested values of the height and width.
		windowWidth = root.winfo_reqwidth()
		windowHeight = root.winfo_reqheight()
		 
		# Gets both half the screen width/height and window width/height
		positionRight = int(root.winfo_screenwidth()/3 - windowWidth/3)
		positionDown = int(root.winfo_screenheight()/3 - windowHeight/3)
		 
		# Positions the window in the center of the page.
		root.geometry("+{}+{}".format(positionRight, positionDown))
		
		hlColor = 'deep sky blue'
		

		currentUser = getpass.getuser()
		folderEmpty = 'Please enter folder name'
		folderName = ''



		def btnInstallers_click():
			installers = Tk()
			installers.title('INSTALLERS')
			installers.resizable(False, False)
			installers.configure(background='white')

			# Gets the requested values of the height and width.
			windowWidth = installers.winfo_reqwidth()
			windowHeight = installers.winfo_reqheight()
		 
			# Gets both half the screen width/height and window width/height
			positionRight = int(installers.winfo_screenwidth()/2.5 - windowWidth/2.5)
			positionDown = int(installers.winfo_screenheight()/2.5 - windowHeight/2.5)
		 
			# Positions the window in the center of the page.
			installers.geometry("+{}+{}".format(positionRight, positionDown))


			insLabel1 = Label(installers, text='Required to be connected to the internet when running installers' +'\nAlways check for updates before running installers'+'\nInstall in numerical order'+'\nEnter password when prompted', pady=10, bg='white', highlightbackground = hlColor)

			btnInsChkUpd = Button(installers, text="0. Check For Updates", bg='white', highlightbackground = hlColor, command=btnInsChkUpd_click)

			btnInsCMake = Button(installers, text="1. Install CMake", bg='white', highlightbackground = hlColor, command=btnInsCMake_click)

			btnInsVl4 = Button(installers, text="2. Install VL4-Utils", bg='white', highlightbackground = hlColor, command=btnInsVl4_click)

			btnClnGit = Button(installers, text="3. Clone Jetson-Inference Github Repo", bg='white', highlightbackground = hlColor, command=btnClnGit_click)

			btnMkdir = Button(installers, text="4. Create Folder Inside Jetson-Inference called build", bg='white', highlightbackground = hlColor, command=btnMkdir_click)

			btncompileCM = Button(installers, text="5. Compile CMake into build folder", bg='white', highlightbackground = hlColor, command=btncompileCM_click)

			btnBldCpplibs = Button(installers, text="6. Build underlying cpp libraries into build folder", bg='white', highlightbackground = hlColor, command=btnBldCpplibs_click)

			btnInsCpplibs = Button(installers, text="7. Install underlying cpp libraries into the system", bg='white', highlightbackground = hlColor, command=btnBldCpplibs_click)

			btnClnConf = Button(installers, text="8. Clean Configurations", bg='white', highlightbackground = hlColor, command=btnClnConf_click)

			btnInsSwapFileDef = Button(installers, text="9. Install Swapfile -Default", bg='white', highlightbackground = hlColor, command=btnInsSwapFileDef_click)

			swapFileLabel = Label(installers, text="The default Swapfile size is 6GB \nTo increase Swapfile use terminal and enter: \nbash installSwapfile.sh -s Size", bg='white', highlightbackground = hlColor)


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
			btnInsSwapFileDef.grid(row=10, column=0, columnspan=8)
			swapFileLabel.grid(row=11, column=0, columnspan=8)


		# Installer Controls
		def btnInsChkUpd_click():
			call('sudo apt-get update',shell=True)

		def btnInsCMake_click():
			call('sudo apt-get install git cmake libpython3-dev python3-numpy',shell=True)

		def btnInsVl4_click():
			call('sudo apt-get install v4l-utils',shell=True)

		def btnClnGit_click():
			call('git clone --recursive https://github.com/dusty-nv/jetson-inference temp',shell=True)
			call('mv temp ~/jetson-inference' , shell=True)
			call('rm -rf temp', shell=True)

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

		def btnInsSwapFileDef_click():
			call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/gui-inference/installSwapfile', '--', 'bash', 'installSwapfile.sh'])

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
				trainLabel.grid(row=10, column=0, columnspan=8)

		def btnExport_click():
			global foldername
			folderName = trInput1.get()
			if (folderName != ''):
				call(['gnome-terminal', '--working-directory=/home/' +currentUser+ '/jetson-inference/python/training/detection/ssd', '--command=python3 onnx_export.py --model-dir=models/' +folderName])
			else:
				exportLabel.grid(row=12, column=0, columnspan=8)

		# Buttons, Entry, and Labels

		installersLabel = Label(root, text='If running for the first time, Install necessary tools and apps in the "Installers" window', bg='white')

		btnInstallers = Button(root, text="Installers", command=btnInstallers_click, padx=58, bg='white', highlightbackground = hlColor)

		cameraCaptureLabel = Label(root, text='Enter device directory | e.g. /dev/video0' + '\nUse the "Show List of Cameras Detected" button if unknown', bg='white')

		camDirInputLabel = Label(root, text='Camera Directory:   /dev/', bg='white')

		camDirInput = Entry(root, width=9, bg='white', highlightbackground = hlColor)

		btnCap = Button(root, text="Capture Camera", command=btnCap_click, padx=35, bg='white', highlightbackground = hlColor)

		btnShowCamLst = Button(root, text="Show List of Cameras Detected", command=btnShowCamLst_click, bg='white', highlightbackground = hlColor)

		trLabel1 = Label(root, text='Set the following requirements then click on the "Train Annotated Models" button to start training custom model', pady=10, bg='white')
		trInputLabel1 = Label(root, text='Folder Name:', bg='white')
		trInputLabel2 = Label(root, text='Batch Size:', bg='white')
		trInputLabel3 = Label(root, text='Workers:', bg='white')
		trInputLabel4 = Label(root, text='Epoch:', bg='white')

		trInput1 = Entry(root, width=10, bg='white', highlightbackground = hlColor)
		trInput2 = Entry(root, width=10, bg='white', highlightbackground = hlColor)
		trInput3 = Entry(root, width=10, bg='white', highlightbackground = hlColor)
		trInput4 = Entry(root, width=10, bg='white', highlightbackground = hlColor)

		trInput2.insert(0, '2')
		trInput3.insert(0, '1')
		trInput4.insert(0, '1')

		btnTrain = Button(root, text="Train Annotated Models", command=btnTrain_click, bg='white', highlightbackground = hlColor)


		trainLabel = Label(root, text=folderEmpty, fg="red", bg='white')

		btnExport = Button(root, text="Export Trained Models to ONNX", command=btnExport_click, bg='white', highlightbackground = hlColor)

		exportLabel = Label(root, text=folderEmpty, fg="red", bg='white')

		# Show Labels,Entry, and Buttons
		banner.grid(row=1, column=0, columnspan=8)
		installersLabel.grid(row=2, column=0, columnspan=8)
		btnInstallers.grid(row=3, column=0, columnspan=8)
		cameraCaptureLabel.grid(row=4, column=0, columnspan=8)
		camDirInputLabel.grid(row=5, column=0, columnspan=2)
		camDirInput.grid(row=5, column=0, columnspan=5)
		btnCap.grid(row=5, column=0, columnspan=8)
		btnShowCamLst.grid(row=5, column=5, columnspan=8)
		trLabel1.grid(row=6, column=0, columnspan=8)
		trInputLabel1.grid(row=8, column=0)
		trInputLabel2.grid(row=8, column=2)
		trInputLabel3.grid(row=8, column=4)
		trInputLabel4.grid(row=8, column=6)
		trInput1.grid(row=8, column=1)
		trInput2.grid(row=8, column=3)
		trInput3.grid(row=8, column=5)
		trInput4.grid(row=8, column=7)
		btnTrain.grid(row=9, column=0, columnspan=8)
		btnExport.grid(row=11, column=0, columnspan=8)


		root.mainloop()
	except Exception as err:
		print(err)
		#continue
	break
