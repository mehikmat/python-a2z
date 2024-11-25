import socket
import threading
from client_handler import handle_client
from helper import setup_logger

# Logger setup
logger = setup_logger("server.log", "ChatServer")


class ChatServer:

    def __init__(self, host="127.0.0.1", port=8080):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)  # request queue size is 5 as server processes one request at a time.
            logger.info(f"Server started on {self.host}:{self.port}")

            while True:
                client_socket, address = self.server_socket.accept()
                self.clients.append(client_socket)
                logger.info(f"New connection from {address}")

                # Handle the client in a new thread
                thread = threading.Thread(target=handle_client, args=(client_socket, self.clients, logger))
                thread.start()

        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"Error {e}")
        finally:
            self.stop()

    def stop(self):
        logger.info("Shutting down server...")
        self.server_socket.close()
