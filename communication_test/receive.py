

# Machine B: TCP Forwarder
import socket

def machine_b(listen_port, forward_ip, forward_port):
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.bind(('0.0.0.0', listen_port))
    receiver_socket.listen(1)

    print(f"Machine B: Listening on port {listen_port}...")

    conn, addr = receiver_socket.accept()
    print(f"Connected by: {addr}")

    while True:
        # 接收来自 Machine A 的数据
        data = conn.recv(1024)
        if not data:
            break
        print(f"Received: {data} from {addr}")

        # 回传数据给 Machine A
        conn.send(1)

    print("Machine B: Connection closed.")
    conn.close()
    receiver_socket.close()

if __name__ == "__main__":
    Sender_IP = '192.168.3.80'  # Machine A IP
    machine_b(listen_port=6050, forward_ip=Sender_IP, forward_port=5060)
