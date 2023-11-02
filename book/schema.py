import graphene
from graphene import ObjectType, InputObjectType
from graphene_django import DjangoObjectType
from .models import Book, Author

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'brief', 'published_year']

    author = graphene.Field(AuthorType)

    def resolve_author(self, info):
        return self.author



class CreateBookInput(InputObjectType):
    title = graphene.String()
    author = graphene.String()
    brief = graphene.String()
    published_year = graphene.String()

class CreateBook(graphene.Mutation):
    class Arguments:
        input_data = CreateBookInput(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, input_data):
        book = Book(
            title=input_data.title,
            author=input_data.author_id,
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
    create_book = CreateBook.Field()

book_schema = graphene.Schema(query=Query, mutation=Mutation)

