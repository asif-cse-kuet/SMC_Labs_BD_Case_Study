# SMC Labs BD Case Study: Distributed P2P Task Execution System

This repository contains two implementations of a distributed peer-to-peer (P2P) task execution system. The system is designed to handle tasks across multiple nodes in a specified order, with each node responsible for a specific type of task.

- **Version 1**: Uses Python’s `socket` and `threading` libraries for basic P2P communication.
- **Version 2**: Uses `libp2p` to enable advanced P2P features such as secure channels, peer discovery, and multi-protocol support.

## Features

- **Node Discovery**: Each node discovers other nodes running the same application and registers them.
- **Connection Management**: Establishes connections to required nodes based on task type.
- **Task Execution**: Executes tasks across nodes in the order specified by the user.
- **Connection Termination**: Cleanly disconnects from peers after task completion.

## Requirements

- Python 3.x
- Required packages for each version:
  - **Version 1 (Socket-Based)**: No external dependencies, uses Python standard libraries (`socket`, `threading`, `json`, `time`).
  - **Version 2 (libp2p-Based)**: Requires `libp2p` and `multiaddr` libraries.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

### 2. Verify Python Installation
Ensure Python 3.x is installed:
```bash
python3 --version
```
If not installed, download it from [Python.org.](https://www.python.org/downloads/)

### 3. Create a tasks.txt File
Create a tasks.txt file in the same directory with task details listed in the order they should be executed. Each task should have a unique type and identifier (e.g., a1 a2 c1 b1 c2), where the letter indicates the task type, and the number is the task ID. Here’s an example:
```bash
a1 a2 c1 b1 c2 a3 b2 b3 a4 c3 b4
```

### 4: Choose a Version
Select the version you’d like to use and follow the specific setup instructions below.

### **Version 1: Socket-Based P2P System**
This version uses Python’s socket and threading libraries to create a basic P2P system. No additional dependencies are required.

**Installation for Version 1**
No external packages are needed, as this version relies on Python’s standard libraries.

**Running Version 1**
 *1.Ensure tasks.txt is in the current directory.*
 *2.Run the program using:*
  ```bash
  python3 node_socket.py
  ```
**Execution Workflow (Socket-Based)**
 1. The program reads tasks from tasks.txt and determines the required task types.
 2. It initiates peer discovery to find nodes capable of handling each task type.
 3. Tasks are assigned and executed across nodes in the specified order.
 4. Connections are terminated after task completion.

### **Version 2: libp2p-Based P2P System**
This version uses libp2p to enable advanced P2P functionality, including multi-protocol support, peer discovery, and secure channels.

**Installation for Version 2**
Install the required libp2p and multiaddr libraries:
```bash
pip install libp2p multiaddr
```
**Running Version 2**
  1. Ensure tasks.txt is in the current directory.
  2. Start the node with:
  ```bash
  python3 node_libp2p.py
  ```
  3. Note: You will need to replace "<peer_id>" in the code with the actual peer ID of another node you want to connect to for discovery.
**Execution Workflow (libp2p-Based)**
  1. The program reads tasks from tasks.txt and determines the required task types.
  2. It initiates peer discovery through libp2p’s discovery protocol to find nodes capable of handling each task type.
  3. Tasks are assigned and executed across nodes in the specified order.
  4. Connections are gracefully terminated after task completion.

### **Usage Example**
Suppose you have the following tasks.txt file:
```bash
a1 a2 c1 b1 c2 a3 b2 b3 a4 c3 b4
```
**Running Version 1**
Run the program with the following command:
```bash
python3 node_socket.py
```
**Running Version 2**
Run the program with the following command:
```bash
python3 node_libp2p.py
```
Both versions will execute tasks in the specified order, discover necessary peers, establish connections, and display task execution statuses in the console.

### Example Console Output
Example output during execution:
```bash
Discovering peers...
Initiating connections...
Assigning tasks...
Executing task: a1
Executing task: a2
...
Task completed by peer handling type 'B'
Terminating connections...
Disconnected from all nodes.
```

### Troubleshooting
**Common Issues :**
  1. Port Conflicts: Ensure no other services are using the same ports defined in the code. Modify port values if necessary.
  2. Network Firewall: If nodes are on different machines, ensure the firewall allows traffic over the specified ports.
  3. Peer Discovery: For libp2p version, replace "<peer_id>" in the code with actual peer IDs for effective peer discovery.

### Updating the Code
To update the code, pull the latest changes from the repository:
```bash
git pull origin main
```

### Future Enhancements
Integration with libp2p for more features in the socket version.
Improved error handling and retry mechanisms for increased network reliability.
Enhanced logging for detailed insights into each node’s operations.
Dynamic load balancing and task reallocation among nodes.
Real-time monitoring of task status across the distributed network.
