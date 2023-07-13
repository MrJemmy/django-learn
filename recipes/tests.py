from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Recipe, RecipeIngredient
from django.core.exceptions import ValidationError

# Create your tests here.
User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('jaiminpatel', password='8609')

    def test_user_pw(self):
        checked = self.user_a.check_password('8609')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.number_of_recipe = 2
        self.no_of_ingredient_for_recipe_a = 2
        self.no_of_ingredient_for_recipe_b = 0
        self.user_a = User.objects.create_user('jaiminpatel', password='8609')
        self.recipe_a = Recipe.objects.create(
            name='Khichdi',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Dal Bhat',
            user=self.user_a
        )
        self.recipe_ingredient_a = RecipeIngredient.objects.create(
            name='Rice',
            quantity='1  1/2',  # double space works check how?
            unit='grams',
            recipe=self.recipe_a
        )
        self.recipe_ingredient_b = RecipeIngredient.objects.create(
            name='water',
            quantity='5 kilo',
            unit='liter',
            recipe=self.recipe_a
        )

    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a
        qs = user.recipe_set.all()  # ModelName_set
        self.assertEqual(qs.count(), self.number_of_recipe)

    def test_user_recipe_forward_count(self):
        user = self.user_a
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), self.number_of_recipe)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a
        qs = recipe.recipeingredient_set.all()  # ModelName_set
        self.assertEqual(qs.count(), self.no_of_ingredient_for_recipe_a)

    def test_recipe_ingredient_forward_count(self):
        recipe = self.recipe_a
        qs = RecipeIngredient.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), self.no_of_ingredient_for_recipe_a)

    def test_user_two_level_forward_relation(self):
        user = self.user_a
        qs = RecipeIngredient.objects.filter(recipe__user=user)
        # qs = RecipeIngredientImages.objects.filter(recipeingredient__recipe__user=user)  # This is 3 Level Relation ship
        self.assertEqual(qs.count(), self.no_of_ingredient_for_recipe_a)

    def test_user_two_level_reverse_relation(self):
        # try to avoid 2 level reverse relations
        user = self.user_a
        recipe_ingredient_ids = user.recipe_set.all().values_list('recipeingredient__id', flat=True)
        qs = RecipeIngredient.objects.filter(recipe__in=recipe_ingredient_ids)
        self.assertEqual(qs.count(),  self.no_of_ingredient_for_recipe_a)  # user

    def test_user_two_level_reverse_relation_via_recipes(self):
        # this is a better way to use reverse relation
        user = self.user_a
        recipe_ids = user.recipe_set.all().values_list('id', flat=True)
        qs = RecipeIngredient.objects.filter(recipe__id__in=recipe_ids)
        self.assertEqual(qs.count(),  self.no_of_ingredient_for_recipe_a)  # user

    # Testing Validation
    def test_unit_measure_validation(self):
        invalid_unit = 'kg'
        ingredient = RecipeIngredient(
            name='Test',
            quantity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_unit = ['spoon', 'package']
        with self.assertRaises(ValidationError):  # This will raise an error when Error is not Raised
            for unit in invalid_unit:
                ingredient = RecipeIngredient(
                    name='Test',
                    quantity=10,
                    recipe=self.recipe_a,
                    unit=unit
                )
                ingredient.full_clean()  # it does all process but skip only .save() method
                # ingredient.save()  # unit are invalid still .save is not create a validation error

    def test_quantity_as_float(self):
        self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
        self.assertIsNone(self.recipe_ingredient_b.quantity_as_float)