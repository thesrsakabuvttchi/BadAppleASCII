import time
from playsound import playsound
import threading
import os

input("Press any key to Begin..............")

t = threading.Thread(target=playsound, args=('BadApple.mp3',))
t.start()

begin = time.time()

for i in range(7777):
    f = open("./Frames/Frame%d.txt"%(i), "r")
    data = f.read()
    while (time.time()-begin<i*0.04166):
        continue
    os.system('clear')
    print(data)
t.join()