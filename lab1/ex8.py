# Write a program that displays your name inside a box on the screen, like this:
#  +------+
#  ¦ Dave ¦
#  +------+
# Do your best to approximate lines with characters such as “ | ” ,“ - ”, “ + ”, “ . ”, “ ¦ ”.
name = input("write your name here: ")
print("+" + "-" * (len(name) + 2) + "+")
print(f"¦ {name} ¦")
print("+" + "-" * (len(name) + 2) + "+")

