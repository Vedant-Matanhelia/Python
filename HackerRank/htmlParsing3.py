from html.parser import HTMLParser


n = int(input())


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for element in attrs:
            print(f"-> {element[0]} > {element[1]}")


parser = MyHTMLParser()
parser.feed("".join([input() for i in range(n)]))
parser.close()