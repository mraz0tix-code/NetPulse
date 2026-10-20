# NetPulse 📡

**NetPulse** is a lightweight and fast CLI tool designed to automate network auditing and connection monitoring. Built specifically for advanced Linux users and optimized for the `Kitty` terminal emulator on Arch Linux.

This tool allows system administrators or network engineers to manage workflows via an interactive terminal menu without having to type complex flags manually.

## 🔥 Features

- 🌐 **Internet Check Menu**: Quick ping diagnostics to Google DNS (`8.8.8.8`) or any custom domain/IP address.
- 🔌 **Ports Monitor**: Instant display of all listening TCP/UDP ports in the system using the efficient `ss` utility.
- 🔍 **Nmap Subnet Scanner**: Powerful subnet auditing (detects running services, versions, and target operating systems) using SYN-scan mode.

## 🛠️ Dependencies

To run this tool successfully, ensure the following packages are installed on your Linux system:
- `python3`
- `kitty` (terminal emulator used to isolate processes with the `--hold` flag)
- `nmap` (required for the subnet scanning mode)
- `iproute2` (provides the `ss` utility, pre-installed by default on Arch Linux)

## 🚀 Quick Start

1. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com
cd NetPulse
```

2. Make the script executable:
```bash
chmod +x netpulse.py
```

3. Run the tool:
```bash
./netpulse.py
```

## ⚙️ Architecture
The project is written in pure Python without any heavy third-party packages that clutter the runtime environment. All system automation is built around the native `subprocess` module, which securely interacts with underlying Linux core utilities.

---
*Created by Max under Arch Linux.*
