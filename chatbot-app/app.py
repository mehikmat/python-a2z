from server import ChatServer
from client import ChatClient


def main():
    print("1. Start Server")
    print("2. Start Client")
    choice = input("Enter your choice:\n")

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
