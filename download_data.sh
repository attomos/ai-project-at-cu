#!/bin/sh

mkdir data
cd data
curl -O http://www2.imm.dtu.dk/pubdb/views/edoc_download.php/6010/zip/imm6010.zip
unzip -j imm6010.zip
curl -O http://www.cs.cornell.edu/People/pabo/movie-review-data/rt-polaritydata.tar.gz
mkdir rt-polaritydata && tar -xf rt-polaritydata.tar.gz -C rt-polaritydata
