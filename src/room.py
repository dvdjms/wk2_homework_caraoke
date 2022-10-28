class Room():

    def __init__(self, name, tab, cash):
        self.name = name
        self.tab = tab
        self.cash = cash
        self.capacity = 5
        self.entry_fee = 25.00
        self.guests = ["guest1", "guest2"]
        self.songs = []
        self.play_list = ["Bat Out of Hell", "Born to Run", "Over the Rainbow", "Jump", "Bat Out of Hell"]

    def count_guests(self):
        return len(self.guests)

    def add_guest_to_room(self, guest):
        self.guests.append(guest)

    def remove_guest_from_room(self, guest):
        self.guests.remove(guest)

    def count_songs(self):
        return len(self.songs)

    def add_song_to_room(self, song):
        self.songs.append(song)
    
    def enough_capacity_in_room(self, guests):
        if guests >= self.capacity:
            return "Not enough space"
        return "Enough space"

    def can_guest_afford_entry(self, guest):
        if guest > self.entry_fee:
            return "Guest can afford"
        return "Guest can not afford"

    def add_money_to_cash(self, amount):
        self.cash += amount
     
    def guest_pays_entry(self, guest):
        guest.wallet -= self.entry_fee
        self.add_money_to_cash(guest.wallet)
        self.add_guest_to_room(guest)

    def guests_favourite_song(self, guest):
        for song in self.play_list:
            if song == guest.favourite_song:
                return "Whoo!"
        return "Boo!"



 

   



      