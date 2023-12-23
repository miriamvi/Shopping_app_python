import uuid
import pandas as pd

class Product:
    def __init__(self, name, category, price):
        self.product_id = uuid.uuid4()
        self.name = name
        self.category = category
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}, Category: {self.category.name}, Price: ${self.price:.2f})"
