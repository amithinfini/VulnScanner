import portscanner

targets_ip = input('[+] Enter Target To Scan For Vulnerable Open Ports: ')
port_number = int(input('[+] Enter Number Of Ports To Scan(500 - first 500 ports): '))
vul_file = input('[+] Enter the path to File with Vulnerability Software: ')
print('\n')

target = portscanner.PortScan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "' + banner + '" ON PORT ' + str(target.open_ports[count]))
        count += 1