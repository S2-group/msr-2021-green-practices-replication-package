# MSR 2021 – Replication Package

<!--[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3672050.svg)](https://doi.org/10.5281/zenodo.3672050)-->

This repository contains the replication package of the paper published at MSR 2021 with the title **Mining Energy-Related Practices in Robotics Software**.

This study has been designed, developed, and reported by the following investigators:

- [Michel Albonico](https://michelalbonico.github.io) (Vrije Universiteit Amsterdam/Federal University of Technology, Paraná) 
- [Ivano Malavolta](https://www.ivanomalavolta.com) (Vrije Universiteit Amsterdam)
- [Gustavo Pinto](https://gustavopinto.org/) (Federal University of Pará)
- [Emitzá Guzmán](https://scholar.google.ch/citations?user=cMs97_YAAAAJ&hl=en) (Vrije Universiteit Amsterdam)
- [Katerina Chinnappan](http://katerinachinnppan.com/) (Vrije Universiteit Amsterdam)
- [Patricia Lago](https://www.cs.vu.nl/~patricia/Patricia_Lago/Home.html) (Vrije Universiteit Amsterdam)

For any information, interested researchers can contact us by sending an email to any of the investigators listed above.
The full dataset including raw data, mining scripts, and analysis scripts produced during the study are available below.

## How to Cite the Dataset
If the dataset is helping your research, consider to cite it is as follows, thanks!

```
@inproceedings{MSR_2021_architectural_tactics,
  year = { 2021 },
  pages = { To appear },
  month = { May },
  author = { Michel Albonico and Ivano Malavolta and Gustavo Pinto and Emitzá Guzmán and Katerina Chinnappan and Patricia Lago },
  publisher = { ACM },
  booktitle = { Proceedings of the 18th International Conference on Mining Software Repositories, {MSR} },
  title = { Mining the ROS ecosystem for Green Architectural Tactics in Robotics and an Empirical Evaluation },
  address = { New York, NY },
}
```

### Overview of the Replication Package
---

This replication package is structured as follows:

```
./
    |--- data_analysis/       		  The data that has been extracted during the iterative content analysis and the thematic analysis phases, and the spreadsheets used to analyse the data.
    |--- dataset_building/     		  The full dataset of ROS-based systems mined from GitHub, including also the Python scripts for rebuilding/updating the dataset and the raw data produced in all intermediate steps.
    |--- MSR_2020.pdf (not available yet)  A copy of the paper in pdf format
```

Each of the folders listed above are described in details in the remaining of this readme.

### Dataset Building

All the explanation of executing dataset building scripts is in the folder [readme](https://github.com/S2-group/msr-2021-green-practices-replication-package/blob/main/dataset_building/README.md).

---
```
./dataset_building/
  |--- include/
  |--- configuration/conf_reader.py                    Functions to read configuration files.
  |--- mongodb/                                        MongoDB connectors.
       |--- driver.py                                  Used by mongo_con.
       |--- mongo_con.py                               Functions to connect and query MongoDB. 
  |--- phase1/
       |--- input_data/                                
            |--- git_repos_data.json                   Markdown files and code comments (we still need to upload this to MongoDB).
       |--- output_data/                               JSON files (for each collection) containing data points with energy-related terms.
       |--- energy_mining.py                           Mining code that searches for energy-related.
       |--- gen_csv.py				       Code that generates the CSV file from extracted JSONs.
       |--- energy-term-datapoints.csv                 Data points with energy terms.
  |--- phase2/
       |--- input_data/
            |--- included-datapoints-date-msr2021.csv  Reference file (used in the paper) - all the energy-related data points and their dates.     
            |--- included-datapoints-date.csv          Editable list of energy-related data points with dates.
	    |--- included-datapoints.csv               All the energy-related datapoints without dates (already manually filtered).
       |--- output_data/
            |--- energy-datapoints-msr2021.csv         Reference file (used in the paper) - all the energy-related data points with timestamps.
            |--- energy-datapoints.csv                 Editable list of energy-related data points with timestamps.
       |--- gen_codes.py                               Generates a list of codes (output: ../data_analysis/coding/initial-codes.csv).
       |--- get_date.py	                               Gets the date of each data point (we still need to move this to Phase 1).
       |--- get_timestamp.py                           Gets the timestamp of each data point (we still need to move this to Phase 1).
  |--- phase3/
       output_data/
            |--- false-negatives.json                  JSON file containing the possible false negatives.
       |--- get_false_negatives.py                     Mining code that searches for false-negatives.
  |--- Energy-Data-Points-Summary.pdf                  Summary of energy-related data points from our paper.
  |--- mongodb-dump.tar.gz                             Dump of MongoDB database.
  |--- parameters.cfg                                  Configuration file.
  |--- requirements.txt                                Python requirements.
```

### Data Analysis

The data in the CSV files has been manually, collaboratively, and iteratively extracted by the authors of the paper. 

---
```
./data_analysis/
    |--- energy-related-datapoints.csv                 Energy-related data points with timestamp, robot type and main capability.
    |--- coding/
        |--- initial-codes.csv                         Data points and their codes.
	|--- separated-codes.csv                       List of separated codes.
	|--- cleaned-codes.csv                         Renamed codes.
	|--- codes-classification.csv                  Initial classification of codes by research question.
    |--- rq1/
	|--- plot_graph.R                              R script that plots RQ1 graph.
    |--- rq2/
        |--- rq2-themes.csv                            Cause themes.               
	|--- main-causes.csv                           Causes after themes.
    |--- rq3/
        |--- rq3-themes.csv                            Solution themes.
	|--- main-solutions.csv                        Solutions after themes.
    |--- rq4/
    	|--- quality-attributes.csv                    Quality atributes.
```

## License

This software is licensed under the MIT License.
