This program scans an IP range or network and return the IP, MAC, UUID, Active TCP/UDP ports and the service running on it, and the operating system running on each device in the network.


Note: You will need root/administrator previliges to run the code and the executable file.

To secssefully run the code and the executable file in both windows and linux, you need to download and install nmap from Nmap's official download page "https://nmap.org/download.html"

if you already installed nmap with " pip install nmap"; you need to uninstall it by running "pip uninstall nmap"  or "pip3 uninstall nmap" if you are on Linux

then install python-nmap instead of nmap with the following command:
1- Windows:
     pip uninstall python-nmap

2- Linux:
     pip3 install python3-nmap
    
Note: "pip install nmap", installs nmap python library but python-nmap requires nmap binary, moreover nmap python library conflicts with python-nmap because they share same module name. 

Also, make sure that tkinter is installed by running "pip install tk" or "pip3 install tk" 

Once all modules are installed you can run the code:
1- in terminal if you are on Linux by this command: sudo python3 scanner.py
2- in cmd if you are on Windows (you should open cmd with admin), by this command:  python scanner.py in windows.

to run the executable file in:
  1- In windows:
     right click and choose run as administrator
  2- In Linux:
     Open a terminal and run the following command: 
       sudo ./scanner_Linux

once you run the scanner, enter the IP/Mask to scann and click scann and it will start scanning
wait untill "Networked Scanned!" is showing, then check your working directory and you find the ouput file.
