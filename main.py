import sys
import library as lib


try:
    initial_word = str(sys.argv[1])
    print("Got initial word: " + initial_word)
except IndexError:
    print("no initial word given, setting 'Password'")
    initial_word = 'Password'

try:
    depth = int(sys.argv[2])
    print("Got depth: " + str(depth))
except IndexError:
    print("no depth given, using 3")
    depth = 3


password_list = lib.call_functions(initial_word,depth)
password_list = lib.common_ends(password_list)
password_list_length = len(password_list)
print("Generated " + str(password_list_length) + " passwords")
print("first and last 3: " + str(password_list[0:3] + password_list[-3:]))

#for password in password_list:
#    if password[0:3] == 'PAS':
#        print(password)

file = open("generated_passwords.txt", "w")
for password in password_list:
    file.write(password + '\n')
file.close()

