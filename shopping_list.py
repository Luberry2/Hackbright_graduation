shopping_list = ["apples", "oranges", "milk"]

def adding_item(shopping_list):
	new_item = raw_input("What do you need to add to your list?: ").lower()
	if new_item in shopping_list: # to check whether the item is already in the list
		print "Oops! You already have it on the list!"
		return

	shopping_list.append(new_item)
	shopping_list.sort()
	print "Here is your new list!" + str(shopping_list)
	return


def removing_item(shopping_list):
	unnecessary_item = raw_input("What do you need to remove from your list?: ").lower()
	if unnecessary_item in shopping_list:
		shopping_list.remove(unnecessary_item)
		shopping_list.sort()
		print "%s is now removed from your list!" %(unnecessary_item)
		print "Here is your new list!" + str(shopping_list)
		return

	print "It looks like you don't have %s in your list." %(unnecessary_item)
	return

questions1 = raw_input("Please select 1 to add items or 2 to remove items: ")

def main():
	if questions1 == "1":
		adding_item(shopping_list)

	else:
		removing_item(shopping_list)


if __name__ == '__main__':
	main()