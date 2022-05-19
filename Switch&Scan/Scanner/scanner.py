import uuid 
import csv
import nmap
import tkinter as tk
from tkinter import messagebox, DISABLED, NORMAL, END
import threading


nm = nmap.PortScanner()


def get_out(network):
    try:
        scan_ports = nm.scan(network, arguments="-O -Pn")
    except:
        return False
    ips_list = list(scan_ports['scan'].keys())

    results = []
    i = 1
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
        try:
            op_sys = scan_ports['scan'][ip]['osmatch'][0]['name']
            rslt.append(op_sys)
        except:
            op_sys = "Unknown"
            rslt.append(op_sys)
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
    with open('scan.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Host", "IP", "MAC", "UUID", "active TCP/UDP Ports:Service", "OS"])
        writer.writerows(results)

    return True



def run():
    
    button_scan.configure(bg="green")
    network = entry_net.get()
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

window = tk.Tk()
window.columnconfigure([0, 1, 2], weight=0, minsize=100)
window.rowconfigure(2, weight=0, minsize=100)
window.rowconfigure(1, weight=0, minsize=50)
window.rowconfigure(0, weight=0, minsize=10)


label_net = tk.Label(window, text="Network Address\ni.e: 192.168.10.0/24")
entry_net = tk.Entry(window)

label_net.grid(row=0, column=1)
entry_net.grid(row=1, column=1)



button_scan = tk.Button(window, text="Scan", background="black", 
                        fg="white", width=15, command=run, height=2)
button_scan.grid(row=5, column=1)

tk.mainloop()