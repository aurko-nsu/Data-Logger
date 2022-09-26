# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib import style
# import serial

# style.use('dark_background')

# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)

# i = 0
# xs = []
# ys = []

# def animate(i):
#     ser = serial.Serial('COM6', 9600)
#     line = ser.readline()
#     if line:
#         string = line.decode() 
#         num = int(string)        
#         xs.append(i)
#         ys.append(num)
#         i = i + 1
#     ax1.clear()
#     ax1.plot(xs, ys, linewidth = '4', marker = 'o')
        
# ani = animation.FuncAnimation(fig, animate, interval=10)
# plt.show()

# ---------------------------------------another


import serial # import Serial Library
import matplotlib.pyplot as plt #import matplotlib library
from drawnow import *

tempF= []
pressure=[]
plt.ion() #Tell matplotlib you want interactive mode to plot live data
cnt=0

def makeFig(): #Create a function that makes our desired plot
    # plt.plot(pressure, 'ro-')
    
    # plt.ylim(0,100)                                 #Set y min and max values
    plt.title('My Live Streaming Sensor Data')      #Plot the title
    plt.grid(True)                                  #Turn the grid on
    plt.ylabel('Temp F')                            #Set ylabels
    plt.plot(tempF, 'ro-', label='Degrees F')       #plot the temperature
    plt.legend(loc='upper left')                    #plot the legend
    plt2=plt.twinx()                                #Create a second y axis
    # plt.ylim(93450,93525)                           #Set limits of second y axis- adjust to readings you are getting
    plt2.plot(pressure, 'b^-', label='Pressure (Pa)') #plot pressure data
    plt2.set_ylabel('Pressrue (Pa)')                    #label second y axis
    plt2.ticklabel_format(useOffset=False)           #Force matplotlib to NOT autoscale y axis
    plt2.legend(loc='upper right')                  #plot the legend
    
#https://toptechboy.com/python-with-arduino-lesson-11-plotting-and-graphing-live-data-from-arduino-with-matplotlib/
arduinoData = serial.Serial('COM14', 115200) #Creating our serial object named arduinoData
while True: # While loop that loops forever
    while (arduinoData.inWaiting() == 0):
        pass
    aString = arduinoData.readline()
    bString = aString.decode('utf-8')
    dataArray = bString.split(',')
    temp = int(dataArray[0])            #Convert first element to floating number and put in temp
    P =    int(dataArray[1])            #Convert second element to floating number and put in P
    print(dataArray[1])
    tempF.append(temp)                     #Build our tempF array by appending temp readings
    pressure.append(P)                     #Building our pressure array by appending P readings
    drawnow(makeFig)                       #Call drawnow to update our live graph
    plt.pause(.000001)                     #Pause Briefly. Important to keep drawnow from crashing
    cnt=cnt+1
    if(cnt>50):                            #If you have 50 or more points, delete the first one from the array
        tempF.pop(0)                       #This allows us to just see the last 50 data points
        pressure.pop(0)

# while True:
#     while (arduinoData.inWaiting() == 0):
#         pass
#     aString = arduinoData.readline().decode('utf-8')
#     dataArray = aString.split(',')
#     print(dataArray[0])