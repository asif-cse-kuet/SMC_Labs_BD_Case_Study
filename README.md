# SMC_Labs_BD_Case_Stud

This repository contains a Python-based implementation of a peer-to-peer (P2P) protocol for distributed task execution across multiple nodes. Each node in the system is capable of discovering other nodes, establishing connections, communicating assigned tasks in sequence, and disconnecting after completing the tasks.

## Features

- **Node Discovery**: Identify nodes running the same application and available for task execution.
- **Connection Management**: Establish and terminate connections with peer nodes based on task requirements.
- **Task Execution**: Execute tasks across nodes in a user-defined order.
- **Connection Termination**: Gracefully terminate connections after task completion.

## Requirements

- Python 3.x
- Packages:
  - `socket` (Standard Library)
  - `threading` (Standard Library)
  - `json` (Standard Library)
  - `time` (Standard Library)
  
## Installation and Setup

### 1. Clone the Repository

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

### 4. Install Required Packages
The required libraries (socket, threading, json, time) are included in Python’s standard library, so no external installation is necessary.

### 5. Run the Program
To start the node, use the following command:
```bash
python3 node.py
```

### 6. Execution Workflow
*1. The program will read tasks from the tasks.txt file and determine the required task types.*
*2. It will then initiate discovery to find other nodes capable of performing different task types.*
*3. Tasks are assigned and executed across nodes in the specified order.*
*4. Once all tasks are complete, connections to all nodes are terminated.*

### Usage Example
Suppose you have the following tasks.txt file:
```bash
a1 a2 c1 b1 c2 a3 b2 b3 a4 c3 b4
```
You would initiate the program with:
```bash
python3 node.py
```
The program will then:
 1. Discover available nodes capable of handling each task type (A, B, C).
 2. Establish a connection with each node and assign tasks in the specified order.
 3. Output task execution status to the console.
 4. Terminate connections upon task completion.

### Example Output
Example console output during execution:
```bash
Discovering peers...
Initiating connections...
Assigning tasks...
Executing task: a1
Executing task: a2
...
Task completed by node handling type 'B'
Terminating connections...
Disconnected from all nodes.
```
## Troubleshooting

### Common Issues

1. **Port Conflicts**: Ensure no other services are using the same ports defined in the code.
   - Modify the port values in the code if conflicts occur.

2. **Network Firewall**: If nodes are on different machines, ensure the firewall allows traffic over the specified ports.

### Updating the Code

To update the code, pull the latest changes from the repository:

```bash
git pull origin main
```

### Future Enhancements

- Integration with `libp2p` for more robust P2P capabilities, including automatic peer discovery and secure channels.
- Improved error handling and retry mechanisms for increased network reliability and resilience.
- Enhanced logging for detailed insights into each node’s operations, including task execution status and connection lifecycle.
- Support for dynamic node addition and removal, allowing nodes to join and leave the network seamlessly without disrupting ongoing tasks.
- Load balancing among nodes based on task complexity or resource availability to optimize performance.

