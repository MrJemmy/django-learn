# inserted using -->> python manage.py shell
from restframeworklearn.models import Product

# No need to save when we are using create
Product.objects.create(title='Hello Jaimin', content='telling Hello to jaimin', price=26.14)
Product.objects.create(title='Hello Gunjan', content='telling Hello to Gunjan', price=26.14)
Product.objects.create(title='Hello Raj', content='telling Hello to Raj', price=11.11)
Product.objects.create(title='Hello Prince', content='telling Hello to Prince', price=100.00)
Product.objects.create(title='Hello Shivam', content='telling Hello to Shivam', price=12.12)

# to get random data
random_entry = Product.objects.all().order_by('?').first()
#
# # How we run property of models
fist_entry_amt = Product.objects.first().sale_price
last_entry_amt = Product.objects.last().sale_price