""" Parse a MISRA C logfile """

import argparse
import csv
import operator
from misra_parser import MisraParser


# custom compare function to compare the rules
def misra_c2004_compare(rule):
    """ compare misra C2004 rules """

    return int(rule.split('.')[0])*100 + int(rule.split('.')[1])


def misra_c2012_compare(rule):
    """ compare misra C2012 rules """

    return int(rule.split('.')[0])*100 + int(rule.split('.')[1])


def determine_compare_method(standard):
    """ determine the compare method based upon the provided standard """

    possibles = globals().copy()
    possibles.update(locals())
    method_name = "misra_" + standard.lower() + "_compare"
    method = possibles.get(method_name)
    if not method:
        raise NotImplementedError("Method %s not implemented" % method_name)

    return method


def print_violations_per_rule(violations_per_rule, standard):
    """ Print the violations per rule on the standard output """

    method = determine_compare_method(standard)
    sorted_violations = sorted(violations_per_rule, key=method)

    print("-----------")
    for key in sorted_violations:
        print('%s,%s' % (key, violations_per_rule[key]))


def print_violations_per_category(violations_per_category):
    """ Print the violations per category on the standard output """

    print("-----------")
    for key in violations_per_category:
        print('%s,%s' % (key, violations_per_category[key]))


def print_violations_per_group(violations_per_group):
    """ Print the violations per group on the standard output """

    print("-----------")
    for key in violations_per_group:
        print('%s,%s' % (key, violations_per_group[key]))


def print_violations_per_file(violations_per_file):
    """ Print the violations per file on the standard output """

    sorted_violations = sorted(violations_per_file.items(), key=operator.itemgetter(1), reverse=True)

    print("-----------")
    for key in sorted_violations:
        print('%s,%s' % (key[0], key[1]))


def save_violations_per_rule(violations_per_rule, guidelines, standard):
    """ Save the violations per rule to a file """

    method = determine_compare_method(standard)
    sorted_violations = sorted(violations_per_rule, key=method)

    outputfile = "misra-" + standard + "-violations-per-rule.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Rule', 'Violations', 'Description'])

        for key in sorted_violations:

            if key in guidelines.keys():
                csvwriter.writerow([key,
                                    violations_per_rule[key],
                                    guidelines[key].get_description()])


def save_violations_per_category(violations_per_category, standard):
    """ Save the violations per category to a file """

    outputfile = "misra-" + standard + "-violations-per-category.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Category', 'Violations'])

        for key in violations_per_category:
            csvwriter.writerow([key,
                                violations_per_category[key]])


def save_violations_per_group(violations_per_group, standard):
    """ Save the violations per group to a file """

    outputfile = "misra-" + standard + "-violations-per-group.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Group', 'Violations'])

        for key in violations_per_group:
            csvwriter.writerow([key, violations_per_group[key]])


def save_violations_per_file(violations_per_file, standard):
    """ Save the violations per file to a file """

    sorted_violations = sorted(violations_per_file.items(), key=operator.itemgetter(1), reverse=True)

    outputfile = "misra-" + standard + "-violations-per-file.csv"

    with open(outputfile, 'w') as output:
        csvwriter = csv.writer(output, delimiter=',', lineterminator='\n', quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['File', 'Violations'])

        for key in sorted_violations:
            csvwriter.writerow([key[0], int(key[1])])


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
        parser.read_guidelines("misra-c2004-guidelines.csv")
    elif standard == "C2012":
        parser.read_guidelines("misra-c2012-guidelines.csv")
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
