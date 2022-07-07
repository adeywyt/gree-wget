import wget
import time
import tkinter.messagebox
import os
import sys 
import tempfile
time.sleep(1)
print("The program is starting, please wait.....")
time.sleep(2)
print("Loading Progress:"+"=====25%")
time.sleep(3)
print("Loading Progress:"+"==========50%")
time.sleep(3)
print("Loading Progress:"+"===============75%")
time.sleep(3)
print("Loading Progress:"+"====================100%")
time.sleep(3)
print("Loading completed")
i=os.system("cls")
l=os.system("color 9")
print(".........................................................................")
print(".  ________                                __      __              __   .")
print(". /  _____/______   ____   ____           /  \    /  \____   _____/  |_ .")
print("./   \  __\_  __ \_/ __ \_/ __ \   ______ \   \/\/   / ___\_/ __ \   __\.")
print(".\    \_\  \  | \/\  ___/\  ___/  /_____/  \        / /_/  >  ___/|  |  .")
print(". \______  /__|    \___  >\___  >           \__/\  /\___  / \___  >__|  .")
print(".        \/            \/     \/                 \//_____/      \/      .")
print(".                         Gree-Wget version 3.0                         .")
print(".........................................................................")
print(".Welcome to Gree-Wget                                                   .") 
print(".Gree-Wget official website: https://adeylinux.xyz/                     .")
print(".Gree-Wget is developed using python. It mainly uses wget, time, os     .")            
print(".Gree-Wget is an open source downloader that supports multitasking      .")
print(".........................................................................")
#tkinter.messagebox.showerror("Gree-Wget提醒：","Gree-Wget属于开源软件可以免费使用.")
#tkinter.messagebox.showinfo("Gree-Wget","Gree-Wget is an open source program. It is free to use.")
try:
  j=int(input("Please enter the number of files to download："))
  if j == 0:
   print("The number of file downloads cannot be equal to 0")
  url=[]
  while len(url) < j :
   nlinux=input("Please enter the added download link:")
   url.append(nlinux) 
  for i in url:
     file_name = wget.filename_from_url(i)
     macc=input("Please enter the rename name <name,linux,box>:")
     lnmap=input("Please enter the file extension (.exe, .jpg, .png):")
     file_name = wget.download(i,out=macc+"."+lnmap)
     print("")
     print("file name:",macc+"."+lnmap)
     print("")
  os.path.dirname(__file__) 
  namep=os.path.abspath(('./'))
  print("File download path:",namep)
  print("")
  sgree=input("Please enter any key to exit the program.............")
except:
     print("Program error -- please enter the correct download link")