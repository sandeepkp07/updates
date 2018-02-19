import os
import sys
dir = sys.argv[1]
names=os.listdir(dir)
paths = [os.path.join(dir,name) for name in names]
for path in paths:
    if os.path.isfile(path):
        print path
    else:
<<<<<<< HEAD
        subdir=os.walk(path)
        for t in subdir:
             for files in t:
                print files
=======
        print path
        for sub in os.walk(path):
            print sub[0]
>>>>>>> 5bb43aebc0ac3a9748c86384d6576c8626bc645d
