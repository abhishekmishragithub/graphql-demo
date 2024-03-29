"""
GraphQL schema 
"""
import graphene
import extraction
import requests

def extractd(url):
    print(type(url))
    html = requests.get(url['url']).text
    extracted = extraction.Extractor().extract(html, source_url=url['url'])
    return extracted

class Website(graphene.ObjectType):
    url = graphene.String(required=True, description="simple website url")
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()
    feed = graphene.String()
    
    
class Query(graphene.ObjectType):
    website = graphene.Field(Website, url=graphene.String())
    

    def resolve_website(self, url, context, info):
        extracted = extractd(url)
        print(extracted)
        return Website(url=url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image,
                       feed=extracted.feed
        )

schema = graphene.Schema(query=Query)
# print(schema)