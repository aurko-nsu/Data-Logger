# import time
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation

# fig = plt.figure()
# x , y = [] , []

# number = 0
# i = 0

# def work(i):
#     x.append(i)
#     y.append(number)
#     plt.plot(x , y)
#     i += 1
#     number += 2

# ani = animation.FuncAnimation(fig, work, interval=20, blit=True, save_count=50)
# plt.show()


import matplotlib.animation as animation
import matplotlib.pyplot as plt
 
fig = plt.figure()
axis = plt.axes(xlim =(0, 200),
                ylim =(0, 100))
 
line, = axis.plot([], [], lw = 2)
 
def init():
    line.set_data([], [])
    return line,

xdata, ydata = [], []
 
def animate(i):
    x = i + 1
    y = i + 2

    xdata.append(x)
    ydata.append(y)
    line.set_data(xdata, ydata)
     
    return line,
 
# calling the animation function    
anim = animation.FuncAnimation(fig, animate,
                            interval = 20,
                            blit = True,
                            save_count=50)

plt.show()