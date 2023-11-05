import graphene
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from .models import Book, Author
from graphene_django.filter import DjangoFilterConnectionField

# Define the AuthorType and BookType with their fields and connections
class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'brief', 'published_year']
        filter_fields = {
            'title': ['exact', 'icontains'],
            'id': ['exact']
        }
        interfaces = (relay.Node, )

    author = graphene.Field(AuthorType)

    def resolve_author(self, info):
        return self.author

# Define the mutation for creating a book
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author_name = graphene.String(required=True)
        brief = graphene.String()
        published_year = graphene.String()

    book = graphene.Field(BookType)

    def mutate(self, info, title, author_name, brief, published_year):
        author, created = Author.objects.get_or_create(name=author_name)
        book = Book(
            title=title,
            author=author,
            brief=brief,
            published_year=published_year
        )
        book.save()
        return CreateBook(book=book)

# Define a query for retrieving all books
class Query(ObjectType):
    all_books = DjangoFilterConnectionField(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.filter(**kwargs)

# Define the mutation for creating a book
class Mutation(ObjectType):
    create_book = CreateBook.Field()

# Create the GraphQL schema with the query and mutation
book_schema = graphene.Schema(query=Query, mutation=Mutation)
