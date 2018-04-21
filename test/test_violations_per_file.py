from src.misra.misra_guideline import MisraGuideline
from src.queries.violations_per_file import get_violations_per_file


def test_violations_per_file_success():

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Layout", "Functions rule 5"))}

    guideline_violations = [
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 1")), "welcome.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "welcome.c", "12", "34", "var"),
        (MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 1")), "welcome.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "hello.c", "12", "34", "var"),
        (MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 1")), "test.c", "12", "34", "var"),
    ]

    violations_per_file = get_violations_per_file(guideline_violations, guidelines)

    assert 3 == len(violations_per_file)
    assert 1 == violations_per_file['hello.c']
    assert 3 == violations_per_file['welcome.c']
    assert 3 == violations_per_file['test.c']


def test_no_violations_empty_violations_per_file():

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Layout", "Functions rule 5"))}

    guideline_violations = []

    violations_per_file = get_violations_per_file(guideline_violations, guidelines)

    assert 0 == len(violations_per_file)


def test_no_guidelines_empty_violations_per_file():

    guidelines = {}

    guideline_violations = [
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 1")), "welcome.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "welcome.c", "12", "34", "var"),
        (MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 1")), "welcome.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "hello.c", "12", "34", "var"),
        (MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 1")), "test.c", "12", "34", "var"),
    ]

    violations_per_file = get_violations_per_file(guideline_violations, guidelines)

    assert 0 == len(violations_per_file)
