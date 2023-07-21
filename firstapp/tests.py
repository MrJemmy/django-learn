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
        print(' -> Running SetUp')
        self.no_of_rows = 5
        for i in range(0, self.no_of_rows):
            FirstModel.objects.create(title='Hello World', content='something else')

    def test_queryset_exists(self):
        print('Running Test : test_queryset_exists')
        qs = FirstModel.objects.all()
        self.assertTrue(qs.exists())

    def test_queryset_count(self):
        print('Running Test : test_queryset_count')
        qs = FirstModel.objects.all()
        self.assertEqual(qs.count(), self.no_of_rows)

    def test_slug(self):
        print('Running Test : test_slug')
        obj1 = FirstModel.objects.all().order_by('id').first() # '-id' will order this in desc order
        title = obj1.title
        slug = obj1.slug
        slugified_title = slugify(title)
        self.assertEqual(slug,slugified_title)

    def test_unique_slug(self):
        print('Running Test : test_unique_slug')
        obj1 = FirstModel.objects.all().order_by('id').first()
        slug = obj1.slug
        qs = FirstModel.objects.exclude(slug__iexact=slug)
        for q in qs:
            self.assertNotEqual(q.slug, slug)

    # testing slugify method using below 2 functions : All Slugs are not Equal or not
    def test_slugify_instance_title(self):
        print('Running Test : test_slugify_instance_title')
        obj = FirstModel.objects.all().last()
        new_slug = []
        for i in range(0, self.no_of_rows):
            instance = slugify_instance_title(obj)
            new_slug.append(instance.slug)
        unique_slugs = list(set(new_slug))
        self.assertEqual(len(new_slug), len(unique_slugs))

    def test_slugify_instance_title_redux(self):
        print('Running Test : test_slugify_instance_title_redux')
        slug_list = FirstModel.objects.all().values_list('slug', flat=True)
        unique_slug_list = list(set(slug_list))
        self.assertEqual(len(slug_list), len(unique_slug_list))

    # if user change slug manually then it should also be unique  Write Test For That also
    # ---------------------------------------------------------------------------------- #

    def test_search_manager_query(self):
        print('Running Test : test_search_manager_query')
        qs = FirstModel.objects.search(query='hello')
        self.assertEqual(qs.count(), self.no_of_rows)


