# Dataset Building

Here you find all the data and the code used to mine/extract energy-related data points.

The file [<i>mongodb-dump.tar.gz</i>](./mongodb-dump.tar.gz) contains all the ROS data we have scrapped (339,563 data points). 

## Pre-configuration

1) Install all the python dependencies.

```bash
$ pip install -r requirements.txt 
```

2) [Restore](https://docs.mongodb.com/manual/reference/program/mongorestore/) the database to your MongoDB instance.

3) Configure the configuration parameters (file parameters.cfg):
 
```
[general]
host = ***:27017
database = data_phase1
con_method = mongodb

[security]
user = ***
password = ***
extra_param = ?authSource=admin

[github]
token = ***
```
The GitHub token is required for Phase 2.

## How to Replicate Phase 1

```bash
$ cd phase1/
$ python energy_mining.py
```

The output will be in the <i>output_data</i> folder. By default, the data from MSR2021 paper is there.

## Generating the Analysis Spreadsheets

Here we just get the data point dates and transforme them into timestamps. If you wish to completly execute this phase, you mus delete the <i>input_data/included-datapoints-date.csv</i> file.

```bash
$ cd phase2/
$ python get_timestamps.py
```

All the data points and their timestamps will be in the <i>output_data/energy-datapoints.csv</i> file. Proceed to the [data analysis](../data_analysis/).