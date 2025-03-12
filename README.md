# Electronic Device Shopping Cart

## Overview
This is a Python-based shopping cart system for electronic devices, implementing Object-Oriented Programming (OOP) concepts such as inheritance and encapsulation. The system allows customers to browse, add devices to a shopping cart, and proceed to checkout while managing stock and applying discounts.

## Features
- **Device Management**: Includes Smartphones, Laptops, and Tablets, each with unique attributes.
- **Shopping Cart**: Users can add and remove devices from the cart.
- **Stock Management**: Ensures stock availability before purchases.
- **Discount Application**: Allows applying discounts to device prices.
- **Checkout System**: Calculates total price and updates stock upon purchase.

## Classes and Attributes

### `Device` (Base Class)
**Attributes:**
- `name`: Device name
- `price`: Price of the device
- `stock`: Stock availability
- `warranty_period`: Warranty period in months

**Methods:**
- `display_info()`: Shows device details
- `apply_discount(discount_percentage)`: Applies a discount to the price
- `is_available(amount)`: Checks stock availability
- `reduce_stock(amount)`: Reduces stock when an item is purchased

### `Smartphone` (Inherits from Device)
**Additional Attributes:**
- `screen_size`: Screen size in inches
- `battery_life`: Battery life in hours

**Additional Methods:**
- `make_call()`: Simulates making a call
- `install_app()`: Simulates installing an app

### `Laptop` (Inherits from Device)
**Additional Attributes:**
- `ram_size`: RAM size in GB
- `processor_speed`: Processor speed in GHz

**Additional Methods:**
- `run_program()`: Simulates running a program
- `use_keyboard()`: Simulates typing

### `Tablet` (Inherits from Device)
**Additional Attributes:**
- `screen_resolution`: Screen resolution
- `weight`: Weight in grams

**Additional Methods:**
- `browse_internet()`: Simulates browsing the internet
- `use_touchscreen()`: Simulates touchscreen navigation

### `Cart`
**Attributes:**
- `items`: List of items added to the cart
- `total_price`: Total price of items in the cart

**Methods:**
- `add_device(device, amount)`: Adds a device to the cart
- `remove_device(device, amount)`: Removes a device from the cart
- `get_total_price()`: Returns total cart price
- `print_items()`: Displays items in the cart
- `checkout()`: Finalizes the purchase and updates stock

## How to Run the Program
1. Clone the repository:
   ```sh
   git clone <https://github.com/MamashovMirbek/OOP-5/blob/main/main.py>
   ```
2. Navigate to the project folder:
   ```sh
   cd electronic-device-shopping-cart
   ```
3. Run the Python script:
   ```sh
   python main.py
   ```
4. Use the menu options to browse devices, add them to the cart, and proceed to checkout.

## Sample Input/Output
```
Menu:
1. Show Devices
2. Show Cart
3. Exit
Enter your choice: 1

1. iPhone 13 - $999 - Stock: 10
2. MacBook Pro - $1999 - Stock: 5
3. iPad Pro - $799 - Stock: 8
Select a device to add to cart: 1
Enter quantity: 2

Your Cart:
iPhone 13 - Quantity: 2
Total Price: $1998
Proceed to checkout? (y/n): y

Receipt:
iPhone 13 - Quantity: 2
Total Price: $1998
```

## UML Class Diagram
*`UML.txt`*

## Repository Contents
- `main.py`: Main program file
- `README.md`: Documentation
- `UML.txt`: Class diagram
