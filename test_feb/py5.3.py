import os
import sys
dir = sys.argv[1]
names=os.listdir(dir)
paths = [os.path.join(dir,name) for name in names]
for path in paths:
    if os.path.isfile(path):
        print path
    else:
        print path
        for sub in os.walk(path)
            print sub[0]
