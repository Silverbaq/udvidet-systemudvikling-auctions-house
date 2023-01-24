import socket
import threading

from auctionhouse import AuctionHouse

HOST = '127.0.0.1'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

auction_house = AuctionHouse()


def run_server():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}!")
        # clients.append(client)
        # broadcast(f"Client {address} connected to the server".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))
        thread = threading.Thread(target=auction_house.client_handler, args=(client, address))
        thread.start()


print("Server running...")

if __name__ == "__main__":
    run_server()
