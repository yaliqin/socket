def socket_server():
    import socket
    import time

    HOST = '192.168.1.35'
    PORT = 8001

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print('Server start at: %s:%s' %(HOST, PORT))
    print('wait for connection...')

    while True:
        conn, addr = s.accept()
        print('Connected by '+addr[0])

        while True:
            data = conn.recv(1024)
            print(data)
            str ="server received you message."
            b = str.encode('utf-8')
            conn.send(b)
            time.sleep(15.0)

        #conn.close()

socket_server()
