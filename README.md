<p align="center">
  <img src="https://img.shields.io/badge/Project-Reverse_Shell_C2-red?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Purpose-Educational-blue?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Platform-Kali_Linux_|_Windows-lightgrey?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge&labelColor=black" />
  <img src="https://img.shields.io/badge/Date-May_2026-purple?style=for-the-badge&labelColor=black" />
</p>

# 🔴 Reverse Shell C2 Handler - Command & Control Demo

## 📋 Executive Summary

This project demonstrates a fully functional **Reverse Shell Command and Control (C2) system** using Python sockets. The attacker (Kali Linux) sets up a listener, and the victim (Windows) initiates an outbound connection, successfully bypassing traditional firewall rules.

## 🖥️ Lab Environment

| Component | Specification |
|-----------|---------------|
| **Attacker OS** | Kali Linux |
| **Victim OS** | Windows 10/11 |
| **Network** | Isolated Lab Network |
| **Protocol/Port** | TCP / 4444 |
| **Language** | Python 3.14.3 |
| **Libraries** | socket, subprocess, os |

## 🚀 Attack Chain

| Phase | Technique | Details |
|-------|-----------|---------|
| **1** | **Listener Setup** | `attacker.py` creates socket on port 4444 |
| **2** | **Payload Execution** | `victim.py` connects back to attacker |
| **3** | **C2 Handshake** | Connection established |
| **4** | **Remote Control** | Commands execute on victim |
| **5** | **Clean Exit** | `exit` terminates session |

## 🛠️ Files

| File | Purpose |
|------|---------|
| `attacker.py` | C2 listener for Kali Linux |
| `victim.py` | Reverse shell payload for Windows |
| `REVERSE SHELL HANDLER.docx` | Complete project report |
| `/screenshots/` | 17 evidence screenshots |

## 📸 Commands Tested

| Command | Result |
|---------|--------|
| `whoami` | Username retrieved |
| `dir` | Files listed |
| `ipconfig` | Network info shown |
| `calc` | Calculator opened |
| `exit` | Connection closed |

## 🛡️ Why Firewalls Don't Block Reverse Shells

Standard firewalls BLOCK incoming connections but ALLOW outgoing connections.

**Normal Connection (BLOCKED):**

> Attacker → ✗ Firewall → Victim

**Reverse Shell (ALLOWED):**

> Attacker ← ✓ Firewall ← Victim

The victim initiates the connection outward, so the firewall allows it.

## ✅ Key Findings

| Finding | Recommendation |
|---------|----------------|
| Firewall bypass via reverse shell | Implement egress filtering |
| Python payload undetected | Enable application whitelisting |
| Remote command execution | Deploy EDR monitoring |

## ⚠️ Disclaimer

> This project was completed for educational purposes as part of the CEH v13 training curriculum. All demonstrations were performed in a controlled lab environment.

## 🔗 Connect with Me

[![GitHub](https://img.shields.io/badge/GitHub-bimalbist07-black?logo=github&style=for-the-badge)](https://github.com/bimalbist07)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Bimal_Bist-blue?logo=linkedin&style=for-the-badge)](https://www.linkedin.com/in/bimal-bist-98a324315/)

---

*CEH v13 Training Project - Reverse Shell Command & Control Demo*
