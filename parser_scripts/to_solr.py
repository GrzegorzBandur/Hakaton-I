import pickle
import pysolr

plik = file(r'../parsed_results/deviantart_parsed_filtered.txt')
dane = pickle.load(plik)
print len(dane)

solr = pysolr.Solr(r'http://127.0.0.1:8983/solr', timeout=10)
solr.add(dane)
print 'done'
