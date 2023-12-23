import pandas as pd
import uuid

from category_f import Category
from catalog_f import Catalog
from product_f import Product

class Admin:
    admins_db = {'a1': 'p1', 'admin2': 'adminpass2', 'admin3': 'adminpass3'}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.session_id = None
    def create_admin(self):
        pass

    def login(self):
        if self.username in Admin.admins_db and Admin.admins_db[self.username] == self.password:
            self.session_id = str(uuid.uuid4())
            print(f"\nAdmin '{self.username}' logged in with session ID: {self.session_id}")
        else:
            print("\n           Invalid username or password. Please try again.")
        return self.session_id

    def add_category(self, catalog, name):
        if self.session_id is None:
            print("\n           Admin must log in first.")
            return

        new_category = Category(name)
        catalog.add_category(new_category)
        print(f"\nCategory '{name}' added to the catalog.")

    def remove_category(self, catalog, category_name):
        if self.session_id is None:
            print("\n           Admin must log in first.")
            return

        catalog.remove_category(category_name)
            
    def add_product(self, catalog, name, category_name, price):
        if self.session_id is None:
            print("\n           Admin must log in first.")
            return
        # Find category object
        category = next((cat for cat in catalog.categories if cat.name == category_name), None)
        if category is None:
            print(f"\n          Category '{category_name}' not found. Create the category first.")
            return
        
        new_product = Product(name, category, price)
        catalog.add_product(new_product)
        print(f"\nProduct '{name}' added to the catalog in category '{category_name}'.")

    def remove_product(self, catalog, product_id):
        if self.session_id is None:
            print("\n           Admin must log in first.")
            return

        catalog.remove_product(product_id)

