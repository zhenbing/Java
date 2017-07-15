# -*- coding:UTF-8 -*-

with open("D:/tmp/surface.csv", 'rb') as f:
    i = 0
    for line in f:
        print line
        if i>3:
            break
        i=i+1
        


