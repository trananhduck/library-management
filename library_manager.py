class Catalog:
    """
    Đại diện cho danh mục các mục trong thư viện.
    Attributes:
        items (list): Danh sách các mục trong thư viện.
    """

    def __init__(self):
        self.items = []
    # Phương thức tìm kiếm

    def add_item(self, item):
        """
        Thêm một mục trong danh mục bằng tên item.
        Args:
            item (str): Tên item cần thêm.
        """
        return self.items.append(item)

    def search_item(self, query):
        """
        Tìm kiếm một mục trong danh mục bằng từ khóa.
        Args:
            query (str): Từ khóa tìm kiếm.
        Returns:
            str: Số UPC của mục tìm thấy, nếu không tìm thấy trả về None.
        """
        for item in self.items:
            if query.lower() in item.title.lower():
                return item.upc
        return None
    # Phương thức xóa

    def delete_item(self, upc):
        """
        Xóa một mục khỏi danh mục dựa trên số UPC.
        Args:
            upc (str): Số UPC của mục cần xóa.
        Returns:
            None
        """
        item_deleted = None
        for item in self.items:
            if item.upc == upc:
                item_deleted = item
                self.items.remove(item)
                break

        if item_deleted:
            print(
                f"Item with UPC  {upc} '{item_deleted.title}' deleted.")
        else:
            print(f"No item found with UPC  {upc}.")


class Contributor:
    def __init__(self, name):
        """
        Đại diện cho một người đóng góp vào một mục trong thư viện.
        Attributes:
            name (str): Tên của người đóng góp.
        """
        self.name = name


class ContributorWithType:
    """
    Đại diện cho một người đóng góp vào một mục cụ thể trong thư viện.
    Attributes:
        name (str): Tên của người đóng góp.
        Contributor_type: Loại của người đóng góp (ví dụ: tác giả, diễn viên, đạo diễn).
    """

    def __init__(self, name, type):
        self.contributor = Contributor(name)
        self._type = type


class LibraryItem:
    """
    Đại diện cho một mục trong thư viện.
    Attributes:
        title (str): Tiêu đề của mục.
        upc (str): Số UPC của mục.
        item_type (str): Loại của mục (ví dụ: sách, tạp chí, đĩa CD, đĩa DVD).
        upc: Mã UPC của mục (nếu có).
        subject: Chủ đề của mục (nếu có).
        contributors (list): Danh sách các người đóng góp vào mục.
    """

    def __init__(self, title, upc, subject, item_type):
        # Khởi tạo một mục thư viện với tiêu đề và số UPC cho trước.
        self.title = title
        self.upc = upc
        self.subject = subject
        self.item_type = item_type
        self.contributors = []

    def locate(self):
        """
        Trả về số UPC của mục.
        Returns:
            str: Số UPC của mục.
        """
        return self.upc


class Book(LibraryItem):
    """
    Đại diện cho một cuốn sách trong thư viện.
    Attributes:
        author (str): Tác giả của sách.
        isbn (str): Mã ISBN của sách.
        upc (str): Mã UPC của sách.
    """

    def __init__(self, title, upc, subject, author, isbn, dds_number):
        # Khởi tạo một cuốn sách với tiêu đề, số UPC, tác giả và ISBN cho trước.
        super().__init__(title, upc, subject, "Book")
        self.author = author
        self.isbn = isbn
        self.dds_number = dds_number


class Magazine(LibraryItem):
    """
    Đại diện cho một tạp chí trong thư viện.
    Attributes:
        volume (str): Số tập của tạp chí.
        issue (str): Số phát hành của tạp chí.
    """

    def __init__(self, title, upc, subject, volume, issue):
        # Khởi tạo một tạp chí với tiêu đề, số UPC, số tập và số phát hành cho trước.
        super().__init__(title, upc, subject, "Magazine")
        self.volume = volume
        self.issue = issue


class CD(LibraryItem):
    """
    Đại diện cho một đĩa CD trong thư viện.
    Attributes:
        artists (str): Danh sách các nghệ sĩ trên đĩa CD.
    """

    def __init__(self, title, upc, subject, artists):
        # Khởi tạo một đĩa CD với tiêu đề, số UPC và danh sách nghệ sĩ cho trước.
        super().__init__(title, upc, subject, "CD")
        self.artists = artists


class DVD(LibraryItem):
    """
    Đại diện cho một đĩa DVD trong thư viện.
    Attributes:
        genre (str): Thể loại của đĩa DVD.
        actors (str): Danh sách các diễn viên trên đĩa DVD.
        directors (str): Danh sách các đạo diễn của đĩa DVD.
    """

    def __init__(self, title, upc, subject, genre, actors, directors):
        # Khởi tạo một đĩa DVD với tiêu đề, số UPC và thể loại cho trước.
        super().__init__(title, upc, subject, "DVD")
        self.genre = genre
        self.actors = actors
        self.directors = directors


class Menu:
    """
    Đại diện cho menu tương tác với người dùng.
    Attributes:
        catalog (Catalog): Đối tượng Catalog chứa danh sách các mục trong thư viện.
    """

    def __init__(self, catalog):
        self.items = catalog.items

    def display_menu(self):
        """
        Hiển thị menu và yêu cầu người dùng nhập lựa chọn.
        Returns:
            str: Lựa chọn của người dùng.
        """
        print("1. Add item")
        print("2. Delete item")
        print("3. Search item")
        print("4. Show all")
        print("5. Exit")
        choice = input("Enter your choice: ")
        return choice

    # Hàm thêm item
    def Add_Item(self):
        while True:
            print("Enter item type (book, magazine, cd, dvd): ")
            print("1. Book")
            print("2. Magazine")
            print("3. CD")
            print("4. DVD")
            print("5. Exit")
            choice1 = input("Enter your choice: ")

            if choice1 == '1':
                title = input("Enter item title: ")
                upc = input("Enter UPC : ")
                subject = input("Enter subject: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                dds_number = input("Enter DDS_number: ")
                catalog.add_item(
                    Book(title, upc, subject, author, isbn, dds_number))
                print(f"Item '{title}' (UPC {upc}) added.")

            elif choice1 == '2':
                title = input("Enter item title: ")
                upc = input("Enter UPC : ")
                subject = input("Enter subject: ")
                volume = input("Enter volume: ")
                issue = input("Enter issue: ")
                catalog.add_item(
                    Magazine(title, upc, subject, volume, issue))
                print(f"Item '{title}' (UPC {upc}) added.")
            elif choice1 == '3':
                title = input("Enter item title: ")
                upc = input("Enter UPC : ")
                subject = input("Enter subject: ")
                artist = input("Enter artist: ")
                catalog.add_item(CD(title, upc, subject, artist))
                print(f"Item '{title}' (UPC {upc}) added.")
            elif choice1 == '4':
                title = input("Enter item title: ")
                upc = input("Enter UPC : ")
                subject = input("Enter subject: ")
                genre = input("Enter genre: ")
                actors = input("Enter actors: ")
                directors = input("Enter directors: ")
                catalog.add_item(
                    DVD(title, upc, subject, genre, actors, directors))
                print(f"Item '{title}' (UPC {upc}) added.")
            elif choice1 == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    # Hàm xóa item

    def Delete_Item(self):
        while True:
            print("Please choose item (book, magazine, cd, dvd): ")
            print("1. Book")
            print("2. Magazine")
            print("3. CD")
            print("4. DVD")
            print("5. Exit")
            choice2 = input("Enter your choice: ")
            if choice2 == '1' or choice2 == '2' or choice2 == '3' or choice2 == '4':
                upc_to_delete = input("Enter UPC  to delete: ")
                catalog.delete_item(upc_to_delete)
            elif choice2 == '5':
                break
            else:
                print("Invalid choice. Please try again.")

    # Hàm tìm kiến item

    def Search_Item(self):
        while True:
            print("Please choose item (book, magazine, cd, dvd): ")
            print("1. Book")
            print("2. Magazine")
            print("3. CD")
            print("4. DVD")
            print("5. Exit")
            choice3 = input("Enter your choice: ")
            if choice3 == '1':
                keyword = input("Enter name of the book: ")
                upc = catalog.search_item(keyword)
            elif choice3 == '2':
                keyword = input("Enter name of the magazine: ")
                upc = catalog.search_item(keyword)
            elif choice3 == '3':
                keyword = input("Enter name of the CD: ")
                upc = catalog.search_item(keyword)
            elif choice3 == '4':
                keyword = input("Enter name of the DVD: ")
                upc = catalog.search_item(keyword)
            elif choice3 == '5':
                break
            else:
                print("Invalid choice. Please try again.")
                break
            if upc is not None:
                # tìm item theo loại danh mục(book, magazine, cd, dvd)
                item_type = next(
                    item.item_type for item in catalog.items if item.upc == upc)
                # tìm kiếm item theo keyword trong tên
                # (có thể tìm và trả ra tên đầy đủ khi mới nhập vào một số chữ cái trong tên/ một số từ)
                obj = next(
                    item for item in catalog.items if item.upc == upc)
                if item_type == 'Book':
                    author = next(
                        item.author for item in catalog.items if item.upc == upc)
                    print(
                        f"{item_type} '{obj.title}', subject {obj.subject} with UPC {upc} of {author}, DDS_number: {obj.dds_number} ")
                elif item_type == 'Magazine':
                    volume = next(
                        item.volume for item in catalog.items if item.upc == upc)
                    issue = next(
                        item.issue for item in catalog.items if item.upc == upc)
                    print(
                        f"{item_type} '{obj.title}', subject {obj.subject} with UPC {upc} {volume}, issue {issue}")
                elif item_type == 'CD':
                    artist = next(
                        item.artists for item in catalog.items if item.upc == upc)
                    print(
                        f"{item_type} '{obj.title}', subject {obj.subject} with UPC {upc} of {artist} ")
                elif item_type == 'DVD':
                    genre = next(
                        item.genre for item in catalog.items if item.upc == upc)
                    actors = next(
                        item.actors for item in catalog.items if item.upc == upc)
                    director = next(
                        item.directors for item in catalog.items if item.upc == upc)
                    print(
                        f"{item_type} '{obj.title}', subject {obj.subject} with UPC {upc}, genre {genre}, actors: {actors}, đạo diễn {director}")

            else:
                # Nếu không tìm thấy tên item thì nhập lại hoặc thoát vòng lặp
                # In thông báo lỗi và yêu cầu nhập lại với các option
                print(
                    f"'{keyword}' was not found in the directory, please re-enter")

    def Show_All(self):
        items_by_type = {'Book': [], 'Magazine': [], 'CD': [], 'DVD': []}

        # Phân loại các mục theo loại và lưu vào từ điển items_by_type
        for item in self.items:
            if isinstance(item, Book):
                items_by_type['Book'].append(item)
            elif isinstance(item, Magazine):
                items_by_type['Magazine'].append(item)
            elif isinstance(item, CD):
                items_by_type['CD'].append(item)
            elif isinstance(item, DVD):
                items_by_type['DVD'].append(item)

        # Hiển thị các mục phân loại theo thứ tự từ điển và theo định dạng yêu cầu
        for item_type in sorted(items_by_type.keys()):
            print(f"{item_type}s:")
            for item in items_by_type[item_type]:
                if item_type == 'Book':
                    print(
                        f"Title: {item.title}, UPC : {item.upc}, Subject: {item.subject}, Author: {item.author}, ISBN: {item.isbn}, DDS_number: {item.dds_number}")
                elif item_type == 'Magazine':
                    print(
                        f"Title: {item.title}, UPC : {item.upc}, Volume: {item.volume}, Issue: {item.issue}")
                elif item_type == 'CD':
                    print(
                        f"Title: {item.title}, UPC : {item.upc}, Artist: {item.artists}")
                elif item_type == 'DVD':
                    print(
                        f"Title: {item.title}, UPC : {item.upc}, Genre: {item.genre}, Actors: {item.actors}, Directors: {item.directors}")
            print()


if __name__ == "__main__":
    catalog = Catalog()
    my_menu = Menu(catalog)
    # Một số ví dụ với các danh mục trong thư viện
    # Book
    book1 = Book("Angels and Demons", "B316", "Mystery",
                 "Dan Brown", "813.51", "B123")
    book2 = Book("1984", "B405", "Dystopian Fiction",
                 "George Orwell", "823.912", "B456")
    book3 = Book("The Catcher in the Rye", "B234",
                 "Coming-of-Age Fiction", "J. D. Salinger", "813.54", "C424")
    book4 = Book("The Great Gatsby", "B425", "Jazz Age",
                 "F. Scott Fitzgerald", "813.52", "A123")
    book5 = Book("To Kill a Mockingbird", "B253",
                 "Southern Gothic", "Harper Lee", "813.55", "D124")
    # magazine
    magazine1 = Magazine("National Geographic", "M101",
                         "Geography", "Vol. 123", "updating")
    magazine2 = Magazine("Time Magazine", "M102",
                         "News", "Vol. 200", "updating")
    magazine3 = Magazine("Scientific American", "M103",
                         "Science", "Vol. 50", "finished")
    magazine4 = Magazine("People Magazine", "M104",
                         "Fashion", "Vol. 300", "updating")
    magazine5 = Magazine("Sports Illustrated", "M105",
                         "Sport", "Vol. 75", "finished")
    # CD
    cd1 = CD("Greatest Hits", "C201", "Music", "The Beatles")
    cd2 = CD("Thriller", "C202", "Music", "Michael Jackson")
    cd3 = CD("1989", "C203", "Music", "Taylor Swift")
    cd4 = CD("÷", "C204", "Music", "Ed Sheeran")
    cd5 = CD("Lemonade", "C205", "Music", "Beyoncé")
    # DVD
    dvd1 = DVD("Inception", "V301", "AAA", "Science Fiction",
               "Leonardo DiCaprio, Ellen Page", "Christopher Nolan")
    dvd2 = DVD("The Dark Knight", "V302", "AAA", "Action",
               "Christian Bale, Heath Ledger", "Christopher Nolan")
    dvd3 = DVD("Pulp Fiction", "V303", "AAA", "Crime",
               "John Travolta, Uma Thurman", "Quentin Tarantino")
    dvd4 = DVD("The Shawshank Redemption", "V304", "AAA", "Drama",
               "Tim Robbins, Morgan Freeman", "Frank Darabont")
    dvd5 = DVD("Fight Club", "V305", "AAA", "Drama",
               "Brad Pitt, Edward Norton", "David Fincher")
    # thêm các item vào catalog
    catalog.items.extend([book1, book2, book3, book4, book5])
    catalog.items.extend(
        [magazine1, magazine2, magazine3, magazine4, magazine5])
    catalog.items.extend([cd1, cd2, cd3, cd4, cd5])
    catalog.items.extend([dvd1, dvd2, dvd3, dvd4, dvd5])
    # Thực hiện các option cho tới khi người dùng muốn thoát khỏi chương trình
    while True:
        choice = my_menu.display_menu()
    # Các option theo ý muốn
        if choice == "1":
            my_menu.Add_Item()
        elif choice == "2":
            my_menu.Delete_Item()
        elif choice == "3":
            my_menu.Search_Item()
        elif choice == '4':
            my_menu.Show_All()
        elif choice == "5":
            print("Exiting program.")
            print('--------------')
            print("The program has ended!!!")
            break
        else:
            print("Invalid choice. Please try again.")
