import os
import imageio

file_path = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png", "11.png", "12.png", "13.png", "14.png", "15.png", "16.png", "17.png", "18.png"]

images = []

for i in range(len(file_path)):
        images.append(imageio.imread(file_path[i]))
imageio.mimsave('CM_gif.gif', images)
