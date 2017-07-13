def tree(val):
	return[None, val, None]
def data(node):
	if node is None:
		return None
	else:
		return node[1]

def yes(node, childe=None):
	if node is None:
		return None
	elif val is None:
		return node[0]
	else:
		node[0] = [None, child, None]

def no(node, child=None):
	if node is None:
		return None
	elif child is None:
		return node[2]
	else:
		node[2] = [None, child, None]

data(root, "Am I an object or a place? (YES/NO): ")

yes(root, tree("Am I bigger than a PC? (YES/NO): "))
no(root, tree("Am I human? (YES/NO): "))

yes(yes(root), tree("Am I a building? (YES/NO): "))
no(yes(root), tree("Am I being consumed as you use me? (YES/NO): "))
yes(no(root), tree("Am I fictional? (YES/NO): "))
no(no(root), tree("Can you fit me in a coffee mug? (YES/NO): "))

yes(yes(yes(root)), tree("Am I a salon? (YES/NO): "))
no(yes(yes(root)), tree("Am I New York? (YES/NO): "))
yes(no(yes(root)), tree("Am I Pizza? (YES/NO): "))
no(no(yes(root)), tree("Am I a hat? (YES/NO): "))
yes(yes(no(root)), tree("Am I Santa Clause? (YES/NO): "))
no(yes(no(root), tree("Am I Michael Jackson? (YES/NO): "))
yes(no(no(root), tree("Am I a rat? (YES/NO): "))
no(no(no(root), tree("Am I Dracula? (YES/NO): "))

tracker = root
while "?" in data(tracker):
	answer = input(data(tracker))
	if answer == "YES":
		tracker = yes(tracker)
	else:
		tracker = no(tracker)
		
print(data(tracker))
