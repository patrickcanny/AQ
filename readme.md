# AQ
Implementation of the AQ (Max Star) Data Mining Algorithm presented in EECS 690. This algorithm was modified to discretize a given dataset, whether it contains numeric or symbolic attributes.

# Overview
The AQ Algorithm is a systematic rule-induction algorithm that creates a cover for each concept in a dataset by calculating and comparing "Stars" generated by analyzing attribute-value pairings in the dataset.

# Program Instructions
# Requirements
- Python 2.7.14

# Compilation and Testing
1. Clone this repository into a local directory
2. Type `make` to  initialize the program. You will be prompted for a fileName, and then again for a MaxStar value. The program will output the rules affiliated with your dataset in the folder `data/my-data.with.negation` and `data/my-data.without.negation`
3. Type Command `make clean` to remove Python-generated machine code, as well as old rulesets.

# Comments
Ran into some issues down the stretch, resulting in some shortcomings. Issues in simplifying ruleset when creating a cover for each concept, and general issues on very large datasets. Discovered the importance of writing clean code through this project. Good learning experience!
