import typing
import strawberry
from strawberry.asgi import GraphQL

@strawberry.type
class Book:
    title: str
    author: str


def get_books():
    return [
        Book(
            title="The Great Gatsby",
            author="F. Scott Fitzgerald",
        ),
    ]



@strawberry.type
class Query:
    # Использование позволяет нам указать резолвер для конкретного поля. strawberry.field
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    # Заметка
    # Нам не нужно было указывать какой-либо резолвер для полей Книги, это связано с тем,
    #  что Strawberry добавляет значение по умолчанию для каждого поля, возвращая значение этого поля.

# Чтобы создать схему, добавьте следующий код:
schema = strawberry.Schema(query=Query)

# Затем выполните следующую команду
#strawberry server schema

# Создаём ASGI приложение
app = GraphQL(schema)

# Запустим сервер
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)



