# Machine A: TCP Sender
import socket
import time
import random
def machine_a(sender_port, receiver_ip, receiver_port):
    sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sender_socket.bind(('0.0.0.0', sender_port))
    
    print(f"Machine A: Connecting to Machine B at {receiver_ip}:{receiver_port}...")
    sender_socket.connect((receiver_ip, receiver_port))

    def generate_payload(length):
        return bytes(random.getrandbits(8) for _ in range(length))
    payload_length = 1024  # 调整此值设置字节长度
    payload = generate_payload(payload_length)
    value = 1
    while value <= 5:
        start_time = time.time()

        # 发送数据到 Machine B
        sender_socket.send(payload)
        print(f"Sent: {payload_length}")

        # 接收 Machine B 的回传数据
        data = sender_socket.recv(1024)
        end_time = time.time()

        print(f"Received: {data} (Round Trip Time: {end_time - start_time:.6f} s)")

        value += 1
        time.sleep(1)  # 延迟 1 秒，防止过快发送

    print("Machine A: Transmission completed.")
    sender_socket.close()

if __name__ == "__main__":
    Receiver_IP = '192.168.3.9'  # Machine B IP
    machine_a(sender_port=5060, receiver_ip=Receiver_IP, receiver_port=6050)
