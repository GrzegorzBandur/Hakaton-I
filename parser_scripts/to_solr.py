#!/usr/bin/env python

import pickle
import pysolr
import os

for nazwa_pliku in os.listdir(r'../parsed_results/'):
    plik = file(r'../parsed_results/%s' % nazwa_pliku)
    print 'miele', nazwa_pliku
    dane = pickle.load(plik)
    print 'zaladowano stron:', len(dane)

    solr = pysolr.Solr(r'http://127.0.0.1:8983/solr')
    solr.add(dane)
    print 'done', nazwa_pliku
