import socket
import time
from game import Game
from _thread import *
import pickle
from settings import ip, port
import threading

# Define id_count as a global variable (it keeps track of the currently new joined clients)
id_count = 0


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.port_handler = 0
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = set()
        self.games = {}
        self.locks = {}  # Dictionary to store locks for each game_id

    def run(self):
        global id_count

        try:
            self.s.bind((self.ip, self.port))
        except socket.error as e:
            print(str(e))

        self.s.listen(2)
        print("Waiting for a connection... Server started")

        while True:
            conn, addr = self.s.accept()
            print("Connection made to {}".format(addr))

            id_count += 1
            game_id = (id_count - 1) // 2
            print("A new client of name:", f"{game_id}/{(id_count+1) % 2}")
            print("THE ID_COUNT IS : ", id_count)

            if id_count % 4 == 0:
                self.port_handler += 1
                # This condition assigns a single server to each 4 clients (one server per two games)
                print("NOW A NEW SERVER IS BEING INSTANTIATED")
                new_server = Server(self.ip, (self.port + self.port_handler))
                start_new_thread(
                    new_server.run, ()
                )  # Start the new server instance in a new thread

            current_player = 0

            if id_count % 2 == 1:
                self.locks[game_id] = threading.Lock()  # Create a lock for this game_id
                self.locks[game_id].acquire()  # Acquire lock before accessing game data
                self.games[game_id] = Game(game_id)
                self.locks[game_id].release()  # Release lock after accessing game data
                print("Created a new game of id: ", game_id)
            else:
                self.locks[game_id].acquire()  # Acquire lock before accessing game data
                self.games[game_id].ready = True
                self.locks[game_id].release()  # Release lock after accessing game data
                current_player = 1

            start_new_thread(self.threaded_client, (conn, current_player, game_id))

    def threaded_client(self, conn, player, game_id):
        conn.send(str.encode(str(player)))

        while True:
            try:
                data = conn.recv(4096).decode()
                if game_id in self.games:
                    self.locks[
                        game_id
                    ].acquire()  # Acquire lock before accessing game data
                    game = self.games[game_id]
                    if not data:
                        self.locks[game_id].release()  # Release lock if no data
                        break
                    else:
                        if data == "soft-reset":
                            game.softreset()
                        elif data == "hard-reset":
                            game.hardreset()
                        elif data == "find-winner":
                            game.winner()
                        elif data != "get":
                            print("Data: ", data)
                            game.play(player, data)
                    conn.sendall(pickle.dumps(game))
                    self.locks[
                        game_id
                    ].release()  # Release lock after accessing game data
                else:
                    break
            except:
                break

        print("Lost connection with server")
        try:
            self.locks[game_id].acquire()  # Acquire lock before accessing game data
            del self.games[game_id]
            self.locks[game_id].release()  # Release lock after accessing game data
            del self.locks[game_id]  # Remove lock for this game_id
            print("Closing game", game_id)
        except:
            pass
        conn.close()


if __name__ == "__main__":
    server = Server(ip, port)
    server.run()
