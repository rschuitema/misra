import pytest
from src.misra.violation import Violation
from src.misra.misra_guideline import MisraGuideline

def test_creation():
    theGuideline = MisraGuideline("id-123", "classification", "category", "group", "description")
   
    assert "id-123" == theGuideline.get_id()
    assert "classification" == theGuideline.get_classification()
    assert "category" == theGuideline.get_category()
    assert "group" == theGuideline.get_group()
    assert "description" == theGuideline.get_description()
    
