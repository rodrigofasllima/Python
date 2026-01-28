# portTest.py
# 1. Purpose
This Python script aims to check whether specific network hosts are online and, if so, perform a TCP port scan to identify which ports are open or closed.
It uses the ping3 library to check host availability and the native socket module to test TCP connections.

# 2. Dependencies
- Python 3.x
- External library:
  - ping3 (for ICMP ping)

Install ping3:
pip install ping3

# 3. Code Structure

3.1 Function online(target)
Input: IP address or hostname (target).
Process: sends a ping using ping3.
Output: True if the host responds, False otherwise.

# 3.2 Function scan_port(target, port)
Input:
  - target: IP address of the host.
  - port: TCP port number to test.
Process:
  - Creates a TCP socket.
  - Attempts to connect to the host on the specified port.
  - Returns True if the connection is successful (port is open).
Output:
  - True → port is open.
  - False → port is closed or error occurred.

# 3.3 Port List
Defines a set of ports to be checked:
  - 22 → SSH
  - 23 → Telnet
  - 53 → DNS
  - 80 → HTTP
  - 1315 → Custom port
  - 179 → BGP

# 3.4 Main Loop
IP Iteration:
  - Generates addresses from 8.8.3.3 to 8.8.8.8.
Verification:
  - First checks if the host is online.
  - If online, scans the list of ports to check if they are open or closed.
Output:
  - Colored terminal output:
    - Blue → IP being tested.
    - Green → Port open.
    - Red → Port closed.
    - Yellow → Host offline.

# 4. Sample Output
Procurando em 8.8.3.3
                [OFFLIN]
Procurando em 8.8.3.4
    conexão TCP porta 22    [CLOSED]
    conexão TCP porta 23    [CLOSED]
    conexão TCP porta 53    [ OPEN ]

# 5. Possible Improvements
- Add multithreading to speed up scanning.
- Allow dynamic input of IPs and ports via command-line arguments.
- Export results to a CSV or JSON file.
- Implement more detailed exception handling.
