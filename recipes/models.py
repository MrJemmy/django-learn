import pint
from django.conf import settings
from django.urls import reverse
from django.db import models
from .validators import validate_unit_of_measure
from .utils import number_str_to_float

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    directions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={'id':self.id})

    def get_update_url(self):
        return reverse("recipes:update", kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse("recipes:delete", kwargs={'id':self.id})

    @property
    def get_ingredients(self):
        ingredients = self.recipeingredient_set.all()
        return ingredients

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=50)  # 1 and 1/4
    quantity_as_float = models.FloatField(max_length=50, blank=True, null=True)  # 1.25
    unit = models.CharField(max_length=50, validators=[validate_unit_of_measure])  # KG, gram, pounds, lbs, spoon
    directions = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def get_delete_url(self):
        kwargs={
                'parent_id': self.recipe.id,
                'id': self.id
        }
        return reverse("recipes:ingredient-delete", kwargs=kwargs)

    # TODO : Because of conversion system [as_mks and as_imperial] it is working slow
    # it compute every time when we call detail page so it is taking time.
    def convert_to_system(self, system='mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        return measurement  # .to_base_units()

    def as_mks(self):
        # meter, kilogram, second
        measurement = self.convert_to_system(system='msk')
        print(f'kilogram : {measurement}')
        return measurement.to('kg')
        # return measurement.to_base_units()

    def as_imperial(self):
        # miles, pounds, second
        measurement = self.convert_to_system(system='imperial')
        print(f'pound : {measurement}')
        return measurement.to('pounds')
        # return measurement.to_base_units()

    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_success = number_str_to_float(qty)
        if qty_as_float_success:
            self.quantity_as_float = qty_as_float
        else:
            self.quantity_as_float = None
        super().save(*args, **kwargs)
