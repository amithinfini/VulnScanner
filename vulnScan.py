import portscanner

targets_ip = input('[+] Enter Target To Scan For Vulnerable Open Ports: ')
port_number = int(input('[+] Enter Number Of Ports To Scan(500 - first 500 ports): '))
vul_file = input('[+] Enter the path to File with Vulnerability Software: ')

portscanner.scan(targets_ip)