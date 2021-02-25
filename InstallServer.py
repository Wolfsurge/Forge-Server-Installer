import subprocess
import wget
import shutil
import os


ForgeServer = "https://www.dropbox.com/s/wfjjrjec71dvt2b/forge-1.16.5-36.0.43.jar?dl=1"
MinecraftServer = "https://www.dropbox.com/s/wfz75rciveop1if/minecraft_server.1.16.5.jar?dl=1"
json = "https://www.dropbox.com/s/m6plrdpg88wena8/1.16.5.json?dl=1"
bat = "https://www.dropbox.com/s/555apbb243hogss/StartServer.bat?dl=1"
Libraries = "https://www.dropbox.com/sh/dhdkslkkua7swo0/AAA9d3BZDtSDW75H96i7RaQZa?dl=1"
   


print("Downloading the Forge Server jar...")
wget.download(ForgeServer)
print("Downloaded the Forge Server jar...")
print("Downloading official Minecraft Server jar...")
wget.download(MinecraftServer)
print("Downloaded official Minecraft Server jar...")
print("Downloading libraries...")
wget.download(Libraries)
print("Downloaded Libraries...")
print("Downloading StartServer.bat...")
wget.download(bat)
print("Downloaded StartServer.bat...")
print("Downloading 1.16.5.json...")
wget.download(json)
print("Downloaded 1.16.5.json...")
print("Downloaded all files!")
print("Unzipping libraries...")
shutil.unpack_archive('libraries.zip', 'libraries')
print("Unzipped libraries...")
print("Deleting excess files...")
os.remove("libraries.zip")
print("Deleted excess files...")
print("Thank you for using Wolfsurge's Forge Server installer!")
print("Consider subscribing to Wolfsurge on YouTube!")
ex1t = input(">>> ")


    
    
    
    
    

