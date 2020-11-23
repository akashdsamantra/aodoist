import graphene
from graphene_django import DjangoObjectType

from .models import User

class UserType(DjangoObjectType):
  class Meta:
    model = User
    field = ('id', 'name', 'username', 'email', 'is_mobile_verified', 'is_email_verified')

class Query(graphene.ObjectType):
  users = graphene.List(UserType)

  def resolve_users(root, info):
    return User.objects.all()