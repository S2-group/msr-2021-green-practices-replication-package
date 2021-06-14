# MSR 2021 – Replication Package

<!--[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3672050.svg)](https://doi.org/10.5281/zenodo.3672050)-->

This repository contains the replication package of the paper published at MSR 2021 with the title **Energy-Aware Robotics Software: A Catalog of Architectural Tactics from the ROS Ecosystem**.

This study has been designed, developed, and reported by the following investigators:

- [Katerina Chinnappan](http://katerinachinnppan.com/) (Vrije Universiteit Amsterdam)
- [Ivano Malavolta](https://www.ivanomalavolta.com) (Vrije Universiteit Amsterdam)
- [Patricia Lago](https://www.cs.vu.nl/~patricia/Patricia_Lago/Home.html) (Vrije Universiteit Amsterdam)
- [Michel Albonico](https://michelalbonico.github.io) (Vrije Universiteit Amsterdam/Federal University of Technology, Paraná) 
- [Grace A. Lewis](https://www.andrew.cmu.edu/user/gritter/lewis.html) (Software Engineering Institute, Carnegie Mellon University, USA)


For any information, interested researchers can contact us by sending an email to any of the investigators listed above.
The full dataset including raw data, mining scripts, and analysis scripts produced during the study are available below.
<!--
## How to Cite the Dataset
If the dataset is helping your research, consider to cite it is as follows, thanks!

```
@inproceedings{MSR_2021_robotics_green_practices,
  title = { Mining Energy-Related Practices in Robotics Software },
  author = { Michel Albonico and Ivano Malavolta and Gustavo Pinto and Emitzá Guzmán and Katerina Chinnappan and Patricia Lago },
  pages = { To appear },
  month = { May },
  publisher = {{IEEE} / {ACM}},
  year      = {2021},
  booktitle = { Proceedings of the 18th International Conference on Mining Software Repositories, {MSR} },
  url = {https://arxiv.org/abs/2103.13762},
  address = { New York, NY },
}
```


The preprint paper is available on [arXiv](https://arxiv.org/abs/2103.13762).
-->

### Overview of the Replication Package
---

This replication package is structured as follows:

```
./
    |--- dataset/     		  The full dataset of ROS-based systems mined from GitHub and the scripts used to extract the data.
    |--- data_analysis/       	  Mining scripts and spreadsheets used in the manual data analysis.
    |--- ECSA_2021.pdf            (not available yet)  A copy of the paper in pdf format.
```

Each of the folders listed above are described in details in the remaining of this readme.

### Dataset

#### Building the Dataset
...

#### Mining the Data

All the explanation of the data mining is in the folder [readme](https://github.com/S2-group/msr-2021-green-practices-replication-package/blob/main/dataset_building/README.md).

---
```
./dataset_building/
  |--- include/
  	|--- helpers/				       Scripts for secondary tasks, such as reading the configuration file.
  	|--- mongodb/                                  Scripts to interact to MongoDB.
        |--- csvutils/				       Scripts to convert JSON to CSV files.
  |--- phase1/
       |--- input_data/                                
            |--- git_repos_data.json                   Markdown files and code comments (we still need to upload this to MongoDB).
       |--- output_data/                               JSON files (for each collection) containing data points with energy-related terms.
       |--- energy_mining.py                           Mining code that searches for energy-related terms.
       |--- gen_csv.sh				       Code that generates the CSV file from extracted JSONs.
       |--- energy-term-datapoints.csv                 Data points with energy terms.
  |--- phase2/
       |--- input_data/
	    |--- included-datapoints.csv               All the energy-related datapoints without dates (result from manual selection).
       |--- output_data/
            |--- energy-datapoints.csv                 List of energy-related data points with timestamps.
       |--- get_date.py	                               Gets the date of each data point (we still need to move this to Phase 1).
       |--- get_timestamp.py                           Gets the timestamp of each data point (we still need to move this to Phase 1).
  |--- phase3/
       output_data/                                    JSON files of each collection containing the possible false negatives.
       |--- get_false_negatives.py                     Searches for false-negatives.
       |--- no-energy-terms-datapoints.csv             List of data points without energy terms.
  |--- energy_terms_stats.pdf                          Summary of data points with energy terms.
  |--- mongodb-dump.tar.gz                             Dump of MongoDB database.
  |--- configuration.cfg                                  Configuration file.
  |--- requirements.txt                                Python requirements.
```

### Data Analysis

The data in the CSV files has been manually, collaboratively, and iteratively extracted by the authors of the paper.

---
```
./data_analysis/
    |--- phase2-filtering_by_terms/
        |--- ...
    |--- phase3-data_points_selection/
	|--- ...
    |--- phase4-tactics_extraction/
        |--- ...
```

## License

This software is licensed under the MIT License.
