#The counter function counts down from start to stop when start is bigger than stop, and counts up from start to stop otherwise. Fill in the blanks to make this work correctly.

#Solution
def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x >=stop:
				return_string += "," + str(x -1)
			elif x == stop:
				return_string			
			break	

	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:				
				return_string += "," + str(x + 1) + "," + str(x + 2) + "," + str(x + 3) +"," + str(x + 4) + "," + str(x + 5) + "," + str(x + 6) + "," + str(x + 7) +"," + str(x + 8) + "," + str(x + 9)
			elif x == stop:
				return_string
			break
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"