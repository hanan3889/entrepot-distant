age = input("Entre ton age")
print("Ton age: "+ age)

if age>=16 and age<18:
  withAdult = input("AccompagnÃ© ? o ou n")

if age>=18:
  print("Tu peux entrer !")  
  elif age >= 16 and withAdult == "o":
    print("AccompagnÃ© ok")
  else:
    print("Get out !")  
