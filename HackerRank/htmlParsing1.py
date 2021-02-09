from html.parser import HTMLParser

n = int(input())


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        for element in attrs:
            print(f"-> {element[0]} > {element[1]}")

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        for element in attrs:
            print(f"-> {element[0]} > {element[1]}")


parser = MyHTMLParser()
parser.feed(''.join([input() for i in range(n)]))
parser.close()