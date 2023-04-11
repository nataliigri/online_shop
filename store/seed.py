from .models import Product
from faker import Facer
fake = Facer()

def seed_db(n)
    for i in range(0,n):
        Product.objects.create(
            name = fake.name(),
            slug = fake.name()
        )