from threading import Lock

from utils.menu_helper import welcome_message, main_menu


class AuctionHouse(object):

    def __init__(self):
        self._lock = Lock()
        self._clients = []

    def broadcast(self, message):
        with self._lock:
            for client in self._clients:
                client.send(message)

    def client_handler(self, client, address):
        with self._lock:
            self._clients.append(client)

        # Welcoming message to user
        client.send(welcome_message)
        while True:
            try:
                # Show main menu
                client.send(main_menu)

                # Receive answer/menu choice
                message = self.read_user_input(client)

                print(f"Client {str(address)} says {message}")

                if message == '1':
                    pass
                elif message == '2':
                    pass
                else:
                    pass

                client.send(f"Your choice was {message}".encode('utf-8'))
                # self.broadcast(message)
            except:
                with self._lock:
                    self._clients.remove(client)

                print(f"Client {address} disconnected")
                client.close()
                pass

    @staticmethod
    def read_user_input(client):
        return str(client.recv(1024).decode("utf-8")).strip()
