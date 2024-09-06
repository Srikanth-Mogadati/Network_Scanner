# Port Scanner

## Description

This Port Scanner is a Python-based tool that allows users to scan a range of ports on a specified IP address. It utilizes the Scapy library for packet manipulation and the tqdm library for progress visualization. The scanner identifies open and closed ports and provides information about the services running on open ports.

## Features

- Scan a user-specified range of ports on a given IP address
- Identify open and closed ports
- Display service names for open ports
- Show progress bars for both scanning and result display
- Provide a summary of open and closed ports

## Requirements

- Python 3.6+
- Scapy
- tqdm
- socket (built-in Python module)

## Installation

1. Clone this repository or download the script.
2. Install the required packages:


2. When prompted, enter the target IP address.
3. Enter the port range you wish to scan in the format "start-end" (e.g., "1-1000").
4. The script will display a progress bar as it scans the specified ports.
5. After scanning, it will show another progress bar while displaying the results.
6. The results will include:
   - A list of open ports with their corresponding services
   - A list of closed ports
   - A summary of all scanned ports
