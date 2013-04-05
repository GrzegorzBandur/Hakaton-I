import re
import pickle

tagi = [r'^Recno:: ([0-9]+)$', r'^URL:: (.*)$', r'^ParseText::$', r'^Content::$', r'^Version: (-?[0-9]+)$', r'^url: (.*)$', r'^base: (.*)$', r'^contentType: (.*)$', r'^metadata: (.*)$', r'^Content:$']

nutch = file(r'P:\all\all(excluded deviantart).txt')
dane = []
status = ''

for linia in nutch.readline():
    if re.match(tagi[0], linia):
        status = ''
        dane.append({})
        #dane[-1]['recno'] = re.match(tagi[0], linia).groups()[0]
    elif re.match(tagi[1], linia):
        status = ''
        dane[-1]['url'] = re.match(tagi[1], linia).groups()[0]
        dane[-1]['id'] = dane[-1]['url']
    elif re.match(tagi[4], linia):
        status = ''
        dane[-1]['_version_'] = re.match(tagi[4], linia).groups()[0]
    elif re.match(tagi[5], linia):
        status = ''
        #dane[-1]['url'] = re.match(tagi[5], linia).groups()[0]
    elif re.match(tagi[6], linia):
        status = ''
        #dane[-1]['base'] = re.match(tagi[6], linia).groups()[0]
    elif re.match(tagi[7], linia):
        status = ''
        #dane[-1]['contentType'] = re.match(tagi[7], linia).groups()[0]
    elif re.match(tagi[8], linia):
        status = ''
        #dane[-1]['metadata'] = re.match(tagi[8], linia).groups()[0]
    elif re.match(tagi[3], linia):
        status = 'ParseText'
        dane[-1]['text'] = ''
    elif re.match(tagi[4], linia):
        status = ''
    elif re.match(tagi[9], linia):
        status = 'Content'
        #dane[-1]['Content'] = ''
    elif status == 'ParseText':
        dane[-1]['text'] += linia
    elif status == 'Content':
        #dane[-1]['Content'] += linia
        pass
        
plik = file(r'\\files\students\s380909\Desktop\ISI\hackaton1\tal', 'w')
pickle.dump(dane, plik)