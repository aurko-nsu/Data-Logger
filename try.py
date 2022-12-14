from turtle import color
import serial # import Serial Library
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

sen_one= []
sen_two=[]
sen_three=[]
sen_four=[]
ymin = 0
ymax = 0
plt.ion()   #Tell matplotlib you want interactive mode to plot live data
cnt=0
fig, (ax1, ax2) = plt.subplots(2)

def makeFig(): #Create a function that makes our desired plot   
    ax1.plot(sen_one, color = 'b')       #plot the temperature
    ax1.grid(True)
    ax1.set_ylabel('One')
    ax1.set_title('One Title')

    ax2.plot(sen_two, color = 'r')       #plot the temperature
    ax2.grid(True)
    ax2.set_ylabel('Two')
    ax2.set_title('Two Title')
    
    
    # plt2=plt.twinx()                                #Create a second y axis
    # plt2.plot(sen_two, 'ro-', color='b', label='MQ 2') #plot pressure data
    # plt2.set_ylabel('MQ 2')                    #label second y axis
    # plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    # plt2.legend(loc='upper right')                  #plot the legend

    # plt3=plt.twinx()                                #Create a second y axis
    # plt3.plot(sen_three, 'ro-', color='g', label='MQ 5') #plot pressure data
    # plt3.set_ylabel('MQ 5')                    #label second y axis
    # plt3.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    # plt3.legend(loc='lower right')                  #plot the legend

    # plt4=plt.twinx()                                #Create a second y axis
    # plt4.plot(sen_four, 'ro-', color='y', label='MQ 9') #plot pressure data
    # plt4.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    # plt4.legend(loc='lower left')                  #plot the legend
    
#https://toptechboy.com/python-with-arduino-lesson-11-plotting-and-graphing-live-data-from-arduino-with-matplotlib/

arduinoData = serial.Serial('COM14', 115200) #Creating our serial object named arduinoData
while True: # While loop that loops forever
    while (arduinoData.inWaiting() == 0):
        pass
    aString = arduinoData.readline()
    bString = aString.decode('utf-8')
    dataArray = bString.split(',')
    print(dataArray[0] +" "+ dataArray[1] +" "+ dataArray[2] +" "+ dataArray[3])
    one = int(dataArray[0])            #Convert first element to floating number and put in temp
    two = int(dataArray[1])            #Convert second element to floating number and put in P
    three = int(dataArray[2])            #Convert second element to floating number and put in P
    four = int(dataArray[3])
    # print(dataArray[1])
    sen_one.append(one)                     #Build our sen_one array by appending temp readings
    sen_two.append(two)                     #Building our sen_two array by appending P readings
    sen_three.append(three)                     #Building our sen_two array by appending P readings
    sen_four.append(four)
    plt.show()                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        sen_one.pop(0)                       #This allows us to just see the last 50 data points
        sen_two.pop(0)
        sen_three.pop(0)
        sen_four.pop(0)
