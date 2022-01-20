def ask():
	answer = input("do you want to enter another value? (y,n)	")
	if answer.strip() ==  "y":
		return True
	else:
		return False


def fibSequence(x):
	# given an intiger x should return febanaci value
	# base case to exit loop
	if x <= 2:
		return 1
	else:
		return fibSequence(x - 2) + fibSequence(x - 1)

keepGoing = True
while keepGoing:
	request = int(input("give me a number: "))
	answer = fibSequence(request)
	print(answer)
	keepGoing = ask()

