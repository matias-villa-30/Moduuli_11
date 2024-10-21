class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        return "Book: {}\tAuthor: {}\t\tPage count: {}".format(self.name, self.author, self.page_count)

class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_info(self):
        return "Magazine: {} \tChief Editor: {}".format(self.name, self.chief_editor)

revista = Magazine("Donald Duck", "Aki Hyyppä")
print(revista.print_info())

libro = Book("Compartment No.6", "Rosa Liksom", 192)
print(libro.print_info())