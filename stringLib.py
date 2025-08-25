import string

print(string.ascii_letters)   # All letters (a-z + A-Z)
print(string.ascii_lowercase) # Lowercase letters (a-z)
print(string.ascii_uppercase) # Uppercase letters (A-Z)
print(string.digits)          # All digits (0-9)
print(string.hexdigits)       # Hex digits (0-9 + a-f + A-F)
print(string.octdigits)       # Octal digits (0-7)
print(string.punctuation)     # All punctuation symbols (!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~)
print(string.whitespace)      # All whitespace characters (\t, \n, space, etc.)
 

from string import Template

p=Template("Hello! This is $name from $place")
message=p.substitute(name="Muthuswamy" ,place="Kanyakumari")
print(message)