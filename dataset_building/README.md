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

3) Set the configuration parameters (./configuration.cfg):	

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

The output will be JSON files in the <i>output_data</i> folder. By default, the data from MSR2021 paper is already there.	

Now, it is time to generate a CSV file for Phase 2.

```bash	
$ bash gen_csv.sh	
```	
The output will be in the <i>energy-term-datapoints.csv</i> file.

## Phase 2: Generating Timestamps

Here we just get the data point dates and transform them into timestamps, necessary for answering RQ1. The list of <b>included</b> data points (energy-related ones) must be in <i>input_data/included-datapoints.csv</i>. 

***If you wish to completly execute this phase, you must delete the <i>input_data/included-datapoints-date.csv</i> file.	***

```bash	
$ cd phase2/	
$ python get_timestamps.py	
```	

All the data required for Phase 2 will be in the <i>output_data/energy-datapoints.csv</i> file. Now, proceed to the [data analysis](../data_analysis/).

## Phase 3: Searching for False Negatives

In this phase we generate a list of data points without the energy terms, so we can check whether we miss something (false negatives). 

First, we generate the JSON files for each of the collections.

```bash	
$ cd phase3/	
$ python get_false_negatives.py
```	

Then, we generate a CSV file that is used for a manual analysis.

```bash	
$ bash ../phase1/gen_csv.sh
```
