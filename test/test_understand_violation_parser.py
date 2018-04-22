from src.misra.misra_guideline import MisraGuideline
from src.parsers.understand_violation_parser import parse_understand_violations


def test_no_guidelines_no_violations_empty_guideline_violations():

    violations = []
    guidelines = {}

    guideline_violations = parse_understand_violations(violations, guidelines)

    assert 0 == len(guideline_violations)


def test_two_guideline_violations_success():

    violations = [('upgrade_image.c', 'Identifier plain reused', '963', '32', '1.1 Functions rule 1', 'plain'),
                  ('test.c', 'Wrong parameter list', '11', '22', '1.1 Functions rule 1', 'list')]

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Layout", "Functions rule 5"))}

    guideline_violations = parse_understand_violations(violations, guidelines)

    assert 2 == len(guideline_violations)


def test_rule_not_in_guidelines_empty_guideline_violations():

    violations = [('upgrade_image.c', 'Identifier plain reused', '963', '32', '3.1 Functions rule 1', 'plain'),
                  ('test.c', 'Wrong parameter list', '11', '22', '3.1 Functions rule 1', 'list')]

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Layout", "Functions rule 5"))}

    guideline_violations = parse_understand_violations(violations, guidelines)

    assert 0 == len(guideline_violations)


def test_wrong_rule_format_empty_guideline_violations():

    violations = [('upgrade_image.c', 'Identifier plain reused', '963', '32', '11 Functions rule 1', 'plain'),
                  ('test.c', 'Wrong parameter list', '11', '22', '11 Functions rule 1', 'list')]

    guidelines = {"1.1": MisraGuideline(("1.1", "rule", "Mandatory", "Functions", "Functions rule 1")),
                  "1.5": MisraGuideline(("1.5", "rule", "Mandatory", "Parameters", "Functions rule 2")),
                  "1.7": MisraGuideline(("1.7", "rule", "Mandatory", "Functions", "Functions rule 3")),
                  "2.1": MisraGuideline(("2.1", "rule", "Mandatory", "Layout", "Functions rule 4")),
                  "2.2": MisraGuideline(("2.2", "rule", "Mandatory", "Layout", "Functions rule 5"))}

    guideline_violations = parse_understand_violations(violations, guidelines)

    assert 0 == len(guideline_violations)

