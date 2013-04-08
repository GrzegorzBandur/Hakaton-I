#!/usr/bin/env python

import pickle
import pysolr
import os

katalog = r'../parsed_results/'

for nazwa_pliku in os.listdir(katalog):
    plik = file('{0}{1}'.format(katalog, nazwa_pliku))
    print 'miele', nazwa_pliku
    dane = pickle.load(plik)
    print 'zaladowano stron:', len(dane)

    solr = pysolr.Solr(r'http://127.0.0.1:8983/solr')
    pocz = 0
    for dyszki in range(10, len(dane), 10):
        print 'dodaje od {0} do {1}'.format(pocz, dyszki)
        solr.add(dane[pocz:dyszki])
        pocz=dyszki
    print 'dodaje od {0} do konca'.format(pocz)
    solr.add(dane[pocz:])
    print 'done', nazwa_pliku

print 'optymalizuje baze solr'
solr.optimize()
print 'done'
