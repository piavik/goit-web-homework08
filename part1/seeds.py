from models import Author, Quotes #, Tag
# from datetime import datetime
import json
import connect

with open("authors.json", "r") as a:
    authors = json.load(a)
for author in authors:
    # born_date to datetime conversion needed ?
    # text_date = author['born_date']
    # author['born_date'] = str(datetime.strptime(text_date, "%B %d, %Y").date())
    Author.from_json(json.dumps(author)).save()

with open("quotes.json", "r") as q:
    quotes = json.load(q)
for quote in quotes:
    # assuming author records are unique
    authors = Author.objects(fullname=quote['author'])
    quote['author'] = str(authors[0].id)

    # tags from flat list to list[Tag] needed ?
    # not working
    # quote['tags'].clear()
    # quote['tags'] = [tag.name for tag in tags]

    Quotes.from_json(json.dumps(quote)).save()
