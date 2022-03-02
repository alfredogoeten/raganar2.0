# Ragnar2
Penetration Testing Tool for Internet of Things Devices.  

More friendly, easy to run and improved version of the original [Ragnar](https://github.com/imperador/ragnar).

## Run
    1. Clone this repo
    2. sudo su
    3. sudo apt-get update
    4. Run 'env_scripts.py' for dependencies
    5. Run 'ragnar.py'
## Modules
### Web Interface (WebI)
  
Performs penetration testing by:
 - Establishing connections with provided interfaces;
 - Tests the interface and collects necessary data;
 - Analysing the field x-frame-options for Clickjacking;
 - Scans for standard login pages and analyses their code;
 - Tries to insert encoded SQL queries into the URLs and each detected field;
   - Allows manual addition of paths ;
   - Tries to generate any Database-ManagementSystem (DBMS) response \cite{su2006essence};
 - Performs a recursive search for paths and form fields;
   - Covers both persistent and reflected XSS attempts;
 - For each path and field, attempts to insert javascript strings;
   - Uses several encodings to avoid dynamic detection filtering;
 - Uses a technique known as ACK scan to bypass and detect any existing Web Application Firewall (WAF).

### Network Service (netServ)

Penetration testing routine: 
 - Checks for open ports and available services detection;
   - Applies an SYN scan approach ;
   - Can also recognise WAF presence;
 - Performs randomly-generated Fuzzing attacks on all identified services ;
 - Performs directed Fuzzing attacks on well-known ports.

### Cryptography (transCrypt)
Runs analysis focusing on security protocols used to establish encrypted links between the server and client.

Testing Routine:
 - Outlines allowed security protocols;
 - Verifies the default protocol used by the server;
   - Classifying its cypher suite and provided bits of security; 
 - Checks the use of Perfect Forward Secrecy and used cyphers.

### Firmware (mrBin)

Checks for vulnerabilities on firmware files.

- Verify MD5 signature;
- Find printable strings on bin file;
- Dumphex data from the bin file;
- File system extraction.

## Developer
Cristoffer Leite

GitHub: @imperador

## Referencing this work

#### \[2019\] Pentest on Internet of Things Devices
*Cristoffer Leite, João Gondim, Priscila Solis, Marcos Caetano and Eduardo Alchieri*
<br/> XLV LATIN AMERICAN COMPUTING CONFERENCE (CLEI 2019), 2019
<br/>[\[pdf\]](http://clei2019.utp.ac.pa/storage/app/uploads/public/5d8/cff/bd1/5d8cffbd16f09903219768.pdf) \[bib\]

#### \[2017\] Ragnar: Ferramenta para Pentest em dispositivos da Internet das Coisas
*Cristoffer Leite da Silva*
<br/> Universidade de Brasılia, 2017
<br/>[\[pdf\]](http://bdm.unb.br/bitstream/10483/19824/1/2017_CristofferLeiteDaSilva_tcc.pdf) \[bib\]

