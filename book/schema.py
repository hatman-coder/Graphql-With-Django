import graphene
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType
from .models import Book, Author


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ['id', 'name']


class AuthorInput(InputObjectType):
    name = graphene.String()


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'brief', 'published_year']

    author = graphene.Field(AuthorType)

    def resolve_author(self, info):
        return self.author


class CreateBookInput(InputObjectType):
    title = graphene.String()
    author = AuthorInput()
    brief = graphene.String()
    published_year = graphene.String()


class CreateBook(graphene.Mutation):
    class Arguments:
        input_data = CreateBookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, input_data):
        author_data = input_data.get('author')

        # Create a new author
        author = Author.objects.create(
            name=author_data.get('name')
        )

        book = Book(
            title=input_data.title,
            author=author,
            brief=input_data.brief,
            published_year=input_data.published_year
        )
        book.save()
        return CreateBook(book=book)

# GET method


class Query(ObjectType):
    all_books = graphene.List(BookType)

    def resolve_all_books(self, info):
        return Book.objects.all()

# POST method


class Mutation(graphene.ObjectType):

    # Book Mutation Example

    #     mutation {
    # createBook(
    #     inputData: {title: "Hello World", author: {name: "Akondo"}, brief: "Description of the new book", publishedYear: "2023"}
    # ) {
    #     book {
    #     title: title
    #     author: author {
    #         name
    #     }
    #     brief: brief
    #     publishedYear: publishedYear
    #     }
    # }
    # }

    create_book = CreateBook.Field()


book_schema = graphene.Schema(query=Query, mutation=Mutation)
