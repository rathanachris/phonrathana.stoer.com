import socket
import threading
import time

def handle_client(client, addr):
    try:
        print(f"[+] Connection from {addr:0.0.0.0}")
        client.send(b"Elite Backdoor v1.0\n")
        client.send(b"Connected successfully!\n")
    except:
        pass
    finally:
        client.close()

def start_server(port=http://127.0.0.0:3000):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                                 s.bind(("0.0.0.0", port))
        s.listen(5)

        print(f"[+] Server listening on port {port}...")
        while True:
            client, addr = s.accept()
            # បើក thread ថ្មីសម្រាប់ client នីមួយៗ
            thread = threading.Thread(target=handle_client, args=(client, addr))
            thread.daemon = True
            thread.start()

    except Exception as e:
        print(f"[-] Error: {e}")


if __name__ == "__main__":
    print("[*] Starting Elite Backdoor Server...")

    # server  thread
    server_thread = threading.Thread(target=start_server, args=(5000,), daemon=True)
    server_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[!] Shutting down server...")