import cv2

vidcap = cv2.VideoCapture('BadApple.mp4')
success,image = vidcap.read()
count = 0

AsciVid = []

while success:
    image = cv2.resize(image,(150,50))
    chars = []
    for i in image:
        for j in i:
            if(sum(j)<191):
                chars.append(' ')
            elif (sum(j)<382):
                chars.append('.')
            elif (sum(j)<573):
                chars.append('*')            
            else:
                chars.append('@')
        chars.append('\n')

    AsciVid.append(''.join(chars))
    f = open("./Frames/Frame%d.txt"%(count), "w")
    f.write(''.join(chars))
    f.close()
    success,image = vidcap.read()
    count += 1
    print("converting..........")

