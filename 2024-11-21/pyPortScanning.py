import socket
def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.0001)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"Port {port} is open")
                with open(f"port.txt","+a",encoding="utf8") as f:
                    f.write(f"https://{ip}:{port}\n")
            else:
                print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")
        input("!...")


from datetime import datetime
with open(f"port.txt","a") as f:
    time = datetime.now()
    f.write(f"\n---{time}---\n")

target_ip = "192.168.1.1"
ports = range(1, 1024)
print("Port scanning...")
target_ip = input("IP:")
for port in ports:
    scan_port(target_ip, port)


