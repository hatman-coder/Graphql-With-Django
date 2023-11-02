from django.urls import path
from graphene_django.views import GraphQLView
from .schema import book_schema
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('book/graphql', csrf_exempt(GraphQLView.as_view(
        graphiql=True, schema=book_schema))),
]
