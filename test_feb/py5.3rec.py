import os
import sys

def set(path):
    print path
    files = os.listdir(path)
    for file in files:
        file=os.path.join(path,file)
        if os.path.isfile(file):
            print file
        else:
            set(file)

dir = sys.argv[1]
names=os.listdir(dir)
paths = [os.path.join(dir,name) for name in names]
for path in paths:
    if os.path.isfile(path):
        print path
    else:
        set(path)
