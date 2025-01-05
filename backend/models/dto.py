'''
Модель структури даних "студент" - для представлення:
DTO: Data Transfer Object — один із шаблонів проєктування, який використовують для передачі даних між підсистемами програми.
'''

from dataclasses import dataclass


@dataclass                                                      # декоратор для додавання даних
class BooksDTO:
    """
    book information
    """
    books_name: str
    author: str
    year_creat: int
    books_id: int = -1
    invited: bool = False
    full_name = ""
    
    def __post_init__(self):                                    # дандер метод __post_init__ заповнює поля після створення екземпляру класа
        self.invited = (1000 <= int(self.year_creat) <= 2030)
        self.full_name = f"{self.books_name} {self.author}"
