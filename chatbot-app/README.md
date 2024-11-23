Advanced Python Tutorial: Building a Chat Application

Project Overview
We'll create a real-time chat application where multiple clients can connect to a server and send/receive messages. The server will handle incoming connections and broadcast messages to all connected clients.

Features
Server: Handles client connections and broadcasts messages.
Client: Allows users to send and receive messages.
Concurrency: Uses threading to manage multiple clients.
Modular Design: Code will be organized into reusable modules.
Logging: Tracks server and client activity in log files.
Setting Up the Environment
Prerequisites:
Python 3.8 or higher
Basic understanding of networking (IP and ports)
Recommended Tools:
Code Editor: VSCode, PyCharm, or any text editor.
Installations:
No external libraries are required for this project since we’ll use Python’s built-in modules like socket, threading, json, and logging.

Project Structure
Here’s how the project files will be organized:

markdown
Copy code
chat_application/
├── server/
│   ├── __init__.py
│   ├── server.py
│   ├── client_handler.py
│   └── logger.py
├── client/
│   ├── __init__.py
│   ├── client.py
│   ├── logger.py
├── main.py
server/: Contains server-related modules.

server.py: Starts the server and accepts client connections.
client_handler.py: Handles individual client threads.
logger.py: Handles server-side logging.
client/: Contains client-related modules.

client.py: Provides client functionality.
logger.py: Handles client-side logging.
main.py: Entry point to start the server or client.

Step 1: Setting Up Modules
We’ll create modules for server, client, and logging functionalities.

1.1 Server Module
File: server/server.py
This module will manage the server’s operations: accepting connections and broadcasting messages.

python
Copy code
# server/server.py
import socket
import threading
from .client_handler import handle_client
from .logger import setup_logger

# Logger setup
logger = setup_logger("server.log")

class ChatServer:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []

    def start(self):
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(5)
            logger.info(f"Server started on {self.host}:{self.port}")
            print(f"Server running on {self.host}:{self.port}")

            while True:
                client_socket, address = self.server_socket.accept()
                self.clients.append(client_socket)
                logger.info(f"New connection from {address}")
                print(f"New connection: {address}")

                # Handle the client in a new thread
                thread = threading.Thread(target=handle_client, args=(client_socket, self.clients, logger))
                thread.start()
        except Exception as e:
            logger.error(f"Error: {e}")
        finally:
            self.stop()

    def stop(self):
        logger.info("Shutting down server...")
        self.server_socket.close()
1.2 Client Handler Module
File: server/client_handler.py
This module handles communication with individual clients and broadcasts messages to all connected clients.

python
Copy code
# server/client_handler.py
import json

def handle_client(client_socket, clients, logger):
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                logger.info(f"Received: {message}")
                broadcast(message, client_socket, clients)
            else:
                break
    except Exception as e:
        logger.error(f"Client error: {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()
        logger.info("Client disconnected.")

def broadcast(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except:
                client.close()
                clients.remove(client)
1.3 Server Logger Module
File: server/logger.py
This module configures logging for server activities.

python
Copy code
# server/logger.py
import logging

def setup_logger(log_file):
    logger = logging.getLogger("ChatServer")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
1.4 Client Module
File: client/client.py
This module implements the client’s functionality to connect to the server and send/receive messages.

python
Copy code
# client/client.py
import socket
import threading
from .logger import setup_logger

# Logger setup
logger = setup_logger("client.log")

class ChatClient:
    def __init__(self, host="127.0.0.1", port=5000):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            logger.info("Connected to server")
            print("Connected to server")
            
            # Start a thread to listen for incoming messages
            thread = threading.Thread(target=self.receive_messages)
            thread.start()

            # Sending messages
            while True:
                message = input()
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
                    print(f"Server: {message}")
        except:
            logger.error("Disconnected from server.")
1.5 Client Logger Module
File: client/logger.py
This module configures logging for client activities.

python
Copy code
# client/logger.py
import logging

def setup_logger(log_file):
    logger = logging.getLogger("ChatClient")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger
Step 2: Running the Application
File: main.py
python
Copy code
# main.py
from server.server import ChatServer
from client.client import ChatClient

def main():
    print("1. Start Server")
    print("2. Start Client")
    choice = input("Enter your choice: ")

    if choice == "1":
        server = ChatServer()
        server.start()
    elif choice == "2":
        client = ChatClient()
        client.connect()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
Step 3: Testing
Start the Server:

Run main.py and choose 1 to start the server.
The server will listen for connections on 127.0.0.1:5000.
Start Multiple Clients:

Open new terminals and run main.py, choosing 2 to start clients.
Clients will connect to the server.
Send Messages:

Type a message in one client and watch it appear on all other clients.
Advanced Concepts Covered
Multithreading: Handled multiple client connections using threads.
Networking: Used sockets for real-time communication.
Modules: Organized the project into reusable modules.
Logging: Recorded activities for debugging and tracking.
Next Steps
Enhance Security:
Add encryption using libraries like ssl or cryptography.
Implement User Authentication:
Require clients to log in with usernames and passwords.
GUI Interface:
Use a library like Tkinter or PyQt for a graphical chat client.
File Sharing:
Extend the chat application to allow file sharing between clients.
Enjoy building your chat application! 🎉