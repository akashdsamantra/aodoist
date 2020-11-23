import graphene

import myauth.schema

class Query(myauth.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
