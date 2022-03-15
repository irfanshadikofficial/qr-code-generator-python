#Module to create QRCode
#Need to install first from the terminal
import pyqrcode
#To Export QRCode As Png
import png
#Import QRCode From pyqrcode Module
from pyqrcode import QRCode
#Get Link As User Input
s = input("Enter The Link :")
#To Get Unique File Name For Genareted QRCode
filename = input("File Name :")
#To Know Which Type of Extension The Used Want
fileext = input("File Extension (png/svg/esp) :")
#To Create QRCode From URL
url = pyqrcode.create(s)
#To Determine Which Type Of File To Create ( PNG/SVG/ESP )
if fileext == "svg" or filename == "SVG" or filename == "Svg":
    url.svg(f"{filename}.svg", scale = 8)
elif fileext == "eps" or filename == "EPS" or filename == "Eps":
    url.eps(f"{filename}.eps", scale = 2)
elif fileext == "png" or filename == "PNG" or filename == "Png":
    url.png(f"{filename}.png", scale = 6)
#If Somehow Programm Miss To Know Which Type Of File To Create
else:
    url.png(f"{filename}.png", scale = 6)
#Ending Message To Tell User That Its Done
print("Finished (❁´◡`❁) | Check Your Directory")
#This Files Created & Explained By -𝕴𝖗𝖋𝖆𝖓 𝕾𝖍𝖆𝖉𝖎𝖐-