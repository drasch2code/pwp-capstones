
###  USER

class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = {}

  def get_email(self):
    return self.email

  def change_email(self, update_email):
    self.email = update_email
    return "Your e-mail address has been changed to: {mail}".format(mail=self.mail)

  # read book and rating 
  def read_book(self,book,rating = None):
    self.books[book.title] = rating
    if rating:
      book.add_rating(rating)


  # getting the avg rating
  def get_avg_rating(self):
      ratings_total = 0
      for book in self.books:
          ratings_total += self.books[book]     
          #How do I solve this, it should call the value of the book key & that's a number?
      if len(self.books) > 0:
        average = ratings_total / len(self.books)
      else:
        average = None
      return average



  def __repr__(self):
    return "User {user}, email: {email}, books read: {count}".format( 
      user = self.name, email = self.email, count = str(len(self.books))
      )

  def __eq__(self, other_user):
    return self.name == other_user.name and self.email == other_user.email

### CREATING A BOOK

class Book:
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []

  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def set_isbn(self, new_isbn):
    self.isbn = new_isbn
    return "This books ({book}) ISBN has been changed to: {isbn}".format(
      book= self.title, isbn=self.isbn
      )

  def add_rating(self, rating):
    if rating <= 4 and rating >= 0:
      self.ratings.append(rating)
    else:
      print("Invalid rating!")

  # getting the avg rating
  def get_avg_rating(self):
    sum_rating = 0
    for rating in self.ratings:
      sum_rating += rating
    return sum_rating / len(self.ratings) #IS THIS WORKING? TEST IT!

  #making book hashable:
  def __hash__(self):
    return hash((self.title, self.isbn)) 
    # look this one up:  
    # https://docs.python.org/3/library/functions.html#hash

  def __eq__(self, other_book):
    return self.title == other_book.title and self.isbn == other_book.isbn

### CREATING A FICTION child of BOOK

class Fiction(Book):
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author

  def __repr__(self):
    return "{title} by {author}".format(title=self.title, author= self.author)

### CREATING A FICTION child of BOOK

class Non_Fiction(Book):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.subject

  def __repr__(self):
    return "{title}, a {level} manual on {subject}".format(
      title=self.title, level=self.level,  subject= self.subject
      )

### TOME RATER

class TomeRater(object):
  def __init__(self):
    self.users = {}
    self.books = {}

  def create_book(self, title, isbn):
    return Book(title,isbn)

  def create_novel(self, title, author, isbn):
    return Fiction(title, author, isbn)

  def create_non_fiction(self, title, subject, level, isbn):
    return Non_Fiction(title, subject, level, isbn)

  def add_book_to_user(self, book, email, rating = None):
    if email in self.users:
      new_user = self.users.get(email, "No user with email: {email}!".format(email = email))
      new_user.read_book(book, rating)
      if book in self.books:
        self.books[book] += 1
        book.add_rating(rating)
      else:
        self.books[book] = 1
    else:
      print("No user with email: {email}!".format(email = email))

  def add_user(self, name, email, user_books = None):
    self.users[email] = User(name, email)
    if user_books is not None:
      for book in user_books:
        self.add_book_to_user(book, email)
    return User(name, email)

  ### Some Analysis Methods for TomeRater

  def print_catalog(self):
    print("The catalog are the following books: ")
    for book in self.books:
      print(book)

  def print_users(self):
    print("The user list is: ")
    for user in self.users:
      print(user)

  def most_read_book(self):
    largest_value = 0
    largest_book = float('-inf')
    for key,value in self.books.items():
      if value > largest_value:
        largest_value = value
        largest_book = key
    return print("The most read book is: {largest_book}, it was read by {num} people.".format(
    largest_book=largest_book, num=largest_value)
    )

  def highest_rated_book(self):
    highest_rating = 0
    highest_rated_book = float('-inf')
    for book in self.books:
      if book.get_avg_rating() > highest_rating:
        highest_rating = book.get_avg_rating()
        highest_rated_book = book
    return print("The highest rated book is {highest_rated_book}" 
      +" with an avarage of {highest_rating}".format(
        highest_rated_book=highest_rated_book, highest_rating=highest_rating)
      )

  def most_positive_user(self):
    highest_rating_user = 0
    highest_rated_username = float('-inf')
    for user in self.users.values():
      avg_rating = user.get_avg_rating()
      if avg_rating > highest_rating_user:
        highest_rating_user = avg_rating
        highest_rated_username = user
    return print("The highest rated user is {highest_rated_username}" 
      +" with an avarage of {highest_rating}".format(
        highest_rated_username=highest_rated_username, highest_rating=highest_rating)
      )

  def __repr__(self):
    return """Functions of Tome Rater are: 
print_catalog, \nprint_users, \nmost_read_book, 
highest_rated_book \n """

  def __eq__(self, other_tome_rater):
    return self.users == other_tome_rater.users and self.books == other_tome_rater.books


