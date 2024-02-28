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
            result.append (arr2[j])
            j += 1
            # si arr1 se termina las sublista 
            if i == len(arr1):
                # colocar sublista del otro elemento
                for k in range(j, len(arr2)): result.append(arr2[k])
                 #si nos acaba la lista ponemos las dos lista
                if j == len(arr2):
                    for k in range(i, len(arr1)): result.append(arr2[k])
                    return result
                
                

def merge_sort(arr):
    pass
    
