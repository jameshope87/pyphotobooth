#!/user/bin/python

#for a fresh install
#sudo apt-get install python-picamera
#sudo apt-get install python-imaging
#sudo apt-get install python-pip
#sudo apt-get install imagemagick


#pip install facepy


#import modules
import picamera
import time
from time import sleep
from facepy import GraphAPI
import RPi.GPIO as GPIO
from PIL import Image
import subprocess
import os, sys
import shutil

#change working directory to script path
defaultdir = os.getcwd()
path = sys.path[0]
os.chdir(path)

#setup GPIO pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(23 ,GPIO.IN)

#setup variables
#HDMPi
#screenresH = 1280
#screenresV = 800
#1080p
screenresH = 1280
screenresV = 768

#picture resolution
pictureresH = 1280
pictureresV = 800

#setup camera
camera = picamera.PiCamera()
camera.hflip = True
camera.vflip = False

#start preview screen
camera.start_preview()
print camera.preview.window
#Load images   ####################################################
img = Image.open('go.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

go = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
go.window = (screenresH-img.size[0],screenresV-img.size[1],img.size[0],img.size[1])
go.alpha = 128
#go.layer = 3

#Load images   ####################################################
img = Image.open('take4.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

take4 = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
take4.window = (0,screenresV-img.size[1],img.size[0],img.size[1])
take4.alpha = 128
#take4.layer = 3

#Load images   ####################################################
img = Image.open('ready.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

ready = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
ready.window = (0,0,img.size[0],img.size[1])
ready.alpha = 128
#ready.layer = 3

#Load images   ####################################################
img = Image.open('set.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

setimg = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
setimg.window = ((screenresH-img.size[0])/2,(screenresV-img.size[1])/2,img.size[0],img.size[1])
setimg.alpha = 128
#setimg.layer = 3

#Load images   ####################################################
img = Image.open('startscreen.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

startscreen = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
startscreen.window = ((screenresH-img.size[0])/2,0,img.size[0],img.size[1])
startscreen.alpha = 128
startscreen.layer = 3

#Load images   ####################################################
img = Image.open('take1.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

take1 = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
take1.window = (0,screenresV-img.size[1],img.size[0],img.size[1])
take1.alpha = 128
#take1.layer = 3

#Load images   ####################################################
img = Image.open('take2.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

take2 = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
take2.window = (0,screenresV-img.size[1],img.size[0],img.size[1])
take2.alpha = 128
#take2.layer = 3

#Load images   ####################################################
img = Image.open('take3.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

take3 = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
take3.window = (0,screenresV-img.size[1],img.size[0],img.size[1])
take3.alpha = 128
#take3.layer = 3

#Load images   ####################################################
img = Image.open('uploading.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

uploading = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
uploading.window = ((screenresH-img.size[0])/2,(screenresV-img.size[1])/2,img.size[0],img.size[1])
uploading.alpha = 128
#uploading.layer = 3

#Load images   ####################################################
img = Image.open('working.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

working = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
working.window = ((screenresH-img.size[0])/2,(screenresV-img.size[1])/2,img.size[0],img.size[1])
working.alpha = 128
#working.layer = 3

#Load images   ####################################################
img = Image.open('uploadtofacebook.png')
#Create an image padded to the required size with mode 'RGB'
pad = Image.new('RGB', (
	((img.size[0] + 31) // 32) * 32,
	((img.size[1] + 15) // 16) * 16,
	))
#paste image
pad.paste(img, (0, 0))

uploadtofacebook = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
uploadtofacebook.window = ((screenresH-img.size[0])/2,100,img.size[0],img.size[1])
uploadtofacebook.alpha = 128
#uploadtofacebook.layer = 3

try:
	while True:
		startscreen.layer = 3
		GPIO.wait_for_edge(23, GPIO.RISING)
		
		take1.layer = 3
		startscreen.layer = 1
		ready.layer = 3
		sleep(2)
		ready.layer = 1
		setimg.layer = 3
		sleep(2)
		setimg.layer = 1
		go.layer = 3
		sleep(2)
		
		camera.capture('images/temp/1.jpg', resize=(pictureresH,pictureresV))
		
		go.layer = 1
		take1.layer = 1
		take2.layer = 3
		startscreen.layer = 1
		ready.layer = 3
		sleep(2)
		ready.layer = 1
		setimg.layer = 3
		sleep(2)
		setimg.layer = 1
		go.layer = 3
		sleep(2)
		
		
		camera.capture('images/temp/2.jpg', resize=(pictureresH,pictureresV))
		
		go.layer = 1
		take2.layer = 1
		take3.layer = 3
		startscreen.layer = 1
		ready.layer = 3
		sleep(2)
		ready.layer = 1
		setimg.layer = 3
		sleep(2)
		setimg.layer = 1
		go.layer = 3
		sleep(2)
		
		
		camera.capture('images/temp/3.jpg', resize=(pictureresH,pictureresV))
		
		go.layer = 1
		take3.layer = 1
		take4.layer = 3
		startscreen.layer = 1
		ready.layer = 3
		sleep(2)
		ready.layer = 1
		setimg.layer = 3
		sleep(2)
		setimg.layer = 1
		go.layer = 3
		sleep(2)
		
		
		camera.capture('images/temp/4.jpg', resize=(pictureresH,pictureresV))
		
		
		take4.layer = 1
		go.layer = 1
		working.layer = 3

		#command = 'montage ' + os.path.abspath(os.path.dirname(__file__))+'/images/*.jpg -tile 2x2 -geometry +10+10 ' + os.path.abspath(os.path.dirname(__file__))+'/montage'+str(imagecount)+'.jpg'
		
		
		command = 'montage ' + os.path.abspath(os.path.dirname(__file__))+'/images/temp/*.jpg -tile 2x2 -geometry +10+10 ' + os.path.abspath(os.path.dirname(__file__))+'/images/temp/5.jpg'
		print command
		#combine images
		process = subprocess.Popen(command, shell=True)
		process.wait()
		
		command = 'montage ' + os.path.abspath(os.path.dirname(__file__))+'/images/temp/5.jpg ' + os.path.abspath(os.path.dirname(__file__))+'/banner.jpg -tile 2x1 -geometry +5+5 ' + os.path.abspath(os.path.dirname(__file__))+'/images/temp/montage.jpg'
		print command
		#combine banner
		process = subprocess.Popen(command, shell=True)
		process.wait()
		
		
		print("montage saved")
		#working.layer = 1
		
		
		
		#Load montage image   ####################################################
		img = Image.open('images/temp/montage.jpg')
		#Create an image padded to the required size with mode 'RGB'
		pad = Image.new('RGB', (
			((img.size[0] + 31) // 32) * 32,
			((img.size[1] + 15) // 16) * 16,
			))
		#paste image
		pad.paste(img, (0, 0))
		working.layer = 1
		montage = camera.add_overlay(pad.tostring(), size=img.size, fullscreen=False)
		#montage.window = ((screenresH-img.size[0])/2,(screenresV-img.size[1])/2,img.size[0],img.size[1])
		montage.window = (0,0,screenresH,screenresV)
		
		GPIO.remove_event_detect(22)
		print("listening for button press")
		GPIO.add_event_detect(23, GPIO.RISING)
		montage.layer = 3
		uploadtofacebook.layer = 3
		sleep(15)
		#print("sleeping and waiting")
		uploadtofacebook.layer = 1
		camera.remove_overlay(montage)
		
		
		
		if GPIO.event_detected(23):
			#####################################
			
			uploading.layer = 3

			#post final image to facebook
			graph = GraphAPI('*******')
			graph.post(
				#path = 'me/photos',  ##my wall
                                path = '1456004404712766/photos',   ##sophie's birthday
				#path = '*******/photos',
                                source = open('images/temp/montage.jpg', 'rb')#,
				#message = 'image ' + str(imagecount)
			)
			
			uploading.layer = 1
			######################################
		
		
		#cleanup
		GPIO.remove_event_detect(23)
		
		
		######################################
		
		#copy image to permanent location
		filename = 'images/' + time.strftime("%Y.%m.%d - %H.%M.%S") + '.jpg'
		shutil.copyfile('images/temp/montage.jpg',filename)
		
		
		#delete images after uploading
		command = 'rm '+ os.path.abspath(os.path.dirname(__file__))+'/images/temp/*.jpg'
		process = subprocess.Popen(command, shell=True)
		process.wait()
		
		

except KeyboardInterrupt:
	print("Exiting")
finally:
	GPIO.cleanup()		#cleanup normal exit
	camera.close()
	os.chdir(defaultdir)
