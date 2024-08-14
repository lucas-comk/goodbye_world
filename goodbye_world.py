import time
import subprocess
from subprocess import call

print("Goodbye world!")
time.sleep(5)
call("shutdown -h now", shell=True)