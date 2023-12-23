from catalog_f import Catalog
from category_f import Category
from product_f import Product
from cartitem_f import CartItem
from user_f import User
from admin_f import Admin

import pandas as pd
import uuid
import time

def create_demo_database():
    # Create an instance of the Catalog class
    catalog = Catalog()

    # Sample usage with initial data
    initial_data = [
        {
            'name': 'Footwear',
            'products': [
                {'name': 'Boots', 'price': 100.0},
                {'name': 'Sneakers', 'price': 80.0},
                {'name': 'Sandals', 'price': 30.0}
            ]
        },
        {
            'name': 'Clothing',
            'products': [
                {'name': 'Coats', 'price': 120.0},
                {'name': 'Jacket', 'price': 100.0},
                {'name': 'T-Shirt', 'price': 20.0}
            ]
        },
        {
            'name': 'Electronics',
            'products': [
                {'name': 'Laptop', 'price': 1000.0},
                {'name': 'Smartphone', 'price': 500.0},
                {'name': 'Headphones', 'price': 100.0}
            ]
        },
    ]

    # Populate the catalog with initial data
    for category_data in initial_data:
        category = Category(category_data['name'])

        for product_data in category_data['products']:
            product = Product(product_data['name'], category, product_data['price'])
            category.products.append(product)
            # Add the product to the catalog
            catalog.add_product(product)
        catalog.add_category(category)

    return catalog

def welcome_message():
    print("""
          

          Welcome to the Demo Marketplace!

          """)

def main():    
    # Create an instance of the Catalog class
    catalog = create_demo_database()
    welcome_message()
    
    while True: 
        print(
            """
        1. User Login
        2. Admin Login
        3. Exit
        """
        )
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("\n           Please enter a valid choice.")
            continue
        if choice == 1:
            #user login  
            user_name=str(input("username: ")) 
            pwd=str(input("password: ")) 
            user=User(user_name,pwd)
            session=user.login()
            if session:
                while True:
                    print(
                    """
                        1. View catalog
                        2. Add to cart
                        3. Remove from cart
                        4. View Cart
                        5. Pay
                        6. Exit
                    """
                    )
                    try:
                        ch = int(input("Enter choice: "))
                    except ValueError:
                        print("\n           Please enter a valid choice.")
                        continue
                    if ch == 1:
                        catalog.display_catalog()
                    elif ch == 2:
                        catalog.display_catalog()
                        try:
                            product_idx = int(input("\nSelect the product number to add to your cart: "))
                            if 0 <= product_idx < len(catalog.p_catalog):
                                quantity = int(input("Enter quantity: "))
                                if quantity > 0:
                                    selected_product = catalog.p_catalog.iloc[product_idx]
                                    product = Product(selected_product['name'], Category(selected_product['category']), selected_product['price'])
                                    user.add_to_cart(product, quantity)
                                else:
                                    print("\n         Quantity should be greater than zero.")      
                            else:
                                print("\n           Invalid product number.")
                        except ValueError:
                            print("\n           Please enter a valid number.")
                    elif ch == 3:
                        user.view_cart()
                        try:
                            cart_idx_remove = int(input("\nSelect the product number you want to remove from your cart: "))
                            if 0 <= cart_idx_remove < len(user.cart):
                                qty_remove = int(input("\nSelect the quantity to remove: "))
                                if qty_remove > 0:
                                    product_id = user.cart[cart_idx_remove].product.product_id
                                    user.remove_from_cart(product_id, qty_remove)
                                else:
                                    print("\n         Quantity should be greater than zero.")   
                            else:
                                print("\n         Invalid cart index.")
                        except ValueError:
                            print("\n         Please enter a valid number.")
                    elif ch == 4:
                        user.view_cart()
                    elif ch == 5:
                        user.process_payment()
                    elif ch == 6:
                        print("\n\n\n         Good Bye")
                        break
                    else:
                        print("\n         Invalid choice. Please try again.")

        elif choice == 2:
            #admin login
            admin_name=str(input("admin_name: ")) 
            pwd=str(input("password: ")) 
            admin=Admin(admin_name,pwd)
            session=admin.login()
            if session:
                while True:
                    print(
                    """
                        1. Add Category 
                        2. Remove Category
                        3. Add Product
                        4. Remove Product
                        5. View Catalog
                        6. Exit
                    """
                    )
                    try:    
                        ch = int(input("\nEnter choice: "))
                    except ValueError:
                        print("\n           Please enter a valid choice.")
                        continue
                    if ch == 1:
                        catalog.display_categories()
                        new_cat=input("\nName of the new category:").title()
                        admin.add_category(catalog, new_cat)
                    elif ch == 2:
                        catalog.display_categories()
                        try:
                            category_idx = int(input("\nSelect the index of the category to remove: "))
                            if 0 <= category_idx < len(catalog.categories):
                                category_to_remove = catalog.categories[category_idx]
                                catalog.remove_category(category_to_remove.name)
                            else:
                                print("\n         Invalid category index.")
                        except ValueError:
                            print("\nPlease enter a valid number.")
                    elif ch == 3:
                        new_prod = input("\nName of the new product:").title()
                        new_p_category = input("Category name:").title()
                        try:
                            new_p_price=float(input("Price:"))
                            admin.add_product(catalog,new_prod,new_p_category,new_p_price)
                        except ValueError:
                            print("\n           Please enter a valid price.")
                    elif ch == 4:
                        catalog.display_catalog()
                        try:
                            product_idx = int(input("Select the product number to remove: "))
                            if 0 <= product_idx < len(catalog.p_catalog):
                                selected_product_id = catalog.p_catalog.iloc[product_idx]['product_id']
                                admin.remove_product(catalog, selected_product_id)  
                            else:
                                print("\n         Invalid product number.")
                        except ValueError:
                            print("\n         Please enter a valid number.")
                    elif ch ==5:
                        catalog.display_catalog()
                        catalog.display_categories()
                    elif ch == 6:
                        print("Good Bye")
                        break
                    else:
                        print("\n         Invalid choice. Please try again.")

        elif choice == 3:
            print("\n\n\n         Good Bye")
            break
        else:
            print("\n         Invalid choice. Please try again.")
   

if __name__ == "__main__":
    main()
