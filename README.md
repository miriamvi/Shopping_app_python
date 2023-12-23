### Creating a Shopping App Using Python
#### 1.	Introduction
The Shopping App project was developed to simplify the shopping experience for users. This app contains login features for users and administrators. It enables users to browse products, manage their shopping carts, and process payments, supporting a variety of payment options. The app contains a demo catalog, but this app enables the admin to manage the catalog by adding and removing products and categories. 
#### 2.	Scope
The shopping app supports the backend implementation using Python. UX/UI and database connectivity are not supported. Nevertheless, the app provides interactive functionality, creating a user-friendly interface and a robust backend with error handling.
#### 3.	Project Description
The Shopping App is a comprehensive application designed to provide an online shopping experience. Components:
###### Catalog Class: 
- Functionality: Serves as the central repository of all products and categories. It uses a pandas DataFrame (‘p_catalog’) to store product information, including product IDs, names, categories, and prices. The class provides functionalities to add or remove products and categories and to display the current catalog, and categories.
- Attributes: Maintains a pandas DataFrame (‘p_catalog’) for product details and a list (‘categories’) for category objects.
- Error Handling: Checks for the existence of products and categories before adding or removing them to prevent duplicates or removing non-existent items. Resets the DataFrame index after product removal to maintain consistent indexing.
###### Product Class: 
- Functionality: Represents individual products with attributes such as name, category, and price. Each product is assigned a unique ID upon creation.
- Attributes: Includes ‘product_id’, ‘name’, ‘category’, and ‘price’.
###### Category Class: 
- Functionality: Represents different categories of products. Each category has a unique ID and a name and can contain multiple products.
- Attributes: Has a unique ‘category_id’, ‘name’, and a list of products (‘products’).
###### Admin Class: 
- Functionality: Manages administrative functions such as adding or removing products and categories from the catalog.
- Login System: Includes a login function with authentication against a predefined list of admins.
- Error Handling: Checks for admin login status before performing any administrative action. Provides feedback on unsuccessful operations (e.g., trying to add a duplicate category or remove a non-existent product).

###### User Class: 
- Functionality: Manages customer interactions, including shopping cart operations.
- Login System: Authenticates users against a predefined list.
- Shopping Cart: Manages a list of CartItem objects.
- Error Handling: Checks for login status, validates quantity inputs, and ensures cart operations (addition/removal) are performed on valid items.
###### CartItem Class: 
- Functionality: Represents items in a user's shopping cart, including the product and quantity.
- Attributes: Includes a product object and a quantity.
###### Main Execution Logic:
The main function serves as the entry point of the application. It creates a demo catalog with initial data and provides a menu-driven interface for users and admins. After logging in, users can view the catalog, manage their shopping cart, and process payments. Upon logging in, Admins can add or remove products and categories and view the current catalog.
- User Operations: Users can browse the catalog, add products to their cart by selecting them via their index, adjust quantities, remove items, view their cart with total pricing, and proceed to a simulated payment process.
- Admin Operations: Admins can add new categories and products to the catalog, remove existing ones, and view the updated catalog and category lists. They interact with the catalog through the provided options, ensuring a dynamic environment.
- Functional Flow: Upon launching the application, users are greeted with options to log in as a user or an admin or to exit the application. The user and admin functionalities are encapsulated within their respective loops, providing a continuous experience until the user decides to exit.
- Error Handling:
1. Input Validation: Includes checks for valid numeric input where required (e.g., product index, quantity).
2. Session Validation: Ensures that user and admin operations are accessible only after successful login.
3. Boundary Checks: Verifies user inputs against valid ranges (e.g., product index within the catalog range).
4. Feedback Mechanism: Provides users and admins with appropriate feedback messages for every operation, including errors and successful actions.
#### 4.	Results
The Shopping App delivers a user-friendly shopping platform. All the guidelines are successfully implemented:
- A welcome message is initially displayed.
- User and Admin login are created.
- The demo database was created according to the requirements.
- User login rights include viewing cart contents, adding items to carts, and removing items from carts. The user should be able to add items or delete items in the cart.
- The app provides demo payment checkout options and simulates the payment process.
- Admin Login rights include the ability to remove/add products and categories in the catalog.
- Admin does not interfere with the user functions, and the user cannot perform the admin functions.

