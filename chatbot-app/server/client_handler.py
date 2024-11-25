def handle_client(client_socket, clients, logger):
    try:
        while True:
            message = client_socket.recv(1024).decode("utf-8")
            if message:
                logger.info(f"Received: {message}")
                broadcast(message, client_socket, clients, logger)
            else:
                break
    except Exception as e:
        logger.error(f"Client error: {e}")
    finally:
        clients.remove(client_socket)
        client_socket.close()
        logger.info("Client disconnected.")


def broadcast(message, sender_socket, clients, logger):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode("utf-8"))
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                client.close()
                clients.remove(client)
