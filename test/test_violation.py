import pytest
from src.misra.violation import Violation
from src.misra.misra_guideline import MisraGuideline

@pytest.fixture
def defaultViolation():
    theGuideline = MisraGuideline("id-123", "classification", "category", "group", "description")
    theViolation = Violation("myfile.txt", "89", "12", theGuideline, "variable xyz")
    return theViolation, theGuideline

def test_creation(defaultViolation):
    theViolation, theGuideline = defaultViolation
    assert "myfile.txt" == theViolation.get_file()
    assert "89" == theViolation.get_line()
    assert "12" == theViolation.get_column()
    assert "variable xyz" == theViolation.get_entity()
    assert theGuideline == theViolation.get_guideline()

    
def test_get_set_file(defaultViolation):
    theViolation, theGuideline = defaultViolation

    theViolation.set_file("c:\\test\\hello.c") 
    assert "c:\\test\\hello.c" == theViolation.get_file()
    
def test_get_set_line(defaultViolation):
    theViolation, theGuideline = defaultViolation

    theViolation.set_line("21") 
    assert "21" == theViolation.get_line()

def test_get_set_column(defaultViolation):
    theViolation, theGuideline = defaultViolation

    theViolation.set_column("54") 
    assert "54" == theViolation.get_column()
