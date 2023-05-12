import jellyfish
import itertools

dataArray = ["Ronaldo", "Orlando", "Romario", "Ronaldinho"]

for i in range(0, len(dataArray)):
    for j in range(i+1, len(dataArray)):
      print(dataArray[i], dataArray[j], jellyfish.jaro_distance(dataArray[i], dataArray[j]))


permutationsArray = list(list(elem) for elem in itertools.permutations(dataArray))

"""for testArray in permutationsArray:
  arrayEquivalence = []
  for i in range(len(testArray)-1, -1, -1):
    actualDistance = 0
    for j in range(0, i):
      print(testArray[i], testArray[j])
      if jellyfish.jaro_distance(testArray[i], testArray[j]) >= 0.7:
        arrayEquivalence.append({"origin": testArray[i], "destiny": testArray[j] })

  print(arrayEquivalence)"""

for testArray in permutationsArray:
  arrayEquivalence = []
  for i in range(0, len(testArray)):
    for j in range(i+1, len(testArray)):
      if jellyfish.jaro_distance(testArray[i], testArray[j]) >= 0.7:
        arrayEquivalence.append({"origin": testArray[i], "destiny": testArray[j] })

  print(arrayEquivalence)
