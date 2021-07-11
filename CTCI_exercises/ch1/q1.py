# solution for problem 1.1 isUnique

def isUnique(s):
	charList = [False] * 128
	for i in range(len(s)):
		curr_char = s[i]
		ascii_val = ord(curr_char)
		if charList[ascii_val] == False:
			charList[ascii_val] = True
		elif charList[ascii_val] == True:
			return False
	return True


print('Sarah -> ',isUnique('Sarah'))

print('chapter -> ', isUnique('chapter'))
