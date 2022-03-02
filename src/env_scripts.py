import os

commands = ['sudo apt-get remove -y python3',
            'sudo apt install -y python2',
            'sudo apt install -y python-pip',
            'sudo apt-get install -y python2-dev',
            'sudo apt-get install -y libssl-dev libffi-dev',
            'sudo apt-get install -y libmagic1',
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