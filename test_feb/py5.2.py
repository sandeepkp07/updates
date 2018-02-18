import os
import sys
import pprint
dir = sys.argv[1]
names=os.listdir(dir)
paths = [os.path.join(dir,name) for name in names]
sizes = [(path, os.stat(path).st_size) for path in paths]
list = sorted(sizes, key=lambda x: x[1])
pprint.pprint(list)

