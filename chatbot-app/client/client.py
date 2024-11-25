import socket
import threading
from helper import setup_logger

# Logger setup
logger = setup_logger("client.log", "ClientChat")


class ChatClient:
    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            logger.info("Connected to server")

            # Start a thread to listen for incoming messages
            thread = threading.Thread(target=self.receive_messages)
            thread.start()

            # Sending messages
            while True:
                message = input("Enter your message:\n")
                self.client_socket.send(message.encode("utf-8"))
        except Exception as e:
            logger.error(f"Connection error: {e}")
        finally:
            self.client_socket.close()

    def receive_messages(self):
        try:
            while True:
                message = self.client_socket.recv(1024).decode("utf-8")
                if message:
                    logger.info(f"Server: {message}")
        except Exception as e:
            logger.error(f"Disconnected from server: {e}")
