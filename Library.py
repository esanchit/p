#Jade Nguyen
#10/7/20
#Keeps track of library items through multiple classes

class LibraryItem(object):
    """Creates a class library and takes in library_item_id, and title. """

    def __init__(self, library_item_id, title):
        """initializes library_item_id, title, location, requested by, date checked out, and checked out by """
        self._library_item_id = library_item_id
        self._title = title
        self._location = "ON_SHELF"
        self._requested_by = None
        self._date_checked_out = None
        self._checked_out_by = None

    # getters
    def get_requested_by(self):
        """returns requested_by """
        return self._requested_by

    def get_location(self):
        """returns location"""
        return self._location

    def get_title(self):
        """returns title"""
        return self._title

    def get_library_item_id(self):
        """returns library item id"""
        return self._library_item_id

    def get_checked_out_by(self):
        """returns checked out by"""
        return self._checked_out_by

    def get_date_checked_out(self):
        """sets date checked out"""
        return self._date_checked_out

   # setters
    def set_library_item_id(self, library_item_id):
        """sets library_item_id"""
        self._library_item_id = library_item_id

    def set_title(self, title):
        """sets title"""
        self._title = title

    def set_location(self, location):
        """Sets location"""
        self._location = location

    def set_requested_by(self, requested_by):
        """sets requested by"""
        self._requested_by = requested_by

    def set_date_checked_out(self, date_checked_out):
        """sets date checked out"""
        self._date_checked_out = date_checked_out

    def set_checked_out_by(self, checked_out_by):
        """sets checked out by"""
        self._checked_out_by = checked_out_by

class Book(LibraryItem):
    """creates class book with inheritance from libraryitem """
    def __init__(self, library_item_id, title, author):
        """inheritance and initializes author"""
        super().__init__(library_item_id, title)
        self._author = author

    def get_author(self):
        """returns author"""
        return self._author

    def get_check_out_length(self):
        """returns book check out length"""
        return 21

class Album(LibraryItem):
    """creates class album with inheritance from libraryitem"""
    def __init__(self, library_item_id, title, artist):
        """inheritance and initializes artist"""
        super().__init__(library_item_id, title)
        self._artist = artist

    def get_artist(self):
        """returns artist"""
        return self._artist

    def get_check_out_length(self):
        """returns album check out length"""
        return 14

class Movie(LibraryItem):
    """creates class Movie with inheritance from libraryitem"""
    def __init__(self, library_item_id, title, director):
        """inheritance and initializes director"""
        super().__init__(library_item_id, title)
        self._director = director

    def get_director(self):
        """returns director"""
        return self._director

    def get_check_out_length(self):
        """returns movie check out length"""
        return 7

class Patron:
    """creates class with patron id and name"""
    def __init__(self, patron_id, name):
        """initializes patron_id, name, checked_out_items, and fine amount """
        self._patron_id = patron_id
        self._name = name
        self._checked_out_items = []
        self._fine_amount = 0

    def get_patron_id(self):
        """returns patron id"""
        return self._patron_id

    def get_name(self):
        """returns name"""
        return self._name

    def get_checked_out_items(self):
        """returns checked_out_items"""
        return self._checked_out_items

    def get_fine_amount(self):
        """returns fine amount"""
        return self._fine_amount

    def add_library_item(self, item):
        """appends an item to checked out items"""
        self._checked_out_items.append(item)

    def remove_library_item(self, item):
        """removes an item to checked out items"""
        self._checked_out_items.remove(item)

    def amend_fine(self, fine):
        """amends the accrued fine amounts"""
        self._fine_amount += fine

class Library:
    """creates class library"""
    def __init__(self):
        """initializes current date, holdings, members"""
        self._current_date = 0
        self._holdings = []
        self._members = []

    def get_holdings(self):
        """returns holdings"""
        return self._holdings

    def get_members(self):
        """returns members"""
        return self._members

    def get_current_date(self):
        """returns current date"""
        return self._current_date

    def add_library_item(self, LibraryItem):
        """appends library item to holdings"""
        self._holdings.append(LibraryItem)

    def add_patron(self, Patron):
        """appends patron to members"""
        self._members.append(Patron)

    def get_library_item_from_id(self, id_value):
        """returns item from id value"""
        for item in self._holdings:
            if item.get_library_item_id() == id_value:
                return item
        return None

    def get_patron_from_id(self, Patron_id):
        """returns member from patron id"""
        for member in self._members:
            if member.get_patron_id() == Patron_id:
                return member
        return None

    def check_out_library_item(self, patron_id, library_item_id):
        """check out sequence"""
        if self.get_patron_from_id(patron_id) is None:
            return "patron not found"

        if self.get_library_item_from_id(library_item_id) is None:
            return "item not found"

        lib_item = self.get_library_item_from_id(library_item_id)

        if lib_item.get_location() == "CHECKED_OUT":
            return "item already checked out"

        if lib_item.get_location() == "ON_HOLD_SHELF" and lib_item.get_requested_by().get_patron_id() != patron_id:
            return "item on hold by other patron"

        pat = self.get_patron_from_id(patron_id)

        lib_item.set_checked_out_by(pat)
        lib_item.set_date_checked_out(self._current_date)
        lib_item.set_location("CHECKED_OUT")

        if lib_item.get_requested_by() == patron_id:
            lib_item.set_requested_by(None)

        pat.add_library_item(lib_item)

        return "check out successful"

    def return_library_item(self, library_item_id):
        """library item return process"""
        if self.get_library_item_from_id(library_item_id) is None:
            return "item not found"

        lib_item = self.get_library_item_from_id(library_item_id)

        if lib_item.get_location() == "ON_HOLD":
            return "item already in library"
        elif lib_item.get_location() == "ON_HOLD_SHELF":
            isInLibrary=True;
            for member in self._members:
                if lib_item in member.get_checked_out_items():
                    isInLibrary=False
                    break
            if  isInLibrary:
                return "item already in library"

        pat = lib_item.get_checked_out_by()
        pat.remove_library_item(lib_item)

        if lib_item.get_requested_by() == None:
            lib_item.set_location("ON_HOLD")
        elif lib_item.get_requested_by().get_patron_id() == pat.get_patron_id():
            lib_item.set_location("ON_HOLD")
        else:
            lib_item.set_location("ON_HOLD_SHELF")

        lib_item.set_checked_out_by(None)

        return "return successful"

    def request_library_item(self, patron_id, library_item_id):
        """request to hold item process"""
        lib_item = self.get_library_item_from_id(library_item_id)
        pat = self.get_patron_from_id(patron_id)

        if pat is None:
            return "patron not found"

        if lib_item is None:
            return "item not found"

        if lib_item.get_location() == 'ON_HOLD_SHELF':
            return "item already on hold"

        lib_item.set_requested_by(pat)
        lib_item.set_location('ON_HOLD_SHELF')

        return "request successful"

    def pay_fine(self, patron_id, amount):
        """amend and pay fine process"""
        pat = self.get_patron_from_id(patron_id)
        if pat is None:
            return "patron not found"
        pat.amend_fine(-amount)
        return "payment successful"

    def increment_current_date(self):
        """date increment process and fine calculations"""
        self._current_date += 1
        for member in self._members:
            for item in member.get_checked_out_items():
                if (self._current_date - item.get_date_checked_out()) > item.get_check_out_length():
                    member.amend_fine(0.10)

# Main code for Test
#b1 = Book("345", "Phantom Tollbooth", "Juster")
#a1 = Album("456", "...And His Orchestra", "The Fastbacks")
#m1 = Movie("567", "Laputa", "Miyazaki")
#print(b1.get_author())
#print(a1.get_artist())
#print(m1.get_director())

#p1 = Patron("abc", "Felicity")
#p2 = Patron("bcd", "Waldo")

#print(a1.get_location())

#lib = Library()
#lib.add_library_item(b1)
#lib.add_library_item(a1)
#lib.add_library_item(m1)

#lib.add_patron(p1)
#lib.add_patron(p2)

#print()
#print(a1.get_location())
#print(lib.check_out_library_item("abc", "456"))
#print( a1.get_location())
#print(lib.request_library_item("bcd", "456"))
#print( a1.get_location())

#print()
#print(lib.check_out_library_item("abc", "456"))
#print( a1.get_location())
#print(lib.request_library_item("abc", "456"))
#print( a1.get_location())

#print()
#print(lib.return_library_item("456"))
#print( a1.get_location())

#print()
#print(lib.request_library_item("bcd", "456"))
#print(a1.get_location())

#print()
#print(lib.return_library_item("456"))

#print()
#print(lib.check_out_library_item("abc", "456"))
#print( a1.get_location())

#print()
#print(lib.check_out_library_item("bcd", "456"))
#print( a1.get_location())

#print()
#print(lib.check_out_library_item("abc", "456"))
#print( a1.get_location())

#print()
#print  (p1.get_fine_amount())
#for i in range(57):
#    lib.increment_current_date()   # 57 days pass

#p2_fine = p2.get_fine_amount()
#print(p2_fine)
#print(lib.pay_fine("bcd", p2_fine))
#p1.get_fine_amount()
#print( p2.get_fine_amount())
#print()
#print(lib.return_library_item("456"))
