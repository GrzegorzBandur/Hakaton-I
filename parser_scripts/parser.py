#!/usr/bin/env python

import re
import pickle

licencje = {
    'freeware': 'freeware',
    'design science license': 'design science license',
    'public domain': 'public domain',
    'domena publiczna': 'public domain',
    'domeny publicznej': 'public domain',
    'x11 license': 'mit licences',
    'mit license': 'mit licences',
    'gnu gpl': 'gnu gpl',
    'gpl': 'gnu gpl',
    'general public license': 'gnu gpl',
    'guile': 'gnu gpl',
    'lgpl': 'gnu lgpl',
    'gnu lgpl': 'gnu lgpl',
    'gnu lesser general public license': 'gnu lgpl',
    'gnu free documentation license': 'gnu fdl',
    'gnu fdl': 'gnu fdl',
    'gfdl': 'gnu fdl',
    'creative commons': 'creative commons',
    'commons creative': 'creative commons',
    'cc0': 'creative commons',
    'cc-0': 'creative commons',
    'cc-by': 'creative commons',
    'cc by': 'creative commons',
    'cc-by-nc': 'creative commons',
    'bsdl': 'berkeley software distribution license',
    'free art license': 'free art license',
    'licencja wolnej sztuki': 'free art license',
    'rscpl': 'ricoh source code public license',
    'agpl': 'affero general public license',
    'affero gpl': 'affero general public license',
    'apache license': 'apache software license',
    'apache software license': 'apache software license',
    'ms-pl': 'microsoft public license',
    'microsoft public license': 'microsoft public license',
    'ms-rl': 'microsoft reciprocal license',
    'copyleft': 'copyleft',
    'open database license': 'open database license',
    'odbl': 'open database license',
    'artistic license': 'artistic license',
    'european union public licence': 'european union public licence',
    'eupl': 'european union public licence',
    'common public license': 'common public license',
    'eclipse public license': 'eclipse public license',
    'cecill': 'cea cnrs inria logiciel libre',
    'intel open source license': 'intel open source license',
    'freebsd documentation license': 'freebsd documentation license',
    'w3c software notice and license': 'w3c software notice and license',
    'python software foundation license': 'python software foundation license',
    'python license': 'python software foundation license',
    'apple public source license': 'apple public source license',
    'apsl': 'apple public source license',
    'boost software license': 'boost software license',
    'beerware': 'beerware',
    'wtfpl': 'do what the fuck you want to public license',
    'cddl': 'common development and distribution license',
    'ibm public license': 'ibm public license',
    'latex project public license': 'latex project public license',
    'lppl': 'latex project public license',
    'openssl license': 'openssl license',
    'php license': 'php license',
    'netscape public license': 'netscape public license',
    'open software license': 'open software license',
    'academic free license': 'academic free license',
    'sleepycat license': 'sleepycat public license',
    'code project open license': 'code project open license',
    'cpol': 'code project open license',
    'cryptix general license': 'cryptix general license',
    'educational community license': 'educational community license',
    'eiffel forum license': 'eiffel forum license',
    'fair license': 'fair license',
    'hacktivismo enhanced-source software license agreement': 'hacktivismo enhanced-source software license agreement',
    'hessla': 'hacktivismo enhanced-source software license agreement',
    'isc license': 'isc license',
    'opac free public license': 'opac free public license',
    'ofpl': 'opac free public license',
    'sun industry standards source license': 'sun industry standards source license',
    'sissl': 'sun industry standards source license',
    'zope public license': 'zope public license',
    'zlib license': 'zlib license',
    'xcore open source licenses': 'xcore open source licenses',
    'q public license': 'q public license'
}

licencje_njdz = {
    'fal': 'free art license',
    'psfl': 'python software foundation license',
    'cpl ': 'common public license',
    'epl': 'eclipse public license',
    'ipl': 'ibm public license',
    'npl': 'netscape public license',
    'osl': 'open software license',
    'afl': 'academic free license',
    'ecl': 'educational community license',
    'efl': 'eiffel forum license',
    'mit': 'mit licences',
    'cc': 'creative commons',
    'bsd': 'berkeley software distribution license',
    'lal': 'licence art libre',
    'asl': 'apache software license',
    'mpl': 'mozilla public license',
    'spl': 'sun public license',
    'qpl': 'q public license'
}

tagi = [r'^Recno:: ([0-9]+)$', r'^URL:: (.*)$', r'^ParseText::$', r'^Content::$', r'^Version: (-?[0-9]+)$', r'^url: (.*)$', r'^base: (.*)$', r'^contentType: (.*)$', r'^metadata: (.*)$', r'^Content:$']

#nutch = file(r'../../../all/all(excluded deviantart).txt')
nutch = file(r'../../../all/deviantart.txt')
dane = [{'id':'start'}]
status = ''

for linia in nutch:
    #print linia
    if re.match(tagi[0], linia):
        #print '-------------nowa strona-------------'
        for klucz in licencje.iterkeys():
            if klucz in dane[-1].get('text', '').lower():
                dane[-1]['license'] = licencje[klucz]
                print dane[-1]['id'], licencje[klucz]
                break
        if not 'license' in dane[-1]:
            for klucz in licencje_njdz.iterkeys():
                if ('licen' in dane[-1].get('text', '').lower()) and (klucz in dane[-1].get('text', '').lower()):
                    dane[-1]['license'] = licencje_njdz[klucz]
                    print dane[-1]['id'], licencje_njdz[klucz]
                    break
        if not 'license' in dane[-1]:
            #print 'BRAK LICENCJI', dane[-1]['id']
            dane.pop()
        status = ''
        dane.append({})
        #dane[-1]['recno'] = re.match(tagi[0], linia).groups()[0]
    elif re.match(tagi[1], linia):
        #print '-------------url-------------'
        status = ''
        dane[-1]['url'] = re.match(tagi[1], linia).groups()[0]
        dane[-1]['id'] = dane[-1]['url']
    elif re.match(tagi[4], linia):
        #print '-------------wersja-------------'
        status = ''
        #dane[-1]['_version_'] = 1
        #dane[-1]['_version_'] = re.match(tagi[4], linia).groups()[0]
    elif re.match(tagi[5], linia):
        #print '-------------url-------------'
        status = ''
        #dane[-1]['url'] = re.match(tagi[5], linia).groups()[0]
    elif re.match(tagi[6], linia):
        #print '-------------base-------------'
        status = ''
        #dane[-1]['base'] = re.match(tagi[6], linia).groups()[0]
    elif re.match(tagi[7], linia):
        #print '-------------contentType-------------'
        status = ''
        #dane[-1]['contentType'] = re.match(tagi[7], linia).groups()[0]
    elif re.match(tagi[8], linia):
        #print '-------------metadata-------------'
        status = ''
        #dane[-1]['metadata'] = re.match(tagi[8], linia).groups()[0]
    elif re.match(tagi[2], linia):
        #print '-------------ParseText-------------'
        status = 'ParseText'
        dane[-1]['text'] = ''
    elif re.match(tagi[3], linia):
        #print '-------------Content-------------'
        status = ''
    elif re.match(tagi[9], linia):
        #print '-------------Content-------------'
        status = 'Content'
        #dane[-1]['Content'] = ''
    elif status == 'ParseText':
        #print '-------------ParseText-------------'
        dane[-1]['text'] += linia
    elif status == 'Content':
        #print '-------------Content-------------'
        #dane[-1]['Content'] += linia
        pass
        
nutch.close()
print 'wynikow:', len(dane)
        
#plik = file(r'../parsed_results/all(excluded deviantart)_parsed_filtered.txt', 'w')
plik = file(r'../parsed_results/deviantart_parsed_filtered.txt', 'w')
pickle.dump(dane, plik)
plik.close()

