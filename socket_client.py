def socket_client():
    import socket
    HOST = '192.168.1.35'
    PORT = 8001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True:

        str ="Please input msg:"
        cmd = str.encode('utf-8')
        s.send(cmd)
        data = s.recv(1024)
        print(data)

        #s.close()


socket_client()
