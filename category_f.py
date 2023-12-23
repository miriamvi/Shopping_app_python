import pandas as pd
import uuid

class Category:
    def __init__(self, name):
        self.category_id = uuid.uuid4()
        self.name = name
        self.products = []

    def __str__(self):
        return f"{self.name} (ID: {self.category_id})"