arr1 = [', Graduado, Terciario/Tecnico.']
arr2 = ['Ingeniero De Sistemas', ', Graduado, Universitario.']
arr3 = ['Project Management Professional (Pmp)', '', ', Graduado, Otro.']

arr = [arr1, arr2, arr3]
for elem in arr:
    second = elem[-1]
    print(second)
    first = "".join(elem[0:-1])
    print(first)