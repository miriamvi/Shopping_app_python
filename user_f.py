import pandas as pd
import uuid
import time

from cartitem_f import CartItem

class User:
    users_db = {'u1': 'p1', 'user2': 'password2', 'user3': 'password3'}
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cart = []
        self.session_id = None

    def create_user(self):
        pass

    def login(self):
        if self.username in User.users_db and User.users_db[self.username] == self.password:
            self.session_id = str(uuid.uuid4())
            print(f"Welcome! '{self.username}'")
        else:
            print("\n           Invalid username or password. Please try again.")

        return self.session_id
    def add_to_cart(self, product, quantity=1):
        if self.session_id is None:
            print("\n           User must log in first.")
            return
        if quantity <= 0:
            print("\n           Quantity should be greater than zero.")
            return
        self.cart.append(CartItem(product, quantity))
        print(f"\n{quantity} {product.name}(s) added to your cart.")

    def remove_from_cart(self, product_id, quantity_to_remove=1):
        if self.session_id is None:
            print("\n           User must log in first.")
            return
        if quantity_to_remove <= 0:
            print("\n           Quantity to remove should be greater than zero.")
            return

        for item in self.cart:
            if item.product.product_id == product_id:
                if item.quantity <= quantity_to_remove:
                    self.cart.remove(item)
                    print(f"\n{item.quantity} {item.product.name}(s) removed from your cart.")
                else:
                    item.quantity -= quantity_to_remove
                    print(f"\n{quantity_to_remove} {item.product.name}(s) removed from your cart.")
                break
        else:
            print("\n           Product not found in your cart.")

    def view_cart(self):
        if self.session_id is None:
            print("\n           User must log in first.")
            return
        if not self.cart:
            print("\n           Your cart is empty.")
        else:
            print("\nYour Cart:")
            for idx, item in enumerate(self.cart):
                            product = item.product
                            print(f"{idx}: {product.name} - Quantity: {item.quantity} - Price: ${product.price:.2f} - Total: ${item.quantity*product.price}")
            total_price = sum(item.product.price * item.quantity for item in self.cart)
            print(f"Total amount to pay: ${total_price:.2f}")
            
    def process_payment(self):
        if self.session_id is None:
            print("\n           User must log in first.")
            return

        if not self.cart:
            print("\n           Your cart is empty. Add items before processing payment.")
            return

        total_price = sum(item.product.price * item.quantity for item in self.cart)

        print(f"\nTotal amount to pay: ${total_price:.2f}")

        # Prompt the user to select a payment option
        print(
        """
            Select a payment option:
            1. Net Banking
            2. Credit Card
            3. PayPal
            4. UPI
        """
        )

        payment_option=int(input("\nSelect your payment option:"))

        # Assume the user selects option 4 for UPI
        if payment_option == 4:
            print("\nYou will be shortly redirected to the portal for Unified Payment Interface.")
            time.sleep(1)
        elif payment_option ==3:
             print("\nYou will be shortly redirected to the portal for PayPal.")
             time.sleep(1)
        
        # Simulate processing payment
        print(f"\nProcessing payment using {payment_option}...")
        time.sleep(1)  # Simulating payment processing time

        print("\nPayment successful! Your order is successfully placed.")

        # Clear the user's cart after successful payment
        self.cart = []
