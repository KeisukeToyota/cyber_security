import socket

target_host = '0.0.0.0'
target_port = 9999

# ソケットオブジェクトの作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# サーバーへの接続
client.connect((target_host, target_port))

# データの送信
client.send(b'Hello World!!')

# データの受信
response = client.recv(4096)

print(response)
