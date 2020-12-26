english = ["good morning","it's a pleasure to meet you", "please call me tomorrow", "have a nice day"]
italian = ["buongiorno", "è un piacere conoscerti", "perfavore chiama domani", "buona giornata"]
mod = int(input("1 or 2?"))

if mod == 1:
  for x in range(0,len(english)):
   print("english \t", english[x]," "*(27-len(english[x])),"|italian \t", italian[x])
elif mod == 2:
  while true:
    name = input("Enter the word to translate:")
    print("Enter x if you want to exit this mode")
    if name

  if name in english :
    print(name, "\t", italian[english.index(name)])
  elif name in italian:
    print(name, "\t", english[italian.index(name)])
  else: print("the world isn't in the dictionary")


