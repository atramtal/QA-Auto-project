import pytest


@pytest.mark.check  # маркування тестів, перевіряє правильність імені та прізвища
def test_change_name(user):
    assert user.name == 'Marta'

@pytest.mark.check
def test_change_second_name(user):
    assert user.second_name == 'Talover'
