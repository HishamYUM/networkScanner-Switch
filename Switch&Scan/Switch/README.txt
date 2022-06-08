This program connects to a CISCO switch using SSH or Telnet and execute three commands: [ "show mac address-table dynamic", "show IP arp", "show version"] then redirect the results to csv file.

Please install required modules: paramiko and tkinter  by running this command:
On Linux: pip3 install paramiko tk 
On Windows: pip install paramiko tk 

*paramiko is used to connect over SSH

run the code in terminal or cmd by the following command:
On Linux: python3 switch_ui.py
On Windows: python switch_ui.py

Once the interface shows up, choose a method to connect, either SSH or Telnet, then enter the credentials of the switch(IP, username and password), then click "Connect & Execute" and wait untill "Commands Executed" is showing.


 Once you connect and execute the commands, check you working directory for the output
