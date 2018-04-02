""" Parse a MISRA C logfile """

import argparse
from misra_parser import MisraParser

from src.writers.misra_console_writer import print_violations_per_rule, print_violations_per_category, \
    print_violations_per_group, print_violations_per_file
from src.writers.misra_file_writer import save_violations_per_rule, save_violations_per_category, \
    save_violations_per_group, save_violations_per_file


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
    input_file = args.input
    standard = args.standard
    verbose = args.verbose

    parser = MisraParser()

    if standard == "C2004":
        parser.read_guidelines("../readers/misra-c2004-guidelines.csv")
    elif standard == "C2012":
        parser.read_guidelines("../readers/misra-c2012-guidelines.csv")
    else:
        print("Unknown standard")
        exit(1)

    parser.read_violations(input_file)

    if verbose:
        print_violations_per_rule(parser.violations_per_rule(), standard)
        print_violations_per_category(parser.violations_per_category())
        print_violations_per_group(parser.violations_per_group())
        print_violations_per_file(parser.violations_per_file())

    save_violations_per_rule(parser.violations_per_rule(), parser.get_guidelines(), standard)
    save_violations_per_category(parser.violations_per_category(), standard)
    save_violations_per_group(parser.violations_per_group(), standard)
    save_violations_per_file(parser.violations_per_file(), standard)


if __name__ == "__main__":
    main()
