# Python_Projects
# Port Scanner

## Description

This Python script serves as a basic port scanner tool. It allows users to specify a target IP address and scans a range of ports (from 20 to 100 by default) to determine which ports are open on the target system.

## Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of networking concepts.

## Usage

1. Clone the repository or download the `port_scanner.py` file.
2. Open a terminal.
3. Navigate to the directory where `port_scanner.py` is located.
4. Run the script with the following command:

python3 port_scanner.py <ip>


Replace `<ip>` with the IP address of the target system.

## Code Explanation

This Python script serves as a basic port scanner tool. Below is an explanation of how the code works:

- The script first imports necessary modules: `sys`, `socket`, and `datetime`.
- It checks the command-line arguments to ensure the correct number of arguments is provided. If not, it displays a usage message.
- The script resolves the IP address of the target host using `socket.gethostbyname()` function.
- It then prints a banner displaying the target IP address and the current time.
- Inside a try-except block, the script iterates over a range of ports (from 20 to 100 by default).
- For each port, it creates a TCP socket using `socket.socket()` function.
- It sets a default timeout for the socket using `socket.setdefaulttimeout()` function.
- The script attempts to establish a connection with the target host and port using `socket.connect_ex()` function.
- If the connection attempt is successful (result equals 0), it prints a message indicating that the port is open.
- Finally, the socket is closed.
- The script handles exceptions such as keyboard interrupts, hostname resolution errors, and socket errors gracefully.

## Disclaimer

This script is intended for educational and testing purposes only. It should only be used on systems for which you have explicit permission to perform port scanning. Unauthorized port scanning may be illegal and could result in severe consequences.

## Author

Nithin Kumar

