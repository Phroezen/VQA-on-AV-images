import os
import time
start_time = time.time()
os.system("python predicates.py")
os.system("python adjust.py")
print("%s seconds" % (time.time()-start_time))