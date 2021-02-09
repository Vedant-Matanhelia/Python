import textwrap

def wrap(text, width):
	return '\n'.join(textwrap.wrap(text, width))

if __name__ == '__main__':
	string, width = input(), int(input())
	result = wrap(string, width)
	print(result)
