# Dataset Building

Here you find all the data and the code used to mine/extract energy-related data points.

The file [<i>mongodb-dump.tar.gz</i>](./mongodb-dump.tar.gz) contains all the ROS data we have scrapped (339,563 data points). 

## Pre-configuration

1) Install all the python dependencies.

```bash
$ pip install -r requirements.txt 
```

2) [Restore](https://docs.mongodb.com/manual/reference/program/mongorestore/) the database to your MongoDB instance.

3) Configure your MongoDB parameters:

```bash
$ gedit mongodb.cfg
```

## How to Replicate Phase 1

```bash
$ cd phase1/
$ python energy_mining.py
```

The output will be in the <i>output_data</i> folder.

## Generating the Analysis Spreadsheets

...
