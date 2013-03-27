#!/bin/bash

#sciezka do nutcha, trzeba zmienic!!!
cd /media/10420C38420C2556/apache-nutch-1.6-bin/apache-nutch-1.6/

for file in crawl/segments/*
do
	BASENAME=`basename $file`
	./bin/nutch readseg -dump crawl/segments/$BASENAME/ dump_folder -nofetch -nogenerate -noparse -noparsedata -noparsetex
	cat dump_folder/dump >> all_new.txt
done

echo "FINISHED"
