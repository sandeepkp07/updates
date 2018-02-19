import os
import sys
dir = sys.argv[1]
names=os.listdir(dir)
paths = [os.path.join(dir,name) for name in names]
for path in paths:
    if os.path.isfile(path):
        print path
    else:
        subdir=os.walk(path)
        for t in subdir:
             for files in t:
                print files
