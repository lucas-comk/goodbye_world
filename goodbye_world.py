import time
import os

print("Goodbye world!")
time.sleep(5)
os.system('shutdown /p /f' if os.name == 'nt' else 'shutdown -h now')