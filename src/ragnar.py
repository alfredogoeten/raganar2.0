'''
	Project Ragnar
		Program for Penetration test on IoT devices.
'''
#!/usr/bin/python
import sys
import webI
import netServ
import transCrypt
import mrBin
from utils import clear


def _(s): return s

# Main Menu and submodules definition
menuOpts = {0: 'exit', 1: 'webI', 2: 'netServ', 3: 'transCrypt', 4: 'mrBin'}
print(_('Escolha o Modulo a ser executado'))
subModule = {'exit': sys.exit,
             'webI': webI.webIMenu, 		# Submodule of Web Interface tests
             'netServ': netServ.netServMenu, 		# Submodule of Web Interface tests
             'transCrypt': transCrypt.transCryptMenu,
             'mrBin': mrBin.mrBinMenu            
             }
# Selection of the module
while True:
    # Clean the screen
    clear()
    opt = int(raw_input(
        _("0 - Fechar o Programa\n1 - Interface Web \n2 - Rede \n3 - Criptografia \n4 - Firmware \n")))
    if opt == 0:
        sys.exit()
    if opt in menuOpts:
        subModule[menuOpts[opt]]()
    else:
        print _('Escolha invalida')
