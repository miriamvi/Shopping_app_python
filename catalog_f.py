import pandas as pd

from category_f import Category

class Catalog:
    def __init__(self):
        self.p_catalog = pd.DataFrame(columns=['product_id', 'name', 'category', 'price'])
        self.categories = []

    def add_product(self, product):
        new_row = pd.DataFrame([{
            'product_id': product.product_id,
            'name': product.name,
            'category': product.category.name,
            'price': product.price
        }])
        self.p_catalog = pd.concat([self.p_catalog, new_row], ignore_index=True)
        
        

    def remove_product(self, product_id):
        if product_id in self.p_catalog['product_id'].unique():
            self.p_catalog = self.p_catalog[self.p_catalog['product_id'] != product_id]
            # Reset the index of the DataFrame
            self.p_catalog.reset_index(drop=True, inplace=True)
            print(f"\n          Product with ID '{product_id}' removed from the catalog.")
        else:
            print("\n           Product not found in the catalog.")

    def add_category(self, category):
        # Check if the category already exists
        if category.name in [cat.name for cat in self.categories]:
            print(f"\n          Category '{category.name}' already exists.")
            return
        self.categories.append(category)

    def remove_category(self, category_name):
        for category in self.categories:
            if category.name == category_name:
                # Remove the category and its products
                self.categories.remove(category)
                self.p_catalog = self.p_catalog[self.p_catalog['category'] != category_name]
                self.p_catalog.reset_index(drop=True, inplace=True)
                print(f"\n          Category '{category_name}' and its products removed.")
                break
        else:
            print("\n           Category not found.")
    def display_catalog(self):
        print("\nProduct Catalog:")
        if self.p_catalog.empty:
            print("\n           The catalog is empty.")
        else:
            #print(self.p_catalog[['name', 'category', 'price']])
            for idx, row in self.p_catalog.iterrows():
                print(f"{idx}: {row['name']} - {row['category']} - ${row['price']:.2f}")
    def display_categories(self):
        print("\nCategories:")
        if not self.categories:  # Check if the categories list is empty
            print("\n           There are no categories.")
        else:
            for idx, category in enumerate(self.categories):
                print(f"{idx}: {category.name}")
