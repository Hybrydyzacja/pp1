class Phone():
    def __init__(self, brand, color, size):
        self.brand = brand
        self.color = color
        self.size = size
        self.is_on = False
        self.is_calling = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def call(self):
        if self.is_on:
            self.is_calling = True
        else:
            print ("First, turn on the phone")

    def end_call(self):
        self.is_calling = False

    def __str__(self):
        if self.is_on and self.is_calling:
            return "Brand: " + self.brand + ", color: " + self.color + ", size: " + self.size + "inch" + "\n" + "Phone is on, you are calling somebody"
        elif self.is_on:
             return "Brand: " + self.brand + ", color: " + self.color + ", size: " + self.size + "inch" + "\n" + "Phone is on"
        else:
            return "Brand: " + self.brand + ", color: " + self.color + ", size: " + self.size + "inch" + "\n" + "Phone is off"


my_phone = Phone("Samsung", "black", "12")
print(my_phone)
my_phone.turn_on()
my_phone.call()
print(my_phone)
my_phone.end_call()
print(my_phone)
