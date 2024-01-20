from models import Author, Quotes #, Tag
# from datetime import datetime
import json
import connect

def read_json(file):
    with open(file, "r", encoding='utf-8') as f:
        return json.load(f)
    
def main():
    authors = read_json("authors.json")
    quotes = read_json("quotes.json")

    for author in authors:
        # born_date to datetime conversion needed ?
        # text_date = author['born_date']
        # author['born_date'] = str(datetime.strptime(text_date, "%B %d, %Y").date())
        # Author.from_json(json.dumps(author)).save()
        Author(**author).save()

    for quote in quotes:
        # assuming author records are unique
        # authors = Author.objects(fullname=quote['author'])
        # quote['author'] = str(authors[0].id)
        author_name = Author.objects(fullname=quote['author']).first()
        quote['author'] = author_name

        # tags from flat list to list[Tag] needed ?
        # not working
        # quote['tags'].clear()
        # quote['tags'] = [tag.name for tag in tags]

        # Quotes.from_json(json.dumps(quote)).save()
        Quotes(**quote).save()

if __name__ == "__main__":
    main()