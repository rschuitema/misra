[![Build Status](https://travis-ci.org/rschuitema/misra.svg?branch=develop)](https://travis-ci.org/rschuitema/misra)
[![BCH compliance](https://bettercodehub.com/edge/badge/rschuitema/misra?branch=develop)](https://bettercodehub.com/)

# misra
This project visualizes the misra violations of a code base. It is able to visualize the violations of the MISRA C2004 and MISRA C2012 standards. It parses the output of the tool <a href="https://scitools.com/">understand</a>.

# usage
1. Run the tool <a href="https://scitools.com/">understand</a> to analyse the codebase for misra violations.
1. Export the results from <a href="https://scitools.com/">understand</a> to a csv file.
1. Parse the csv file using the python script `parse_misra_c.py`with the following command: `python parse_misra_c.py --standard C2004 understand_codecheck_result.csv`.


This will generate the following set of files:

* misra-C2004-violations-per-rule.csv
* misra-C2004-violations-per-group.csv
* misra-C2004-violations-per-file.csv
* misra-C2004-violations-per-category.csv

# example output
<img src="./images/example.png" width="600">
