# WiFi-Deauth
WiFi deauthentication helper for aircrack-ng

![meme](https://user-images.githubusercontent.com/16358178/205238683-75dbf361-dcb4-468d-8bdb-023568383841.png)

### Requirements
* Aircrack-ng
* Python 3.8
* WiFi adapter that support monitor and injection modes
* Linux distro with xterm (Developed and tested on Ubuntu 22.04)

If you don't have xterm or if you are using non-linux operating system, you will have to modify corresponding xterm commands accordingly for your system.

### Before starting the script
I have not added much interactivity for this code. So, you will have to edit lines 13 to 16 by adding your specific values there before running it.

You should have your WiFi adapter in monitor mode. It should be monitoring the access point that has to be attacked and the corresponding output must be written in csv format into a file.

### What this script will do
It will monitor this live csv file and start deauthentication threads against each client. It will automatically start new threads if new clients connect or if a thread dies due to some error.

> This was developed as a fun hobby project and can be used to automate aircrack-ng to assess WiFi network security. Before running this against any network make sure that you have the proper permission to test that network. Attacking a network without proper authorization is illegal.

Photo credits: https://www.azemalptekin.com/need-a-movie-suggestion-try-the-dictator/
