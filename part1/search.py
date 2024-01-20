from models import Author, Quotes 
import connect

def quotes_by_author(name: str) -> list:
    quotes = []
    try:
        author = Author.objects(fullname__istartswith=name).first()
        records = Quotes.objects(author=author)
    except IndexError:
        # throws if not found
        records = []
    for record in records:
        quotes.append(record.quote)
    return quotes

def quotes_by_tags(tags_string: str) -> list:
    quotes = []
    tag_list = tags_string.split(',')
    for tag in tag_list:
        for rec in Quotes.objects(tags__istartswith=tag):
            # istartswith does not work 
            quotes.append(rec.quote)
    return quotes

# def search_quotes(name: None, tags: None):
#     quotes = []
#     if name:
#         authors = Author.objects(fullname=name)
#         records = Quotes.objects(author=authors[0].id)
#     elif tags:
#         tag_list = tags_string.split(',')
#         records = Quotes.objects(tags__in=tag_list)
#     else:
#         return "Not Found"
#     for record in records:
#         quotes.append(record.quote)
#     return quotes

def main_loop():
    while True:
        entered = input("What? ")
        if entered in ['exit', 'q', 'bye']:
            print("Bye!")
            break
        try:
            k, v = entered.split(':')
        except ValueError:
            print("What do you mean?")
            continue

        # result = []
        if k == "name":
            # list of quotes by author name
            result = quotes_by_author(v.strip())
        elif k in ["tags", "tag"]:
            # list of quotes by tag or tags
            result = quotes_by_tags(v.strip())
        else:
            result = "Incorrect command, try again."

        # result = search_quotes(k, v)
        if result == []:
            result = "Not found, sorry"
        print(result)



if __name__ == "__main__":
    main_loop()