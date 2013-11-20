from crypt import *

global user_id

def generatePassWordFile(atype, users):

	passwd_file = open('passwd_'+atype+'.txt', 'w')

	global user_id
	for u in users:
		# user44:x:45:1045:GECOS:directory:shell45
		passwd_file.write(u+":x:"+str(user_id)+':1040:GECOS:dir:shell\n')
		user_id = user_id + 1

	return


def generateShadowFile(atype, users,passwords,salts):
	# user44:$1$vztckvJR$BxyXIVjlZKZCKXJ5vV0f8.:14538:0:99999:7:::
	# User name : It is your login name
	# Password: It your encrypted password. The password should be minimum 6-8 characters long including special characters/digits
	# Last password change (lastchanged): Days since Jan 1, 1970 that password was last changed
	# Minimum: The minimum number of days required between password changes i.e. the number of days left before the user is allowed to change his/her password
	# Maximum: The maximum number of days the password is valid (after that user is forced to change his/her password)
	# Warn : The number of days before password is to expire that user is warned that his/her password must be changed
	# Inactive : The number of days after password expires that account is disabled
	# Expire : days since Jan 1, 1970 that account is disabled i.e. an absolute date specifying when the login may no longer be used

	shadow_file = open('shadow_'+atype+'.txt', 'w')
	for i in range(0, len(users)):
		crypted_pass = crypt(passwords[i], salts[i])
		shadow_file.write(users[i] + ":" + crypted_pass + ":14538:0:99999:9:::\n")

	return


def main():
	global user_id
	user_id = 1000

	files = [
	(open('upFile_weak.txt', 'r'), 'weak'),
	(open('upFile_med.txt', 'r'), 'med'),
	(open('upFile_strong.txt', 'r'), 'strong'),
	(open('upFile_best.txt', 'r'), 'best')]

	for upFile in files:
		users = []
		passwords = []
		salts = []
		for l in upFile[0]:
			user_name, password, salt = l.split(' ')
			users.append(user_name)
			passwords.append(password)
			salts.append(salt)

		generatePassWordFile(upFile[1], users)
		generateShadowFile(upFile[1], users, passwords, salts)

	return

if __name__ == '__main__':
	main()