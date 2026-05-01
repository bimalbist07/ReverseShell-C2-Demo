# 🔴 Reverse Shell C2 Handler - Command & Control Demo

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows-lightgrey)](https://www.kali.org/)
[![Educational](https://img.shields.io/badge/Purpose-Educational-red.svg)]()
[![Status](https://img.shields.io/badge/Status-Completed-brightgreen)]()

## 📋 Executive Summary

This project demonstrates a fully functional **Reverse Shell Command and Control (C2) system** using Python sockets. The attacker (Kali Linux) sets up a listener, and the victim (Windows) initiates an outbound connection, successfully bypassing traditional firewall rules. This simulation showcases the exact technique used by real-world malware like Cobalt Strike and Metasploit, providing a clear understanding of both the offensive mechanism and defensive countermeasures.

## 🖥️ Lab Environment

| Component | Specification |
|-----------|---------------|
| **Attacker OS** | Kali Linux (IP: `192.168.1.94`) |
| **Victim OS** | Windows 10/11 (IP: `192.168.1.71`) |
| **Network** | Same WiFi network (`192.168.1.x`) |
| **Protocol/Port** | TCP / `4444` |
| **Language** | Python `3.14.3` |
| **Libraries** | `socket`, `subprocess`, `os` |

## 🚀 Attack Chain & Execution Flow

| Phase | Technique | Details |
|-------|-----------|---------|
| **1** | **Listener Setup** | `attacker.py` creates a socket bound to port `4444` on Kali |
| **2** | **Firewall Bypass** | Windows Firewall is temporarily disabled to allow outbound traffic |
| **3** | **Payload Execution** | `victim.py` initiates an outbound TCP connection to `192.168.1.94:4444` |
| **4** | **C2 Handshake** | Connection is established; attacker gains a `C2 Shell>` prompt |
| **5** | **Remote Control** | Attacker sends commands (e.g., `whoami`, `calc`) which execute on Windows |
| **6** | **Post-Exploitation** | Commands demonstrate info gathering, file creation, and app control |
| **7** | **Clean Exit** | `exit` command terminates the session gracefully |

## 🛠️ Tools & Code Used

| Category | Tools / Files |
|----------|---------------|
| **C2 Handler (Attacker)** | `attacker.py` (Kali Linux) |
| **Reverse Shell (Victim)** | `victim.py` (Windows 10/11) |
| **Network Utilities** | `ipconfig` (Windows), `ifconfig`/`ip a` (Kali) |
| **Exploitation Commands** | `whoami`, `dir`, `ipconfig`, `calc`, `echo`, `exit` |

## 📁 Repository Contents

| Path | Description |
|------|-------------|
| `attacker.py` | C2 listener script for Kali Linux |
| `victim.py` | Reverse shell payload for Windows |
| `/screenshots/` | 17+ evidence screenshots documenting each phase |
| `REVERSE SHELL HANDLER.docx` | Comprehensive project report |

## 📸 Key Evidence & Commands Executed

All screenshots in the `/screenshots/` directory demonstrate:

| Command | Purpose | Result |
|---------|---------|--------|
| `whoami` | Identify current user | `desktop-aq4tbn4\predator` |
| `dir` | List directory contents | Desktop files enumerated |
| `ipconfig` | Show network configuration | Victim IP `192.168.1.71` confirmed |
| `calc` | Launch application remotely | Calculator opened on Windows |
| `echo > hacked.txt` | Create a text file | `hacked.txt` written to Desktop |
| `help` | Display available commands | Command menu shown |
| `exit` | Close C2 session | Connection terminated |

## 🛡️ Why This Bypasses Firewalls

Standard firewalls block **incoming** connections but **allow outgoing** traffic (e.g., web browsing). A reverse shell exploits this by having the **victim initiate the connection outward**. The firewall perceives this as legitimate outbound traffic, allowing the malicious tunnel to be established.

**Conceptual Diagram:**
```text
Normal Connection (BLOCKED):
[Attacker] -----X----> [Firewall] -----> [Victim]

Reverse Shell (ALLOWED):
[Attacker] <-----✓---- [Firewall] <----- [Victim]
