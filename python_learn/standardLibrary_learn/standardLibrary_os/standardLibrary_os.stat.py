import os
statinfo = os.stat('read2.txt')
print( statinfo)
print( statinfo.st_mode)
print(statinfo[0])