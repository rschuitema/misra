import csv
import unittest.mock as mock
from io import StringIO

from src.readers.misra_guideline_reader import read_misra_guidelines


def test_read_misrac2004_guideline_success():

    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Rule", "Required", "Language extensions", "Assembly language shall be encapsulated and isolated."
    "4.2", "Rule", "Required", "Character sets", "Trigraphs shall not be used.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2004", test_reader)
        
        m.assert_called_with('misra-c2004-guidelines.csv', 'rt')
        assert '2.1' in guidelines.keys()
        assert 'Rule' == guidelines['2.1'].get_classification()
        assert 'Required' == guidelines['2.1'].get_category()
        assert 'Language extensions' == guidelines['2.1'].get_group()
        assert 'Assembly language shall be encapsulated and isolated.' == guidelines['2.1'].get_description()


def test_read_misrac2004_multiple_guidelines_success():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Rule", "Required", "Language extensions", "Assembly language shall be encapsulated and isolated."
    "4.2", "Rule", "Required", "Character sets", "Trigraphs shall not be used.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2004", test_reader)

        m.assert_called_with('misra-c2004-guidelines.csv', 'rt')
        assert '2.1' in guidelines.keys()
        assert '4.2' in guidelines.keys()
        assert 2 == len(guidelines)


def test_read_guideline_wrong_rule_empty_dictionary():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "201", "Rule", "Required", "Language extensions", "Assembly language shall be encapsulated and isolated.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2004", test_reader)

        m.assert_called_with('misra-c2004-guidelines.csv', 'rt')
        assert 0 == len(guidelines)


def test_read_guideline_wrong_classification_empty_dictionary():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Suggestion", "Required", "Language extensions", "Assembly language shall be encapsulated and isolated.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2004", test_reader)

        m.assert_called_with('misra-c2004-guidelines.csv', 'rt')
        assert 0 == len(guidelines)


def test_read_guideline_wrong_category_empty_dictionary():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Rule", "New", "Language extensions", "Assembly language shall be encapsulated and isolated.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2004", test_reader)

        m.assert_called_with('misra-c2004-guidelines.csv', 'rt')
        assert 0 == len(guidelines)


def test_read_guideline_wrong_group_empty_dictionary():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Rule", "Required", "Language extension", "Assembly language shall be encapsulated and isolated.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2004", test_reader)

        m.assert_called_with('misra-c2004-guidelines.csv', 'rt')
        assert 0 == len(guidelines)


def test_read_misrac2012_guideline_success():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Rule", "Required", "Language extensions", "Assembly language shall be encapsulated and isolated."
    "4.2", "Rule", "Required", "Character sets", "Trigraphs shall not be used.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("C2012", test_reader)

        m.assert_called_with('misra-c2012-guidelines.csv', 'rt')
        assert '2.1' in guidelines.keys()


def test_read_misracpp2008_guideline_success():
    in_mem_csv = StringIO("""Rule,Classification,Category,Group,Description
    "2.1", "Rule", "Required", "Language extensions", "Assembly language shall be encapsulated and isolated."
    "4.2", "Rule", "Required", "Character sets", "Trigraphs shall not be used.\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        guidelines = read_misra_guidelines("CPP2008", test_reader)

        m.assert_called_with('misra-cpp2008-guidelines.csv', 'rt')
        assert '2.1' in guidelines.keys()
