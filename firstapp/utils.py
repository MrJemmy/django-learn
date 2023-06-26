import random
from django.utils.text import slugify

def slugify_instance_title(instance, save=False, new_slug = None):
    # we can improve below method. and also we can use DB table for tracking data
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        rand_int = random.randint(1, 500_000)
        slug = f"{slug}-{rand_int}"
        return slugify_instance_tutle(instance, new_slug=slug)
    instance.slug = slug
    # if save: # we can also perform this here
    #     instance.save()
    return instance