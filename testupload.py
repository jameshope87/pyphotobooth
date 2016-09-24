from facepy import GraphAPI
import picamera
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

while True:
    print("Ready and waiting!")
    GPIO.wait_for_edge(23, GPIO.RISING)

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.capture('test.jpg')
    print("picture taken!")
    time.sleep(1)
    print("uploading...")
    graph = GraphAPI('*******')
    graph.post(
        #path = 'me/photos',  ##my wall
        #path = '/photos',   ##testing event
        path = '*******/photos',
        source = open('test.jpg', 'rb')#,
        #message = 'image ' + str(imagecount)
    )
    print("Successfully uploaded!")
