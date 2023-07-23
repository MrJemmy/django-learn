import pint
from django.core.exceptions import ValidationError
from pint.errors import UndefinedUnitError

# litres, millilitres, grams, kilograms, pounds
valid_unit_measurements = ['pounds', 'lbs','oz', 'gram']

def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f"'{value}' is not valid unit of measure")
    except Exception as e:
        raise ValidationError(f"'{value}' is giving Unknown error {e} ")
    # if value not in valid_unit_measurements:
    #     raise ValidationError(f'{value} is not a valid unit of measure')