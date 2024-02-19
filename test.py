# test.py

import pytest
from main import StudentsInMLOps

@pytest.fixture
def mlops_instance():
    return StudentsInMLOps()

def test_enrollStudents(mlops_instance):
    mlops_instance.enrollStudents(10)
    assert mlops_instance.getTotalStrength() == 10

def test_dropStudents(mlops_instance):
    mlops_instance.enrollStudents(15)
    mlops_instance.dropStudents(5)
    assert mlops_instance.getTotalStrength() == 10

def test_dropStudents_error(mlops_instance):
    mlops_instance.enrollStudents(5)
    with pytest.raises(ValueError, match="Error: Cannot drop more students than the total strength."):
        mlops_instance.dropStudents(10)

def test_getClassName(mlops_instance):
    assert mlops_instance.getClassName() == "MLOps"
