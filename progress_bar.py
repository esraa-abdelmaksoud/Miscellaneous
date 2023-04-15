from time import sleep
import sys

n = 100
for i in range(n):
    sys.stdout.write('\r')
    sys.stdout.write("Files are being processed... {:.0f}%".format((100/(n-1)*i)))
    sys.stdout.flush()
    sleep(0.25)