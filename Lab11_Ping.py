"""
Author: Raymond Llamas
Course: PCC - CIS188 - Scripting for Automation
Instructor: P. Farmer
Description:
This program reads IP addresses from a CSV file and sends an email with their ping times.
It performs the following tasks:
1. Reads IP addresses from the provided 'ip.csv' file.
2. Pings each IP address and collects the ping times.
3. Sends an email containing the ping results.

"""

from ping3 import ping
import ezgmail
import csv

# Initialize ezgmail
ezgmail.init()

# Open and read the IP addresses from the CSV file
ipFile = open('ip.csv')
ipReader = csv.DictReader(ipFile)
msg = "Ping results:\n\n"

# Ping each IP address and store the results
for row in ipReader:
    ip = row['ip']
    ping_time = ping(ip)
    if ping_time is not None:
        ping_time = round(ping_time * 1000, 2)  # Convert to milliseconds and round
        msg += f"IP: {ip}, Ping Time: {ping_time} ms\n"
    else:
        msg += f"IP: {ip}, Ping Time: Request timed out\n"

# Close the CSV file
ipFile.close()

# Send an email with the ping results
ezgmail.send('rllamas2@mail.pima.edu', 'Daily Ping Report', msg)
