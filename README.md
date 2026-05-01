<p align="center">
  <img src="https://img.shields.io/badge/Project-Reverse_Shell_C2-red?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Purpose-Educational-blue?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Platform-Kali_Linux_|_Windows-lightgrey?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Date-May_2026-purple?style=for-the-badge&labelColor=black" />
</p>

# 🔴 Reverse Shell C2 Handler - Command & Control Demo

## 📋 Executive Summary

This project demonstrates a fully functional **Reverse Shell Command and Control (C2) system** using Python sockets. The attacker (Kali Linux) sets up a listener, and the victim (Windows) initiates an outbound connection, successfully bypassing traditional firewall rules. This simulation showcases the exact technique used by real-world malware like Cobalt Strike and Metasploit, providing a clear understanding of both the offensive mechanism and defensive countermeasures. The assessment was conducted in an isolated lab environment with all proper authorizations.

## 🖥️ Lab Environment

| Component | Specification |
|-----------|---------------|
| **Attacker OS** | Kali Linux |
| **Victim OS** | Windows 10/11 |
| **Network** | Isolated Lab Network |
| **Protocol/Port** | TCP / 4444 |
| **Language** | Python 3.14.3 |
| **Libraries** | socket, subprocess, os |

## 🔴 Technical Details

| Component | Description |
|-----------|-------------|
| **Attack Technique** | Reverse TCP Shell |
| **C2 Mechanism** | Python Socket Programming |
| **Firewall Bypass** | Outbound Connection Exploitation |
| **Persistence** | Session-based (until exit command) |
| **Encryption** | None (plain text - for educational purposes) |

## 🚀 Attack Chain & Execution Flow

| Phase | Technique | Details |
|-------|-----------|---------|
| **1** | **Listener Setup** | `attacker.py` creates a socket bound to port 4444 on Kali |
| **2** | **Firewall Configuration** | Windows Firewall temporarily disabled for outbound traffic |
| **3** | **Payload Execution** | `victim.py` initiates outbound TCP connection to attacker |
| **4** | **C2 Handshake** | Connection established; attacker gains interactive shell |
| **5** | **Remote Control** | Attacker sends commands that execute on victim system |
| **6** | **Information Gathering** | Commands demonstrate reconnaissance capabilities |
| **7** | **Post-Exploitation** | File creation, application launch, system enumeration |
| **8** | **Clean Exit** | `exit` command terminates session gracefully |

## 🛠️ Tools & Code Used

| Category | Tools / Files |
|----------|---------------|
| **C2 Handler (Attacker)** | `attacker.py` (Kali Linux) |
| **Reverse Shell (Victim)** | `victim.py` (Windows 10/11) |
| **Network Utilities** | `ipconfig` (Windows), `ifconfig`/`ip a` (Kali) |
| **Exploitation Commands** | `whoami`, `dir`, `ipconfig`, `calc`, `echo`, `exit` |
| **Code Editor (Kali)** | Nano |
| **Code Editor (Windows)** | Notepad |

## 📁 Repository Structure
ReverseShell-C2-Demo/
│
├── README.md # Project documentation
├── attacker.py # C2 listener (Kali Linux)
├── victim.py # Reverse shell payload (Windows)
├── REVERSE SHELL HANDLER.docx # Complete project report
│
└── screenshots/ # All evidence screenshots
├── 01_windows_ip.png
├── 02_kali_ip.png
├── 03_attacker_code.png
├── 04_victim_code.png
├── 05_attacker_waiting.png
├── 06_victim_ready.png
├── 07_connection_kali.png
├── 08_connection_windows.png
├── 09_whoami.png
├── 10_dir.png
├── 11_ipconfig.png
├── 12_calculator.png
├── 13_file_created.png
├── 14_help.png
├── 15_exit.png
├── 16_terminals_closed.png
└── 17_firewall_off.png


## 📸 Commands Executed & Results

| Command | Purpose | Result |
|---------|---------|--------|
| `whoami` | Identify current user | Username successfully retrieved |
| `dir` | List directory contents | Desktop contents enumerated |
| `ipconfig` | Show network configuration | Network information displayed |
| `calc` | Launch application remotely | Calculator opened on victim |
| `echo > hacked.txt` | Create text file | File written to victim Desktop |
| `help` | Display available commands | Command menu shown |
| `exit` | Close C2 session | Connection terminated |

## 🛡️ Why Firewalls Don't Block Reverse Shells

Standard firewalls are configured to:

- **BLOCK** incoming connections (from internet to internal network)
- **ALLOW** outgoing connections (from internal network to internet)

A reverse shell exploits this by having the **victim initiate the connection outward**. The firewall perceives this as legitimate outbound traffic (like web browsing), allowing the malicious tunnel to be established.

**Conceptual Diagram:**

```text
Normal Connection (BLOCKED BY FIREWALL):
┌─────────┐     ✗     ┌──────────┐     ┌─────────┐
│ Attacker│ ────────► │ Firewall │ ──► │ Victim  │
└─────────┘           └──────────┘     └─────────┘

Reverse Shell (ALLOWED BY FIREWALL):
┌─────────┐           ┌──────────┐     ┌─────────┐
│ Attacker│ ◄──────── │ Firewall │ ◄── │ Victim  │
└─────────┘     ✓     └──────────┘     └─────────┘


✅ Key Findings & Recommendations
Finding	Impact	Severity	Recommendation
Successful firewall bypass via reverse shell	Remote code execution	Critical	Implement egress filtering on firewalls to block unusual outbound ports (e.g., 4444, 1337, 31337)
Python-based payload executed without detection	Significant detection gap	High	Enable application whitelisting (Windows Defender Application Control / AppLocker)
Arbitrary commands and processes launched remotely	Full system compromise	Critical	Deploy EDR solutions to monitor parent-child process anomalies (e.g., python.exe spawning cmd.exe)
Data exfiltration and file creation possible	Data breach risk	High	Enforce outbound TLS inspection and network monitoring for beaconing patterns
No authentication required for C2 access	Unauthorized access	Critical	Implement mutual authentication for all C2 communications
🛡️ Defense in Depth Strategy
Layer	Control	Implementation
Network	Egress Filtering	Block all outbound ports except 80, 443, 53
Network	IDS/IPS Signatures	Deploy Snort/Suricata rules for reverse shell patterns
Endpoint	Application Control	Only allow signed/approved executables
Endpoint	EDR Monitoring	Alert on python.exe → cmd.exe parent-child relationships
Configuration	PowerShell Logging	Enable ScriptBlock and Module logging
User Awareness	Security Training	Educate users about running unknown scripts
📚 References & Further Reading
Python Socket Programming Documentation

Reverse Shell - OWASP

MITRE ATT&CK - Command and Control (TA0011)

Cobalt Strike C2 Explained

Understanding Reverse Shells - IBM

⚠️ Disclaimer
This project was completed for educational purposes as part of the CEH v13 training curriculum.

All demonstrations were performed in a controlled, isolated lab environment on systems owned by the author. The techniques shown are for understanding cybersecurity threats and implementing proper defenses. Unauthorized use of these techniques on systems without explicit written permission is illegal and unethical. The author takes no responsibility for misuse of this code.


## 🔗 Connect with Me

<a href="https://github.com/bimalbist07">
  <img src="https://img.shields.io/badge/GitHub-bimalbist07-181717?logo=github&style=for-the-badge&labelColor=black" />
</a>
<a href="https://www.linkedin.com/in/bimal-bist-98a324315/">
  <img src="https://img.shields.io/badge/LinkedIn-Bimal_Bist-0077B5?logo=linkedin&style=for-the-badge&labelColor=white" />
</a>
