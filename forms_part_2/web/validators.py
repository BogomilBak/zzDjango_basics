from typing import Any
from django import forms
from django.utils.deconstruct import deconstructible


def validate_text(value):
    if "_" in value:
        raise forms.ValidationError("invalid character is _")
    
def validate_priority(value):
    if value < 1 or 10 < value:
        raise forms.ValidationError("Wrong value")
    
@deconstructible
class ValueInRangeValidator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if value < self.min_value or self.max_value < value:
            raise forms.ValidationError(f"Value must be brtween {self.min_value} and {self.max_value}")
        
    def __eq__(self, other):
        return (
            isinstance(other, self.__class__)
            and self.min_value == other.min_value
            and self.max_value == other.max_value
        )