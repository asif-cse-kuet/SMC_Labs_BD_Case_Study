import socket
import threading
import json
import time
import re

# Constants for message types
DISCOVERY_REQUEST = "DISCOVERY_REQUEST"
DISCOVERY_RESPONSE = "DISCOVERY_RESPONSE"
CONNECT_REQUEST = "CONNECT_REQUEST"
CONNECT_ACK = "CONNECT_ACK"
TASK_ASSIGN = "TASK_ASSIGN"
TASK_COMPLETE = "TASK_COMPLETE"
DISCONNECT_REQUEST = "DISCONNECT_REQUEST"
DISCONNECT_ACK = "DISCONNECT_ACK"

# Node class to handle peer-to-peer networking
class Node:
    def __init__(self, ip, port, task_type):
        self.ip = ip
        self.port = port
        self.task_type = task_type  # Type of task this node can handle (e.g., 'A', 'B', 'C')
        self.peers = {}  # Dictionary to store connected peers by task type
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip, self.port))
        self.lock = threading.Lock()

    # Function to broadcast discovery requests
    def broadcast_discovery(self):
        message = json.dumps({"type": DISCOVERY_REQUEST, "task_type": self.task_type})
        self.socket.sendto(message.encode(), ('<broadcast>', self.port))

    # Function to handle incoming messages
    def handle_incoming(self):
        while True:
            data, addr = self.socket.recvfrom(1024)
            message = json.loads(data.decode())
            msg_type = message.get("type")

            if msg_type == DISCOVERY_REQUEST:
                self.handle_discovery_request(addr, message)
            elif msg_type == DISCOVERY_RESPONSE:
                self.handle_discovery_response(addr, message)
            elif msg_type == CONNECT_REQUEST:
                self.handle_connect_request(addr)
            elif msg_type == CONNECT_ACK:
                self.handle_connect_ack(addr)
            elif msg_type == TASK_ASSIGN:
                self.handle_task_assign(addr, message)
            elif msg_type == TASK_COMPLETE:
                self.handle_task_complete(addr, message)
            elif msg_type == DISCONNECT_REQUEST:
                self.handle_disconnect_request(addr)
            elif msg_type == DISCONNECT_ACK:
                self.handle_disconnect_ack(addr)

    # Function to handle incoming discovery requests
    def handle_discovery_request(self, addr, message):
        task_type = message.get("task_type")
        if task_type == self.task_type:
            response = json.dumps({"type": DISCOVERY_RESPONSE, "ip": self.ip, "port": self.port, "task_type": self.task_type})
            self.socket.sendto(response.encode(), addr)

    # Function to handle incoming discovery responses
    def handle_discovery_response(self, addr, message):
        task_type = message.get("task_type")
        if task_type not in self.peers:
            self.peers[task_type] = addr

    # Function to handle incoming connection requests
    def handle_connect_request(self, addr):
        ack_message = json.dumps({"type": CONNECT_ACK})
        self.socket.sendto(ack_message.encode(), addr)

    # Function to handle incoming connection acknowledgments
    def handle_connect_ack(self, addr):
        print(f"Connected to {addr}")

    # Function to handle task assignments
    def handle_task_assign(self, addr, message):
        task_data = message.get("task_data")
        print(f"Executing task: {task_data}")
        # Simulate task completion
        time.sleep(2)
        complete_message = json.dumps({"type": TASK_COMPLETE, "task_type": self.task_type})
        self.socket.sendto(complete_message.encode(), addr)

    # Function to handle task completion notifications
    def handle_task_complete(self, addr, message):
        print(f"Task completed by {addr}")

    # Function to handle incoming disconnect requests
    def handle_disconnect_request(self, addr):
        ack_message = json.dumps({"type": DISCONNECT_ACK})
        self.socket.sendto(ack_message.encode(), addr)

    # Function to handle disconnect acknowledgments
    def handle_disconnect_ack(self, addr):
        print(f"Disconnected from {addr}")

    # Function to initiate a connection with peers based on required task types
    def initiate_connection(self, required_task_types):
        for task_type in required_task_types:
            if task_type in self.peers:
                peer_addr = self.peers[task_type]
                connect_message = json.dumps({"type": CONNECT_REQUEST})
                self.socket.sendto(connect_message.encode(), peer_addr)

    # Function to assign tasks to connected nodes
    def assign_task(self, task_type, task_data):
        if task_type in self.peers:
            peer_addr = self.peers[task_type]
            task_message = json.dumps({"type": TASK_ASSIGN, "task_data": task_data})
            self.socket.sendto(task_message.encode(), peer_addr)

    # Function to disconnect from peers after task completion
    def terminate_connection(self):
        for task_type, addr in self.peers.items():
            disconnect_message = json.dumps({"type": DISCONNECT_REQUEST})
            self.socket.sendto(disconnect_message.encode(), addr)

# Helper function to load tasks from a text file and parse required nodes
def load_tasks_from_file(filename):
    with open(filename, 'r') as file:
        task_list = file.read().strip().split()

    task_order = []
    task_count = {}

    # Parse tasks from file content
    for task in task_list:
        task_type = task[0]  # First letter of task indicates the type
        task_order.append((task_type, task))
        task_count[task_type] = task_count.get(task_type, 0) + 1

    # Identify required task types (types with counts greater than 1)
    required_task_types = [task_type for task_type, count in task_count.items() if count > 1]

    return task_order, required_task_types

# Helper function to start node operation
def start_node(ip, port, task_type, required_task_types, tasks):
    node = Node(ip, port, task_type)
    threading.Thread(target=node.handle_incoming).start()

    # Step 1: Discover peers
    print("Discovering peers...")
    node.broadcast_discovery()
    time.sleep(2)  # Wait for discovery responses

    # Step 2: Initiate connections with required peers
    print("Initiating connections...")
    node.initiate_connection(required_task_types)
    time.sleep(1)  # Wait for connection acknowledgments

    # Step 3: Assign tasks in order
    print("Assigning tasks...")
    for task_type, task_data in tasks:
        node.assign_task(task_type, task_data)
        time.sleep(3)  # Allow some time for task completion

    # Step 4: Terminate connections
    print("Terminating connections...")
    node.terminate_connection()

# Main function to set up and run the P2P node
if __name__ == "__main__":
    ip = "127.0.0.1"
    port = 5000
    task_type = "A"  # Assume this node handles 'A' type tasks

    # Load tasks and determine required nodes from the file
    tasks, required_task_types = load_tasks_from_file("tasks.txt")

    # Start the node with the loaded tasks and required peer types
    start_node(ip, port, task_type, required_task_types, tasks)
