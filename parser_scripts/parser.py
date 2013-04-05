import re
import pickle

tagi = [r'^Recno:: ([0-9]+)$', r'^URL:: (.*)$', r'^ParseText::$', r'^Content::$', r'^Version: (-?[0-9]+)$', r'^url: (.*)$', r'^base: (.*)$', r'^contentType: (.*)$', r'^metadata: (.*)$', r'^Content:$']

nutch = file(r'../../../all/deviantart.txt')
dane = []
status = ''

for linia in nutch:
    #print linia
    if re.match(tagi[0], linia):
        print '-------------nowa strona-------------'
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
        dane[-1]['_version_'] = re.match(tagi[4], linia).groups()[0]
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
        
plik = file(r'../../../all/deviantart_parsed.txt', 'w')
pickle.dump(dane, plik)
plik.close()

