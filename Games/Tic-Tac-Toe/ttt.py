transposeX = {}
transposeO = {}

class disp:

  def display():

    print("\n")
    line = " "
    for i in range(9):
      if position[i] in ["X", "O"]:
        if i % 3 == 2:
          line = line + position[i]
        else:
          line = line + position[i] + " | "
      else:
        if i % 3 == 2:
          line = line + str(i + 1)
        else:
          line = line + str(i + 1) + " | "
      if i % 3 == 2:
          print(line)
          if i < 8:
            print("---|---|---")
          line = " "
    print("\n")

class pos:

  def checkWin(l):

    r = None
    wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]
    ]
    xSpots = []
    oSpots = []
    blankSpots = []
    for i in range(9):
      if l[i] == " ":
        blankSpots.append(i)
      if l[i] == "X":
        xSpots.append(i)
      if l[i] == "O":
        oSpots.append(i)
    if blankSpots == []:
      r = 0
    for i in range(8):
        if (wins[i])[0] in xSpots and (wins[i])[1] in xSpots and (wins[i])[2] in xSpots:
          r = 1
        if (wins[i])[0] in oSpots and (wins[i])[1] in oSpots and (wins[i])[2] in oSpots:
          r = -1
    return r
  
  def openSpots(l):

    r = []
    for i in range(9):
      if l[i] == " ":
        r.append(i)
    return r
  
  def closedSpots(l):

    r = [-1]
    for i in range(9):
      if l[i] in ["X", "O"]:
        r.append(i)
    return r

class minimax:

  def maxX(l):

    try:
      transposeX[tuple(l)]
    except:
      pass
    else:
      return transposeX[tuple(l)]

    evals = []
    for i in pos.openSpots(l):
      minimaxTest = l[:]
      minimaxTest[i] = "X"
      if pos.checkWin(minimaxTest) != None:
        evals.append((i, pos.checkWin(minimaxTest)))
      else:
        evals.append((i, minimax.minO(minimaxTest)[1]))
    r = (pos.openSpots(l)[0], -1)
    for i in range(len(evals)):
      if (evals[i])[1] > r[1]:
        r = evals[i]
    
    transposeX[tuple(l)] = r
    return r

  def minO(l):

    try:
      transposeO[tuple(l)]
    except:
      pass
    else:
      return transposeO[tuple(l)]

    evals = []
    for i in pos.openSpots(l):
      minimaxTest = l[:]
      minimaxTest[i] = "O"
      if pos.checkWin(minimaxTest) != None:
        evals.append((i, pos.checkWin(minimaxTest)))
      else:
        evals.append((i, minimax.maxX(minimaxTest)[1]))
    r = (pos.openSpots(l)[0], 1)
    for i in range(len(evals)):
      if (evals[i])[1] < r[1]:
        r = evals[i]
    
    transposeO[tuple(l)] = r
    return r

again = "yes"

while again == "yes":

  position = [
  " ", " ", " ",
  " ", " ", " ",
  " ", " ", " "
  ]

  humanSymbol = input("X or O? (X goes first)\n>>> ")
  if humanSymbol not in ["X", "O", "x", "o", "0"]:
    humanSymbol = "X"
  if humanSymbol in ["X,", "x"]:
    humanSymbol = "X"
  if humanSymbol in ["O", "o", "0"]:
    humanSymbol = "O"

  turn = "X"

  for i in range(9):
    disp.display()
    if turn == humanSymbol:
      move = 0
      while move - 1 in pos.closedSpots(position):
        move = int(input("Input number of square you'd like to move to:\n>>> "))
      position[move - 1] = turn
    else:
      if humanSymbol == "O":
        move = minimax.maxX(position)[0]
        position[move] = turn
        print("AI chooses square " + str(move + 1))
      else:
        move = minimax.minO(position)[0]
        position[move] = turn
        print("AI chooses square " + str(move + 1))
    if pos.checkWin(position) == -1:
      disp.display()
      if humanSymbol == "O":
        print("You win")
      else:
        print("AI wins")
      break
    elif pos.checkWin(position) == 1:
      disp.display()
      if humanSymbol == "X":
        print("You win")
      else:
        print("AI wins")
      break
    elif pos.checkWin(position) == 0:
      disp.display()
      print("Draw")
      break
    elif turn == "X":
      turn = "O"
    else:
      turn = "X"
  
  again = input("\nPlay again? Yes/No:\n>>> ")
  again = again.lower()
  if again == "y":
    again = "yes"
