def menu(menuItems):
	menuString = "Choose an item from the list:\n"
	for key, value in menuItems.items():
		menuString = menuString + "\t" + key + "- " + value + ".\n"

	print(menuString)

def menu(menuchoice):
	menuString = "Choose an item from the list:\n"
	for key, value in menuchoice.items():
		menuString = menuString + "\t" + key + "- " + value + ".\n"

	print(menuString)