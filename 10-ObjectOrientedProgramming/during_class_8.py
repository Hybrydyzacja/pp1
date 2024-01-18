class Phone():
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def call_number(self, number):
        self.number = number
        print(f"Calling {my_phone.number} number")

    def phone_info(self):
        print(
            f"This is {my_phone.brand} phone, it's {my_phone.color} and {my_phone.size} inch big.")

    def status(self):
        if my_phone.is_on:
            print("Phone is on")
        else:
            print("Phone is off")


my_phone = Phone("Poco", "black", "12")


my_phone.phone_info()
my_phone.status()
my_phone.turn_on()
my_phone.status()
my_phone.call_number(1236547)
