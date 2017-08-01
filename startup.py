import subprocess
import os
return_code1 = subprocess.call("service hostapd restart", shell=True)
return_code2 = subprocess.call("service udhcpd start", shell=True)
#return_code3 = subprocess.call("cd /root/bigtooth/blue_hydra/bin", shell=True)
os.chdir("/root/bigtooth/blue_hydra/bin")
return_code4 = subprocess.call("ls", shell=True)
return_code5 = subprocess.call("./blue_hydra", shell=True)
