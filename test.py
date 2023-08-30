import pytest
from unittest.mock import patch
from python_assignment import add_customer, customers


@patch("builtins.input", side_effect=["abc", "123", "abc@abc.com"])
def test_add_customer(mocked_input):
    global customers
    add_customer()
    assert customers[0]["name"] == "abc"
    assert customers[0]["telephone"] == "123"
    assert customers[0]["email"] == "abc@abc.com"
