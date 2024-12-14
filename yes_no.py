def getYesNo(answer):
  s = answer
  if s == "" or s == " ":
    return False
  y =  "yes_words.txt"
  n =  "no_words.txt"
  Fy = open(y, "a")
  Fn = open(n, "a")
  condY = searchLn(s, y)
  condN = searchLn(s, n)
  while not (condY or condN):
    q = "Does " + s + " mean "
    temp = input(q + "yes? ")
    if getYesNo(temp):
      Fy.write(s + "\n")
      condY = True
    else:
      temp = input(q + "no? ")
      if getYesNo(temp):
        Fn.write(s + "\n")
        condN = True
  Fy.close()
  Fn.close()
  return condY

def searchLn(s, fn):
  temp = s + "\n"
  with open(fn, "r") as f:
    lst = f.readlines()
    for ln in lst:
      if (ln.lower() == temp.lower()):
        return True
    return False

test = input('Yes or no? ')
getYesNo(test)
