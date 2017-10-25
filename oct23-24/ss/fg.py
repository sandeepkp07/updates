import os
name=('/home/sandeep/ss/')
k=os.listdir(name)
for name in k:
 cmd ='md5sum ' + name
 fp = os.popen(cmd)
 res = fp.read()
 stat = fp.close()
 ch = res.split()
 print ch



