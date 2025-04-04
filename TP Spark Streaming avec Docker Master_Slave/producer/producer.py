import socket
import time
import random

HOST = '0.0.0.0'  
PORT = 9999

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"🚀 Producteur en écoute sur {HOST}:{PORT}")
        
        while True:
            conn, addr = s.accept()
            print(f"🔌 Connecté à {addr}")
            try:
                while True:
                    number = random.randint(1, 100)
                    conn.sendall(f"{number}\n".encode())
                    print(f"📤 Envoyé: {number}")
                    time.sleep(1)
            except (ConnectionResetError, BrokenPipeError):
                print("⚠️ Connexion perdue, réessai...")
            finally:
                conn.close()

if __name__ == "__main__":
    main()