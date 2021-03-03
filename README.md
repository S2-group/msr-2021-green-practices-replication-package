# MSR 2021 – Replication package

<!--[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3672050.svg)](https://doi.org/10.5281/zenodo.3672050)-->

This repository contains the replication package and dataset of the paper <b>to be </b> published at MSR 2021 with the title **Mining Energy-Related Practices in Robotics Software**.

This study has been designed, developed, and reported by the following investigators:

- [Michel Albonico](https://michelalbonico.github.io) (Vrije Universiteit Amsterdam/Federal University of Technology, Paraná) 
- [Ivano Malavolta](https://www.ivanomalavolta.com) (Vrije Universiteit Amsterdam)
- [Gustavo Pinto](https://gustavopinto.org/) (Federal University of Pará)
- [Emitzá Guzmán](https://scholar.google.ch/citations?user=cMs97_YAAAAJ&hl=en) (Vrije Universiteit Amsterdam)
- [Katerina Chinnappan](http://katerinachinnppan.com/) (Vrije Universiteit Amsterdam)
- [Patricia Lago](https://www.cs.vu.nl/~patricia/Patricia_Lago/Home.html) (Vrije Universiteit Amsterdam)

For any information, interested researchers can contact us by sending an email to any of the investigators listed above.
The full dataset including raw data, mining scripts, and analysis scripts produced during the study are available below.

## How to cite the dataset
If the dataset is helping your research, consider to cite it is as follows, thanks!

```
...
```

### Overview of the replication package
---

This replication package is structured as follows:

```
    /
    .
    |--- data_analysis/       		The data that has been extracted during the iterative content analysis and the thematic analysis phases, and the spreadsheets used to analyse the data.
    |--- dataset_building/     		The full dataset of ROS-based systems mined from GitHub, including also the Python scripts for rebuilding/updating the dataset and the raw data produced in all intermediate steps.
    |--- ICSE_SEIP_2020.pdf             A copy of the paper in pdf format
```

Each of the folders listed above are described in details in the remaining of this readme.

### Dataset Building

All the explanationg of how to execute the dataset building scripts are in the folder [readme](https://github.com/S2-group/msr-2021-green-practices-replication-package/blob/main/dataset_building/README.md).

---
```
dataset_building
    	.
	|--- include/
       |--- configuration/conf_reader.py              Functions to read the configuration file.
       |--- mongodb/                                  MongoDB connectors.
             |--- driver.py
             |--- mongo_con.py                        Functions to connect and query MongoDB. 
  |--- phase1/
       |--- input_data/                               Data that is not queried from MongoDB.
            |--- git_repos_data.json                  ?
       |--- output_data/                              JSON files corresponding energy-related data points extracted from each of the database collections. 
       |--- energy_mining.py                          Mining code that searches for energy-related terms in the data points.
  |--- phase2/
       |--- input_data/
            |--- included-datapoints-date-msr2021.csv
            |--- included-datapoints-date.csv
            |--- included-datapoints.csv (TO BE EXCLUDED)
       |--- output_data/
            |--- energy-datapoints-msr2021.csv
            |--- energy-datapoints.csv
  |--- aaaa.pdf                                       Summary of energy-related data points from our paper. 
  |--- mongodb-dump.tar.gz
  |--- parameters.cfg
  |--- requirements.txt
```

### Data Analysis
---
```
data_analysis
    .
    |--- 
```
The data in the CSV files has been manually, collaboratively, and iteratively extracted by the authors of the paper. The steps for recreating the plots presented in the paper the list of contributors to contact for replicating this study are presented [here](./INSTALL.md). 

## License

This software is licensed under the MIT License.
