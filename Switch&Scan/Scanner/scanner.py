# import needed modules

import uuid # to generate UUID
import csv # to store results to csv file
import nmap # to scan network
import tkinter as tk # to build the graphical user interface
from tkinter import messagebox, DISABLED, NORMAL, END
import threading # threading 


nm = nmap.PortScanner() #initialize nmap scanner 
devs = 0


def get_out(network):
    global devs
	# Scan the network, if an error is occured, return False
    try:
        scan_ports = nm.scan(network, arguments="-O -Pn")
    except:
        return False
        
    ips_list = list(scan_ports['scan'].keys()) # this list stores all IPs addresses in the network

    devs = len(ips_list)
    results = []
    i = 1
    #iterate over all IPs and extract the MAC address and generate the UUID, if no MAC address is found, replace it with ----
    for ip in ips_list:
        try:
            mac = scan_ports['scan'][ip]['addresses']['mac']
            uid = "0x" + mac.replace(":", "")
            uid = int(uid, 16)
            Uuid = str(uuid.uuid1(uid))
        except:
            mac = "--:--:--:--:--:--"
            Uuid = "********-****-****-****-************"
        
        host = "Host-" + str(i)
        rslt = [host, ip, mac, Uuid]
        i += 1
        #Retrieve the OS, if it is not found, replace it with Unknown. To detect the OS, a port should be open in the remote host, otherwise, it fails
        try:
            op_sys = scan_ports['scan'][ip]['osmatch'][0]['name']
            rslt.append(op_sys)
        except:
            op_sys = "Unknown"
            rslt.append(op_sys)
            
        # Retreive all opened ports with the service running on it separed by ;. i.e ssh:22; telnet:23. if no port is opened, fill it with -
        try:
            open_ports = list(scan_ports['scan'][ip]['tcp'].keys())
            open_ports2 = ""
            for port in open_ports:
                ser = scan_ports['scan'][ip]['tcp'][port]['name']
                service = str(port) + ':' + ser +"; "
                open_ports2 += service
                
            rslt.append(open_ports2)
            
        except Exception as error:
            open_ports2 ="-"
            rslt.append(open_ports2)

        results.append(rslt)
    #write all results to a csv file
    with open('scan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Host", "IP", "MAC", "UUID", "OS", "active TCP/UDP Ports:Service"])
        writer.writerows(results)

    return True



def run():
    
    #change the color of scan button when it is clicked
    button_scan.configure(bg="green")
    network = entry_net.get() # get the network address
    if network:
        t = threading.Thread(target=get_out, args=(network,), daemon=True)
        t.start()
        for i in window.grid_slaves():
            i.destroy()
        window.columnconfigure([0, 1, 2], weight=0, minsize=100)
        window.rowconfigure([0, 1, 2], weight=0, minsize=100)
        label_scanning = tk.Label(text="Scanning Network...")
        label_scanning.grid(row=1, column=1)
        
        
        
    else:
        messagebox.showwarning("Warning", "Enter network to scan")
        button_scan.configure(bg="black")
       
    if  button_scan.winfo_exists:
        t.join()
        for i in window.grid_slaves():
                i.destroy()
        window.columnconfigure([0, 1, 2], weight=0, minsize=100)
        window.rowconfigure([0, 1, 2], weight=0, minsize=100)
        label_scanned = tk.Label(text="Network Scanned!")
        label_scanned.grid(row=1, column=1)
        label_devices = tk.Label(text= str(devs) + " Devices found!")
        label_devices.grid(row=3, column=1)

#This Part is used to create the UI using Tkinter module.
window = tk.Tk()
window.columnconfigure([0, 1, 2], weight=0, minsize=100)
window.rowconfigure(2, weight=0, minsize=100)
window.rowconfigure(1, weight=0, minsize=50)
window.rowconfigure(0, weight=0, minsize=10)


label_net = tk.Label(window, text="Network Address\ni.e: 192.168.10.1/24")
entry_net = tk.Entry(window)

label_net.grid(row=0, column=1)
entry_net.grid(row=1, column=1)



button_scan = tk.Button(window, text="Scan", background="black", 
                        fg="white", width=15, command=threading.Thread(target=run).start
                        , height=2)
button_scan.grid(row=5, column=1)

tk.mainloop()
