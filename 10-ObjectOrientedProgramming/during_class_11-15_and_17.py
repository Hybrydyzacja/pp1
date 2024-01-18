class TV():
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.is_on = False
        self.channel_no = 1
        self.avaiable_channels = []
        self.volume = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no

    def set_channels(self, channel_list):
        self.avaiable_channels = channel_list

    def show_channels(self):
        print(f"Avaiable channels: {my_TV.avaiable_channels}")

    def increase_vol(self):
        if self.volume >= 0 and self.volume < 10:
            self.volume += 1
        else:
            self.volume = 10

    def decrease_vol(self):
        if self.volume > 0 and self.volume <= 10:
            self.volume -= 1
        else:
            self.volume = 0

    def show_status(self):
        if self.is_on:
            print(f"TV is on")
            if int(my_TV.channel_no) <= len(my_TV.avaiable_channels):
                print(
                    f"Channel {my_TV.channel_no} ({my_TV.avaiable_channels[int(my_TV.channel_no)-1]})")
            else:
                print(f"Channel {my_TV.channel_no}")
        else:
            print("TV is off")
        print(f"Volume: {my_TV.volume}")


my_TV = TV("Samsung", "2022")

my_TV.show_status()
my_TV.turn_on()
my_TV.show_status()
my_TV.show_channels()
my_TV.set_channels(["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"])
my_TV.show_channels()
my_TV.set_channel(5)
my_TV.increase_vol()
my_TV.show_status()
my_TV.set_channel(7)
my_TV.show_status()
my_TV.decrease_vol()
my_TV.turn_off()
my_TV.show_status()
