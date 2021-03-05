#!/bin/bash

files=`ls ../include/csvutils/*.py`

for f in $files
do
	python3 $f
done
