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

langSelec = {'en': 'English selected', 'pt': 'Portugues selecionado'}

# Basic definitions for the program
menuOpts = {0: 'exit', 1: 'webI', 2: 'netServ'}
langOpts = {'en', 'pt'}

'''
	Main Class of the program, coordinate all penetration tests
	using the other modules. It's the core of the software.
'''

'''
	If the module is called with 'python ragnar.py', this tests are executed.
'''
# Language Selection
while True:
    lang = raw_input("'pt' - Portugues\n'en' - English\n")
    if lang in langOpts:
        print(langSelec[lang])
        break

# Change the software language
if lang == 'pt':
    def _(s): return s
else:
    lg = gettext.translation('ragnar', localedir='locale', languages=[lang])
    lg.install()

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
