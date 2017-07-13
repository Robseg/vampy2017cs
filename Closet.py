id = 0
tops = ["Red","Orange","Yellow","Green","Blue","Grey","bloodofmyenemies"]
bottoms = ["Jeans","Khakis","Shorts","Sweatpants","Swimmingtrunks","bloodofmyenemies"]
shoes = ["Nosoles","Wearables","bloodofmyenemies"]
headgear = ["none","bloodofmyenemies"]
socks = ["goodones","badones","okayones","bloodofmyenemies"]

pattern = "#{0}: Top={1}, Bottom={2}, Shoes={3}, Head={4}, Socks={5}"
for top in tops:
	for bottom in bottoms:
		for kicks in shoes:
			for headitem in headgear:
				for pair in socks:
					if kicks != "Nosoles" and pair == "bloodofmyenemies"
						continue
					id += 1
					print(pattern.format(id, top, bottom, kicks, headitem, pair))
