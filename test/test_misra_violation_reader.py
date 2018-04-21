import csv
import unittest.mock as mock
from io import StringIO
from src.readers.misra_violation_reader import read_misra_violations


def test_read_misrac2004_violation_success():

    in_mem_csv = StringIO("""File,Violation,Line,Column,Check,Entity
    "upgrade_image.c","Identifier plain reused","963","16","5.7 No identifier name should be reused","plain"
    "event_log.h","Identifier EVENT_LOG_TYPE_SNR_FAULTS reused","247","4","5.7 No identifier name should be reused","EVENT_LOG_TYPE_SNR_FAULTS\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        violations = read_misra_violations("violations.csv", test_reader)
        file, violation, line, column, check, entity = violations[0]

        m.assert_called_with('violations.csv', 'rt')

        assert 'upgrade_image.c' == file
        assert '963' == line
        assert '16' == column
        assert 'plain' == entity
        assert 'Identifier plain reused' == violation
        assert '5.7 No identifier name should be reused' == check


def test_read_misrac2004_multiple_violation_success():

    in_mem_csv = StringIO("""File,Violation,Line,Column,Check,Entity
    "upgrade_image.c","Identifier plain reused","963","16","5.7 No identifier name should be reused","plain"
    "event_log.h","Identifier EVENT_LOG_TYPE_SNR_FAULTS reused","247","4","5.7 No identifier name should be reused","EVENT_LOG_TYPE_SNR_FAULTS\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        violations = read_misra_violations("violations.csv", test_reader)

        m.assert_called_with('violations.csv', 'rt')

        assert len(violations) == 2


def test_read_misrac2004_wrong_line_empty_dictionary():

    in_mem_csv = StringIO("""File,Violation,Line,Column,Check,Entity
    "upgrade_image.c","Identifier plain reused","hallo","16","5.7 No identifier name should be reused","plain\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        violations = read_misra_violations("violations.csv", test_reader)

        m.assert_called_with('violations.csv', 'rt')

        assert 0 == len(violations)


def test_read_misrac2004_wrong_column_empty_dictionary():

    in_mem_csv = StringIO("""File,Violation,Line,Column,Check,Entity
    "upgrade_image.c","Identifier plain reused","321","pi","5.7 No identifier name should be reused","plain\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        violations = read_misra_violations("violations.csv", test_reader)

        m.assert_called_with('violations.csv', 'rt')

        assert 0 == len(violations)


def test_read_misrac2004_wrong_check_empty_dictionary():

    in_mem_csv = StringIO("""File,Violation,Line,Column,Check,Entity
    "upgrade_image.c","Identifier plain reused","321","32","No identifier name should be reused","plain\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        violations = read_misra_violations("violations.csv", test_reader)

        m.assert_called_with('violations.csv', 'rt')

        assert 0 == len(violations)


def test_read_misrac2004_wrong_check2_empty_dictionary():

    in_mem_csv = StringIO("""File,Violation,Line,Column,Check,Entity
    "upgrade_image.c","Identifier plain reused","321","32","No identifier 4.5 name should be reused","plain\"""")

    test_reader = csv.DictReader(in_mem_csv, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL, skipinitialspace=True)
    with mock.patch('builtins.open') as m:
        violations = read_misra_violations("violations.csv", test_reader)

        m.assert_called_with('violations.csv', 'rt')

        assert 0 == len(violations)
