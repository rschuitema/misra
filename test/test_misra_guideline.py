import pytest
from src.misra.violation import Violation
from src.misra.misra_guideline import MisraGuideline


def test_creation():
    the_guideline = MisraGuideline(("id-123", "classification", "category", "group", "description"))
   
    assert "id-123" == the_guideline.get_id()
    assert "classification" == the_guideline.get_classification()
    assert "category" == the_guideline.get_category()
    assert "group" == the_guideline.get_group()
    assert "description" == the_guideline.get_description()
