def title(content):
	size = len(content)
	space = 3
	
	return '*' * (size + space * 2 + 2) + '\n'\
		+ '*' + ' ' * (size + space * 2) + '*\n' \
		+ '*' + ' ' * space + content + ' ' * space + '*\n' \
		+ '*' + ' ' * (size + space * 2) + '*\n' \
		+ '*' * (size + space * 2 + 2)