def merge(arr1,arr2):
    result = []
    # indice para arr1 y arr2
    # miestras que i sea menor que la longitud del arreglo 1 y j sea menor ala longitud del arreglo 2
    i, j = 0,0 # i lleva arr1, j arr2
    while 1 < len(arr1) and j < len(arr2):
        # mientras las dos indices no llegan al final el areglo vamos comparar el primer elemento sublista 1 y 2
        if arr1[i] < arr2[j]:
            result.append(arr1[i]):
            i += 1
            # en caso de el segundo sublista sea mas pequeño
        else:
    pass
def merge_sort(arr):
