import os

folder_path = r'F:\movies'

# to change default tamil movie format to only movie name 

for file in os.listdir(folder_path):
    if 'www' in file:                                          # to check for www 
        original_name = file
        name= file.split('-')
        ext = 'mp4'
        if 'mkv' in name[-1]:
            ext = 'mkv'
        to_keep = str(name[1]).split('(')                      # trimming till (year)
        new_name = str(to_keep[0]).strip()                     # movie name 
        original_path =folder_path+"\\" +original_name         #original path and name of the file
        new_path = folder_path+"\\"+new_name+'.'+ext           #new path with new name and extension
        os.rename(original_path,new_path)                      #renaming