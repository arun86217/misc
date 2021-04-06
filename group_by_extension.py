#importing Modules necessary
import os
import subprocess  #for runnind command
import shutil
import time
#start time of program
start_time =time.time()
# current_working_directory
current_working_directory = os.getcwd()  
print(f"The Current Working direcroty : {current_working_directory}\n")
print("process starting.....\n")

for obj	in os.listdir(current_working_directory):                           #Listing file in directory
	total_path = os.path.join(current_working_directory , obj)              #joining file and path
	if  os.path.isfile(total_path):                                         # checking whether object is file or direcroty
		folder = total_path.split('.')[-1]                                  #splitting for file extension
		new_folder = current_working_directory+'\\'+folder                  # extension folder path
		if not os.path.exists(new_folder):                                  # checking if the extension folder exists
			os.mkdir(new_folder)        
		if "group_by_extension" not in total_path:                          #chceking if the file is the programm running file
			try:
				shutil.move(total_path,new_folder)                          #moving files from cwd to extension folder
			except Exception as e:
				print(e)
                
#end time of program
end_time = time.time()
print(f"The program took {round((end_time-start_time),3)}seconds to finish the process")
			