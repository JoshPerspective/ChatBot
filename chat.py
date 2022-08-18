class Chat:
    def __init__(self, bot):
        print("Hello, Welcome to TOK Concepts\n"
              "How can we be of service to you?")
        self._bot = bot

    def bot(self):
        return self._bot


class CustomerRequest:
    def __init__(self, Tour_Packages, Event_Management, Artist_Bookings):
        self._Tour_Packages = Tour_Packages
        self._Event_Management = Event_Management
        self._Artist_Bookings = Artist_Bookings

    def tour_packages(self):
        return self._Tour_Packages

    def event_management(self):
        return self._Event_Management

    def artist_bookings(self):
        return self._Artist_Bookings


class CustomerServices(CustomerRequest):
    def start(self):
        enter = input("What would you like to make enquiries about?\n "
                      "(1) Tour Packages\n (2) Event Management\n (3) Artist Bookings\n")
        if enter == '1':
            print(self.tour_packages())
        elif enter == '2':
            print(self.event_management())
        elif enter == '3':
            print(self.artist_bookings())
        else:
            return self.start()


if __name__ == '__main__':
    b = Chat('bot')
    b.bot()
    c = CustomerServices('Tour Packages!', 'Event Management!', 'Artist Bookings!')
    c.start()

# c = Chat()
# c.bot()
# c._bot
