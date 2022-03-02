import subprocess

commands = ['sudo apt-get remove python3',
            'sudo apt install python2',
            'sudo apt install python-pip',
            'sudo apt-get install python2-dev',
            'sudo apt-get install libssl-dev libffi-dev',
            'sudo apt-get install libmagic1'
            'pip2 install mechanize',
            'pip2 install scapy==2.3.3',
            'pip2 install uefi_firmware',
            'pip2 install beatifulsoup4',
            'pip2 install netifaces',
            'pip2 install backports.ssl_match_hostname',
            'pip2 install cryptography',
            'pip2 install python-magic']


process = subprocess.Popen(
    '/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
out, err = process.communicate(commands.encode('utf-8'))
print(out.decode('utf-8'))
