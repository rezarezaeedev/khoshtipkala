from django.utils.text import slugify
import random
import string

def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_unique_string_id(instance,size=5):
    objid=random_string_generator(size)
    klass=instance.__class__
    if not klass.objects.filter(objid=objid).exists():
        return objid
    else:
        return get_unique_string_id(instance)
