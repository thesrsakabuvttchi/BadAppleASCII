import time
from playsound import playsound
import threading
import curses

screen = curses.initscr()
screen.refresh()
screen.resize(150,150)

t = threading.Thread(target=playsound, args=('BadApple.mp3',))
t.start()

begin = time.time()

for i in range(7777):
    f = open("./Frames/Frame%d.txt"%(i), "r")
    data = f.read()
    while (time.time()-begin<i*0.04166):
        continue
    screen.addstr(0, 0,data)
    screen.refresh()


curses.napms(2000)
curses.endwin()    
t.join()
