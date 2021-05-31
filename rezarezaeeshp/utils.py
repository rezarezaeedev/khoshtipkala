import itertools

from django.utils.text import slugify
import random
import string
from datetime import datetime


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
                    slug=slug,
                    randstr=random_string_generator(size=4)
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

# get date & time for DateTimeField()
def get_currnet_time():
    current_time = datetime.now()
    date_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    return date_time

# get price seperated : 10000000 -> 10,000,000
def price_seperator(price):
    return f"{price:,}"

# get grouped list ,for gallery or recomended products
def list_grouper(n, iterable):
    args = [iter(iterable)] * n
    return list(([e for e in t if e != None] for t in itertools.zip_longest(*args)))

# get a url with good seo ,because replace any space with dash character 
def get_seo_url(url,char='-',oldchar=' '):
    return url.replace(oldchar, char)

