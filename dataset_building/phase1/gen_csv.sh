#!/bin/bash

files=`ls ../csvutils/*.py`

for f in $files
do
	python3 $f
done
