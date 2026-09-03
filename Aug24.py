# Strings are immutable (cannot be changed in place)
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)

# 1. upper() - Converts to uppercase
print(a.upper())

# 2. lower() - Converts to lowercase
print(a.lower())

# 3. rstrip() - Strips trailing specified characters
print(a.rstrip("!"))

# 4. replace() - Replaces all occurrences of a substring
print(a.replace("Harry", "John"))

# 5. split() - Splits string into a list at specified delimiter
print(a.split(" "))

# 6. capitalize() - First character uppercase, rest lowercase
blogHeading = "introduction tO pYtHoN"
print(blogHeading.capitalize())

# 7. center() - Centers string aligned to given width
str1 = "Welcome to the Console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))

# 8. count() - Counts occurrences of substring
print(a.count("Harry"))

# 9. endswith() - Checks if string ends with a value
str2 = "Welcome to the Console !!!"
print(str2.endswith("!!!"))
print(str2.endswith("to", 4, 10)) # Optional slice check

# 10. find() - Finds first index of substring (returns -1 if missing)
str3 = "He's name is Dan. He is an honest man."
print(str3.find("ishh"))
# print(str3.index("ishh")) # Throws ValueError instead of -1

# 11. isalnum() - Checks if alphanumeric (A-Z, a-z, 0-9)
str4 = "WelcomeToTheConsole"
print(str4.isalnum())

# 12. isalpha() - Checks if alphabetic only (A-Z, a-z)
print(str4.isalpha())

# 13. islower() - Checks if all characters are lowercase
print(str4.islower())

# 14. isprintable() - Checks if all characters can be printed
str5 = "We wish you a Merry Christmas\n"
print(str5.isprintable()) # False due to escape sequence \n

# 15. isspace() - Checks if string contains only whitespaces
str6 = "        " # using Spacebar or Tab
print(str6.isspace())

# 16. istitle() - Checks if string is in titlecase
str7 = "To Kill A Mockingbird"
print(str7.istitle())

# 17. isupper() - Checks if all characters are uppercase
str8 = "WORLD HEALTH ORGANIZATION"
print(str8.isupper())

# 18. startswith() - Checks if string starts with a value
print(str8.startswith("WORLD"))

# 19. swapcase() - Swaps uppercase to lowercase and vice versa
str9 = "Python is a Programming Language"
print(str9.swapcase())

# 20. title() - Converts string to titlecase
str10 = "His name is Dan. he is an honest man."
print(str10.title())


