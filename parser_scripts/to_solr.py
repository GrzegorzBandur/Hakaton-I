import pickle
import pysolr

plik = file(r'../parsed_results/all(excluded deviantart)_parsed_filtered.txt')
dane = pickle.load(plik)
print len(dane)

solr = pysolr.Solr('http://localhost:8983/solr/')
solr.add(dane)
print 'done'
