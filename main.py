import socket
import threading
import json


# placeholder for now.
def authenticate(data):
    return {"status": "success", "message": "Authentication successful"}

def handle_client(client_socket, addr):
    print(f"A connection from {addr} has been established.")
    try:
        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                data = json.loads(message)
                action = data.get("action")

                if action == "echo":
                    response = {"status": "success", "message": data.get("message")}
                elif action == "auth":
                    response = authenticate(data)
                else:
                    response = {"status": "error", "message": "Unknown action"}

                client_socket.send(json.dumps(response).encode('utf-8'))
            else:
                break
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print(f"Connection from {addr} closed.")
        client_socket.close()


def start_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"Server started on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        threading.Thread(target=handle_client, args=(client_socket, addr)).start()


if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 47101
    start_server(HOST, PORT)
