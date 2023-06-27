from .models import FirstModel
from django.test import TestCase
from django.utils.text import slugify
from .utils import slugify_instance_title

# Create your tests here.
class FistModelTestCase(TestCase):
    # Django Use Pythons inbuilt unittest methods but with additional Future.
    # def test_anyName(self): # we can create any test by starting with 'test_'
    #     # if any assert Conditions fail then Test result will be failed
    #     self.assertTrue(1==1)
    #     self.assertFalse(1==2)
    #     self.assertIsNone(None)
    #     self.assertIsNotNone(not None)
    #     self.assertEqual(1,1)
    #     self.assertNotEqual(1,2)
    #     self.fail() use in try except to fail test_case

    def setUp(self):
        self.no_of_rows = 5
        for i in range(0, self.no_of_rows):
            FirstModel.objects.create(title='Hello World', content='something else')

    def test_queryset_exists(self):
        qs = FirstModel.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        qs = FirstModel.objects.all()
        self.assertEqual(qs.count(), self.no_of_rows)

    def test_slug(self):
        obj1 = FirstModel.objects.all().order_by('id').first() # '-id' will order this in desc order
        title = obj1.title
        slug = obj1.slug
        slugified_title = slugify(title)
        self.assertEqual(slug,slugified_title)

    def test_unique_slug(self):
        obj1 = FirstModel.objects.all().order_by('id').first()
        slug = obj1.slug
        qs = FirstModel.objects.exclude(slug__iexact=slug)
        for q in qs:
            self.assertNotEqual(q.slug, slug)

    # testing slugify method Video 42 remain
    def test_slugify_instance_title(self):
        pass


