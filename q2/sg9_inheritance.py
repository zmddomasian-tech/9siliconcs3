class Publication: 
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author 

    def get_title(self):
        return f"Title: {self.title}"

    def set_title(self, title: str) -> None:
        if not title or not str(title).strip():
            raise ValueError("title must not be empty.")
            self.__title = str(title).strip()

    def get_author(self):
        return f"Author: {self.author}"

    def set_author(self, author: str) -> None:
        if not author or not str(author).strip():
            raise ValueError("Author must not be empty.")
            self.__author = str(author).strip()
    
    def display_info(self)
        print( f"Title: {self.title}")
        print( f"Author: {self.author}")

class Book(Publication):
    def __init__(self, title: str, author: str, number_of_pages: int):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages

    def get_number_of_pages(self):
        return f'Number of pages: {self.number_of_pages}'

    def set_number_of_pages(self, number_of_pages: int):
        if number_of_pages < 0:
            raise ValueError("Pages must not be negative.")
        self.__number_of_pages = float(number_of_pages)

class Magazine(Publication):
    def __init__(self, title: str, author: str, issue_number: int):
        super().__init__(title, author)
        self.__issue_number = issue_number

    def get_issue_number(self):
        return f'Issue Number: {self.__issue_number}'

    def set_issue_number(self, issue_number: int):
        if issue_number < 0:
            raise ValueError("Issue number must not be negative")
        self.__issue_number = float(issue_number)
    
