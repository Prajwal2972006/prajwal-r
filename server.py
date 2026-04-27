import socket
import ssl

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 5000

leaderboard = {}

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Server running on port", PORT)

with context.wrap_socket(server_socket, server_side=True) as secure_server:
    while True:
        conn, addr = secure_server.accept()
        print("Client connected:", addr)

        data = conn.recv(1024).decode()

        if data:
            name, score = data.split(",")
            score = int(score)

            leaderboard[name] = score

            sorted_board = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)

            response = "\nLeaderboard:\n"
            for player, sc in sorted_board:
                response += f"{player} : {sc}\n"

            conn.send(response.encode())

        conn.close()