from models import Author, Quotes 
import connect_mongo
import connect_redis as redis

@redis.cache
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

@redis.cache
def quotes_by_tags(tags_string: str) -> list:
    quotes = []
    tag_list = tags_string.split(',')
    for tag in tag_list:
        for rec in Quotes.objects(tags__istartswith=tag):
            # istartswith does not work as tags is a list
            quotes.append(rec.quote)
    return quotes

def output(result):
    if result == [] or result == "":
        result = "Not found, sorry"
    print(result)

def main_loop():
    while True:
        entered = input("What? ")
        if entered in ['exit', 'q', 'bye']:
            output("Bye!")
            break
        try:
            k, v = entered.split(':')
        except ValueError:
            output("What do you mean?")
            continue

        # result = []
        if k == "name":
            result = quotes_by_author(v.strip())
        elif k in ["tags", "tag"]:
            result = quotes_by_tags(v.strip())
        else:
            result = "Incorrect command, please try again."     

        output(result)


if __name__ == "__main__":
    main_loop()