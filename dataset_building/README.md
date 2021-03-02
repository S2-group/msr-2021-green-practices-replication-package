# Dataset Building	

Here you find all the data and the code used to mine/extract energy-related data points.	

The file [<i>mongodb-dump.tar.gz</i>](./mongodb-dump.tar.gz) contains all the 339,563 ROS data points. 	

## Pre-configuration	

Considering the Python is already installed and configured:	

1) Install the Python dependencies.	

```bash	
$ pip install -r requirements.txt 	
```	

2) [Restore](https://docs.mongodb.com/manual/reference/program/mongorestore/) the database to your MongoDB instance.	

3) Set the configuration parameters (parameters.cfg):	

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

## Phase 1: Searching for Energy-related Data Points

```bash	
$ cd phase1/	
$ python energy_mining.py	
```	

The output will be in the <i>output_data</i> folder. By default, the data from MSR2021 paper is already there.	

## Generating Data for Phase 2	

Here we just get the data point dates and transform them into timestamps. If you wish to completly execute this phase, you must delete the <i>input_data/included-datapoints-date.csv</i> file.	

```bash	
$ cd phase2/	
$ python get_timestamps.py	
```	

All the data required for Phase 2 will be in the <i>output_data/energy-datapoints.csv</i> file. Now, proceed to the [data analysis](../data_analysis/).
