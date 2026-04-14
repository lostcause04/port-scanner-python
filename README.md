# 🔍 Python Port Scanner

A simple yet effective **Port Scanner** built using Python.
This project scans open ports on a target system using socket programming and provides both **CLI** and **GUI-based interfaces**.

---

## 🚀 Features

* 🔎 Scan open ports on a target IP or domain
* 💻 CLI (Command Line Interface) version
* 🖥️ GUI version using Tkinter
* ⚡ Fast scanning using socket connections
* 🎯 Custom port range input
* 🧪 Works for single or multiple targets (CLI)

---

## 🛠️ Tech Stack

* Python 3
* Socket Programming
* Tkinter (for GUI)
* Termcolor (for CLI output)

---

## 📂 Project Structure

```
port-scanner-python/
│
├── port_scanner.py          # CLI version
├── port_scanner_gui.py      # GUI version
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ▶️ How to Run

### 🔹 CLI Version

```bash
python port_scanner.py
```

**Example Input:**

```
Target: 127.0.0.1
Ports: 100
```

---

### 🔹 GUI Version

```bash
python port_scanner_gui.py
```

* Enter target (e.g., `127.0.0.1`)
* Enter number of ports
* Click **Scan**

---

## 📦 Requirements

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install termcolor
```

---

## 🧠 How It Works

This tool uses Python’s **socket library** to attempt TCP connections on different ports.

If a connection is successful → the port is considered **OPEN**.

Port scanning is widely used in:

* Network diagnostics
* Cybersecurity testing
* Vulnerability analysis ([GitHub][1])

---

## ⚠️ Disclaimer

This project is for **educational purposes only**.

Do NOT use this tool on networks or systems without proper authorization.

---

## 🚀 Future Improvements

* ⚡ Multithreading (faster scanning)
* 📊 Progress bar
* 💾 Save results to file
* 🔍 Service detection (HTTP, SSH, etc.)

---

## 👩‍💻 Author

**Ankita Rangra**

---

## ⭐ Show Some Love

If you like this project, give it a ⭐ on GitHub!

[1]: https://github.com/itaynir1/port-scanner?utm_source=chatgpt.com "itaynir1/port-scanner"
