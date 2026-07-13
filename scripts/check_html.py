from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.void_elements = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}

    def handle_starttag(self, tag, attrs):
        if tag not in self.void_elements:
            self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag in self.void_elements:
            return
        if not self.stack:
            print(f"Error: Found closing tag </{tag}> but stack is empty")
            return
        if self.stack[-1] == tag:
            self.stack.pop()
        else:
            print(f"Error: Found closing tag </{tag}> but expected </{self.stack[-1]}>")

parser = MyHTMLParser()
with open('apps/people/index.html', 'r') as f:
    parser.feed(f.read())

print(f"Remaining stack: {parser.stack}")
