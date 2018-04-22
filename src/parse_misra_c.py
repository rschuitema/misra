""" Parse a MISRA C logfile """
import sys
import os
import argparse

sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../'))
from parsers import understand_violation_parser
from queries import violations_per_category
from queries import violations_per_group
from queries import violations_per_rule
from queries import violations_per_file
from readers import misra_guideline_reader
from readers import misra_violation_reader
from writers import misra_console_writer
from writers import misra_file_writer

#from src.parsers.understand_violation_parser import parse_understand_violations
#from src.queries.violations_per_category import get_violations_per_category
#from src.queries.violations_per_file import get_violations_per_file
#from src.queries.violations_per_group import get_violations_per_group
#from src.queries.violations_per_rule import get_violations_per_rule
#from src.readers.misra_guideline_reader import read_misra_guidelines
#from src.readers.misra_violation_reader import read_misra_violations
#from src.writers.misra_console_writer import print_violations_per_rule, print_violations_per_category, \
#    print_violations_per_group, print_violations_per_file
#from src.writers.misra_file_writer import save_violations_per_rule, save_violations_per_category, \
#    save_violations_per_group, save_violations_per_file


def parse_arguments():
    """ Parse the commandline arguments """

    parser = argparse.ArgumentParser()
    parser.add_argument("input",
                        help="file to parse")
    parser.add_argument("--standard",
                        help="the standard of the input file",
                        choices=["C2004", "C2012", "C++2008"],
                        default="C2004")
    parser.add_argument("--verbose",
                        help="print parse results to console",
                        action="store_true")

    args = parser.parse_args()

    return args


def main():
    """ Main function of the program """

    args = parse_arguments()

    guidelines = read_misra_guidelines(args.standard)
    violations = read_misra_violations(args.input)
    guideline_violations = parse_understand_violations(violations, guidelines)

    if args.verbose:
        print_violations_per_rule(get_violations_per_rule(guideline_violations, guidelines), args.standard)
        print_violations_per_category(get_violations_per_category(guideline_violations, guidelines))
        print_violations_per_group(get_violations_per_group(guideline_violations, guidelines))
        print_violations_per_file(get_violations_per_file(guideline_violations, guidelines))

    save_violations_per_rule(get_violations_per_rule(guideline_violations, guidelines), guidelines, args.standard)
    save_violations_per_category(get_violations_per_category(guideline_violations, guidelines), args.standard)
    save_violations_per_group(get_violations_per_group(guideline_violations, guidelines), args.standard)
    save_violations_per_file(get_violations_per_file(guideline_violations, guidelines), args.standard)


if __name__ == "__main__":
    main()
