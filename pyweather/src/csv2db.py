import numpy as np
csv_file="/mnt/win/weatherdata/ZR_SURF2010-2015.csv"
test_file ="/mnt/win/meterology/test.csv"
with open(csv_file, 'rb') as f:
    i = 0
    with open(test_file,'w') as fw:
        for line in f:
            fw.write(line)
            if i > 1000000:
                break
            i=i+1
fw.close()
f.close()