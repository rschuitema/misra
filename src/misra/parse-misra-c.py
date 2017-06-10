import argparse
import csv
import operator
from misra_parser import MisraParser

# custom compare function to compare the rules
def misraC2004Compare(rule):
	return int(rule.split('.')[0])*100 + int(rule.split('.')[1])

def misraC2012Compare(rule):
	return int(rule.split('.')[0])*100 + int(rule.split('.')[1])
	
def determineCompareMethod(standard):
	possibles = globals().copy()
	possibles.update(locals())
	methodName = standard + "Compare"
	method = possibles.get(methodName)
	if not method:
		 raise NotImplementedError("Method %s not implemented" % methodName)	

	return method
	

def printViolationsPerRule(violationsPerRule, standard):
	
	method = determineCompareMethod(standard)
	sortedViolations = sorted(violationsPerRule, key=method)
	
	print ("-----------")
	for key in sortedViolations:
		print ('%s,%s' % (key, violationsPerRule[key]))
	
def printViolationsPerCategory(violationsPerCategory):
	
	print ("-----------")
	for key in violationsPerCategory:
		print ('%s,%s' % (key, violationsPerCategory[key]))

def printViolationsPerGroup(violationsPerGroup):
	
	print ("-----------")
	for key in violationsPerGroup:
		print ('%s,%s' % (key, violationsPerGroup[key]))

def printViolationsPerFile(violationsPerFile):
	
	sortedViolations = sorted(violationsPerFile.items(), key=operator.itemgetter(1), reverse=True)
	
	print ("-----------")
	for key in sortedViolations:
		print ('%s,%s' % (key[0], key[1]))

	
def saveViolationsPerRule(violationsPerRule, guidelines, standard):

	method = determineCompareMethod(standard)
	sortedViolations = sorted(violationsPerRule, key=method)
	
	outputfile = standard + "-violations-per-rule.csv"
	
	with open(outputfile, 'w') as output:
		csvwriter = csv.writer(output, delimiter = ',', lineterminator='\n', quoting=csv.QUOTE_ALL)
		csvwriter.writerow(['Rule', 'Violations', 'Description'])
		
		for key in sortedViolations:
		
			if key in guidelines.keys():
				csvwriter.writerow([key, 
									violationsPerRule[key],
									guidelines[key].get_description()])


def saveViolationsPerCategory(violationsPerCategory, standard):
	outputfile = standard + "-violations-per-category.csv"
	
	with open(outputfile, 'w') as output:
		csvwriter = csv.writer(output, delimiter = ',', lineterminator='\n', quoting=csv.QUOTE_ALL)
		csvwriter.writerow(['Category', 'Violations'])
		
		for key in violationsPerCategory:
			csvwriter.writerow([key, 
								violationsPerCategory[key]])

def saveViolationsPerGroup(violationsPerGroup, standard):
	outputfile = standard + "-violations-per-group.csv"
	
	with open(outputfile, 'w') as output:
		csvwriter = csv.writer(output, delimiter = ',', lineterminator='\n', quoting=csv.QUOTE_ALL)
		csvwriter.writerow(['Group', 'Violations'])
		
		for key in violationsPerGroup:
			csvwriter.writerow([key, 
								violationsPerGroup[key]])

def saveViolationsPerFile(violationsPerFile, standard):
	sortedViolations = sorted(violationsPerFile.items(), key=operator.itemgetter(1), reverse=True)
	
	outputfile = standard + "-violations-per-file.csv"
	
	with open(outputfile, 'w') as output:
		csvwriter = csv.writer(output, delimiter = ',', lineterminator='\n', quoting=csv.QUOTE_ALL)
		csvwriter.writerow(['File', 'Violations'])
		
		for key in sortedViolations:
			csvwriter.writerow([key[0], 
							   int(key[1])])
		

def parseArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("input", help="file to parse")
	parser.add_argument("--output", help="file to store the results", default="misragram.csv")
	parser.add_argument("--standard", help="the standard of the input file", choices=["misraC2004", "misraC2012", "misraC++2008"], default="misraC2004")
	parser.add_argument("--verbose", help="print parse results to console")
	args = parser.parse_args()
	return args

	
def main():

	args = parseArguments()
	input = args.input
	output = args.output
	standard = args.standard
	verbose = args.verbose

	
	parser = MisraParser()
	
	if standard == "misraC2004":
		parser.readGuidelines("misra-c2004-guidelines.csv")
	elif standard == "misraC2012":
		parser.readGuidelines("misra-c2012-guidelines.csv")
	
	parser.readViolations(input)
	
	if verbose:
		printViolationsPerRule(parser.violationsPerRule(), standard)
		printViolationsPerCategory(parser.violationsPerCategory())
		printViolationsPerGroup(parser.violationsPerGroup())
		printViolationsPerFile(parser.violationsPerFile())
	
	saveViolationsPerRule(parser.violationsPerRule(), parser.getGuidelines(), standard)
	saveViolationsPerCategory(parser.violationsPerCategory(), standard)
	saveViolationsPerGroup(parser.violationsPerGroup(), standard)
	saveViolationsPerFile(parser.violationsPerFile(), standard)

		
if __name__ == "__main__":
    main()
