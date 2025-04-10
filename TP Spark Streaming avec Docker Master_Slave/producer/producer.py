import socket
import time
import random

HOST = '0.0.0.0'
PORT = 9999

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"🚀 Producer listening on {HOST}:{PORT}")
        
        while True:
            conn, addr = server_socket.accept()
            print(f"🔌 Connected to {addr}")
            try:
                while True:
                    number = random.randint(1, 100)
                    conn.sendall(f"{number}\n".encode())
                    print(f"📤 Sent: {number}")
                    time.sleep(1)
            except (ConnectionResetError, BrokenPipeError):
                print("⚠️ Connection lost, retrying...")
            finally:
                conn.close()

if __name__ == "__main__":
    main()