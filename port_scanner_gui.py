import socket
import tkinter as tk

def scan():
    target = entry_target.get()
    ports = int(entry_ports.get())
    result_box.delete("1.0", tk.END)

    for port in range(1, ports):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((target, port))
            result_box.insert(tk.END, f"[+] Port {port} OPEN\n")
            sock.close()
        except:
            pass

# UI
root = tk.Tk()
root.title("Port Scanner")

tk.Label(root, text="Target").pack()
entry_target = tk.Entry(root)
entry_target.pack()

tk.Label(root, text="Ports").pack()
entry_ports = tk.Entry(root)
entry_ports.pack()

tk.Button(root, text="Scan", command=scan).pack()

result_box = tk.Text(root, height=15, width=50)
result_box.pack()

root.mainloop()