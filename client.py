import socket
import json

# shitty temporary client for catspeak

def send_request(action, message=None):
    host = "127.0.0.1"
    port = 47101

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))

        request = {"action": action}
        if message:
            request["message"] = message

        client_socket.send(json.dumps(request).encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {json.loads(response)}")

        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received further data: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
        print("Socket closed.")


if __name__ == "__main__":
    send_request("echo", "This is a test message.")
    send_request("auth", "Authenticate me")
