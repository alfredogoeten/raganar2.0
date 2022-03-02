import os

commands = ['sudo apt-get remove python3 -f',
            'sudo apt install python2 -f',
            'sudo apt install python-pip -f',
            'sudo apt-get install python2-dev -f',
            'sudo apt-get install libssl-dev libffi-dev -f',
            'sudo apt-get install libmagic1 -f',
            'pip2 install mechanize',
            'pip2 install scapy==2.3.3',
            'pip2 install uefi_firmware',
            'pip2 install beatifulsoup4',
            'pip2 install netifaces',
            'pip2 install backports.ssl_match_hostname',
            'pip2 install cryptography',
            'pip2 install python-magic']


for command in commands:
    os.system(command)