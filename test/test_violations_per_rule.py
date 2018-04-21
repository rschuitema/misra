from src.misra.misra_guideline import MisraGuideline
from src.queries.violations_per_rule import get_violations_per_rule


def test_violations_per_rule_success():

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Functions", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Functions", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Functions", "Functions rule 5"))}

    guideline_violations = [
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
    ]

    violations_per_rule = get_violations_per_rule(guideline_violations, guidelines)

    assert 5 == len(violations_per_rule)
    assert 4 == violations_per_rule["1.1"]
    assert 2 == violations_per_rule["2.1"]
    assert 1 == violations_per_rule["1.7"]
    assert 0 == violations_per_rule["2.2"]
    assert 0 == violations_per_rule["1.5"]


def test_no_violations_all_counts_are_zero():

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Functions", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Functions", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Functions", "Functions rule 5"))}

    guideline_violations = []

    violations_per_rule = get_violations_per_rule(guideline_violations, guidelines)

    assert 5 == len(violations_per_rule)
    assert 0 == violations_per_rule["2.2"]
    assert 0 == violations_per_rule["1.5"]
    assert 0 == violations_per_rule["2.1"]
    assert 0 == violations_per_rule["1.7"]
    assert 0 == violations_per_rule["1.1"]


def test_no_guidelines_empty_violations_per_rule():

    guidelines = {}

    guideline_violations = [
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
    ]

    violations_per_rule = get_violations_per_rule(guideline_violations, guidelines)

    assert 0 == len(violations_per_rule)
