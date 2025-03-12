import sys


class Device:
    def __init__(self, name, price, stock, warranty_period):
        self.name = name
        self.price = price
        self.stock = stock
        self.warranty_period = warranty_period

    def display_info(self):
        return f"Name: {self.name}, Price: ${self.price}, Stock: {self.stock}, Warranty: {self.warranty_period} months"

    def __str__(self):
        return self.display_info()

    def apply_discount(self, discount_percentage):
        self.price *= (1 - discount_percentage / 100)

    def is_available(self, amount):
        return self.stock >= amount

    def reduce_stock(self, amount):
        if self.is_available(amount):
            self.stock -= amount
        else:
            raise ValueError("Insufficient stock")


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period, screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return f"{super().__str__()}, Screen Size: {self.screen_size} inches, Battery Life: {self.battery_life} hours"

    def make_call(self):
        return f"Making a call on {self.name}"

    def install_app(self):
        return f"Installing an app on {self.name}"


class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period, ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return f"{super().__str__()}, RAM Size: {self.ram_size} GB, Processor Speed: {self.processor_speed} GHz"

    def run_program(self):
        return f"Running a program on {self.name}"

    def use_keyboard(self):
        return f"Typing on the keyboard on {self.name}"


class Tablet(Device):
    def __init__(self, name, price, stock, warranty_period, screen_resolution, weight):
        super().__init__(name, price, stock, warranty_period)
        self.screen_resolution = screen_resolution
        self.weight = weight

    def __str__(self):
        return f"{super().__str__()}, Screen Resolution: {self.screen_resolution}, Weight: {self.weight} grams"

    def browse_internet(self):
        return f"Browsing the internet on {self.name}"

    def use_touchscreen(self):
        return f"Using the touchscreen on {self.name}"


class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if device.is_available(amount):
            self.items.append((device, amount))
            self.total_price += device.price * amount
            device.reduce_stock(amount)
        else:
            print(f"Error: Not enough stock for {device.name}")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if item[1] >= amount:
                    self.items.remove(item)
                    self.total_price -= device.price * amount
                    device.stock += amount
                else:
                    print(f"Error: Cannot remove {amount} items of {device.name}")

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        for device, amount in self.items:
            print(f"{device.name} - Quantity: {amount}")

    def checkout(self):
        print("Receipt:")
        self.print_items()
        print(f"Total Price: ${self.total_price}")
        self.items = []
        self.total_price = 0


def main():
    devices = [
        Smartphone("iPhone 13", 999, 10, 36, 6.7, 4000),
        Laptop("MacBook Pro", 1999, 5, 36, 16, 2.7),
        Tablet("iPad Pro", 799, 8, 48, "1280x2560", 150)
    ]

    cart = Cart()

    while True:
        print("\nMenu:")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            for i, device in enumerate(devices):
                print(f"{i+1}. {device}")
            device_choice = int(input("Select a device to add to cart: ")) - 1
            amount = int(input("Enter quantity: "))
            cart.add_device(devices[device_choice], amount)

        elif choice == "2":
            print("\nYour Cart:")
            cart.print_items()
            print(f"Total Price: ${cart.get_total_price()}")
            checkout_choice = input("Proceed to checkout? (y/n): ")
            if checkout_choice.lower() == "y":
                cart.checkout()

        elif choice == "3":
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
