import pytest
from src.misra.violation import Violation
from src.misra.misra_guideline import MisraGuideline


@pytest.fixture
def default_violation():
    the_guideline = MisraGuideline(("id-123", "classification", "category", "group", "description"))
    the_violation = Violation("myfile.txt", "89", "12", the_guideline, "variable xyz")
    return the_violation, the_guideline


def test_creation(default_violation):
    the_violation, the_guideline = default_violation
    assert "myfile.txt" == the_violation.get_file()
    assert "89" == the_violation.get_line()
    assert "12" == the_violation.get_column()
    assert "variable xyz" == the_violation.get_entity()
    assert the_guideline == the_violation.get_guideline()


def test_get_set_file(default_violation):
    the_violation, the_guideline = default_violation

    the_violation.set_file("c:\\test\\hello.c")
    assert "c:\\test\\hello.c" == the_violation.get_file()


def test_get_set_line(default_violation):
    the_violation, the_guideline = default_violation

    the_violation.set_line("21")
    assert "21" == the_violation.get_line()


def test_get_set_column(default_violation):
    the_violation, the_guideline = default_violation

    the_violation.set_column("54")
    assert "54" == the_violation.get_column()


def test_get_set_entity(default_violation):
    the_violation, the_guideline = default_violation

    the_violation.set_entity("newEntity")
    assert "newEntity" == the_violation.get_entity()


def test_get_set_guideline(default_violation):
    the_violation, the_guideline = default_violation

    new_guideline = MisraGuideline(("newID", "newclass", "newcat", "newgroup", "new desc"))
    
    the_violation.set_guideline(new_guideline)
    assert new_guideline == the_violation.get_guideline()
    assert new_guideline != the_guideline

