# French country names are feminine when they end with the letter “e”, masculine
# otherwise, except for the following which are masculine even though they end with
# “e”:
# • le Belize
# • le Cambodge
# • le Mexique
# • le Mozambique
# • le Zaïre
# • le Zimbabwe
# Write a program that reads the French name of a country and adds the article: “le”
# for masculine or “la” for feminine, such as le Canada or la Belgique. However, if the
# country name starts with a vowel, use “ l’ ”; for example, l’Afghanistan. For the
# following plural country names, use “ les ”:
# • les Etats-Unis
# • les Pays-Bas
# [P3.30]

exceptionE = ["Belize", "Cambodge", "Mexique", "Mozambique", "Zaïre", "Zimbabwe"]
exceptionLES = ["Etats-Unis", "Pays-Bas", "hello-etc"]
country = input("Enter the name of a French country: ")
vowels = ["A", "E", "I", "O", "U"]
vowelStart = (country.capitalize()).startswith(tuple(vowels))

if country in exceptionLES:
    print((f"les {country.capitalize()}"))
elif vowelStart:
    print(f"l'{country.capitalize()}")
elif country.endswith("e") and country not in exceptionE:
    print(f"la {country.capitalize()}")
else:
    print(f"le {country.capitalize()}")
