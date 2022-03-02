'''
	Project Ragnar
		Program for Penetration test on IoT devices.
'''
#!/usr/bin/python
import sys
import gettext
import webI
import netServ
from utils import clear



# Basic definitions for the program
menuOpts = {0: 'exit', 1: 'webI', 2: 'netServ'}


'''
	Main Class of the program, coordinate all penetration tests
	using the other modules. It's the core of the software.
'''

'''
	If the module is called with 'python ragnar.py', this tests are executed.
'''

# Change the software language
lang = 'en'
def _(s): return s

# Main Menu and submodules definition
print(_('Escolha o Modulo a ser executado'))
subModule = {'exit': sys.exit, 	# Close the program
             'webI': webI.webIMenu, 		# Submodule of Web Interface tests
                                'netServ': netServ.netServMenu, 		# Submodule of Web Interface tests
             }
# Selection of the module
while True:
    # Clean the screen
    clear()
    opt = int(raw_input(
        _("0 - Fechar o Programa\n1 - Interface Web \n2 - Servicos de Rede\n")))
    if opt == 0:
        sys.exit()
    if opt in menuOpts:
        subModule[menuOpts[opt]](lang)
    else:
        print _('Escolha invalida')
