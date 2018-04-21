from src.misra.misra_guideline import MisraGuideline
from src.queries.violations_per_category import get_violations_per_category


def test_violations_per_category_success():

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Required", "Functions", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Required", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Advisory", "Functions", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Advisory", "Functions", "Functions rule 5"))}

    guideline_violations = [
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Advisory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Advisory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.7", "rule", "Required", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
    ]

    violations_per_category = get_violations_per_category(guideline_violations, guidelines)

    assert 3 == len(violations_per_category)
    assert 4 == violations_per_category["Mandatory"]
    assert 1 == violations_per_category["Required"]
    assert 2 == violations_per_category["Advisory"]


def test_no_violations_all_counts_are_zero():

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Required", "Functions", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Required", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Advisory", "Functions", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Advisory", "Functions", "Functions rule 5"))}

    guideline_violations = []

    violations_per_category = get_violations_per_category(guideline_violations, guidelines)

    assert 3 == len(violations_per_category)
    assert 0 == violations_per_category["Mandatory"]
    assert 0 == violations_per_category["Required"]
    assert 0 == violations_per_category["Advisory"]


def test_no_guidelines_empty_violations_per_rule():

    guidelines = {}

    guideline_violations = [
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Advisory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("2.1", "rule", "Advisory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.7", "rule", "Required", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
        (MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")), "test.c", "12", "34", "var"),
    ]

    violations_per_category = get_violations_per_category(guideline_violations, guidelines)

    assert 0 == len(violations_per_category)
