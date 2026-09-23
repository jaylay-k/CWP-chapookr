Original_array = [2, 8, 9, 48, 8, 22, -12, 2]
print(Original_array)

New_array = []
for i in range(len(Original_array)) :
    if Original_array[i] > 5 :
        New_array.append(Original_array[i] + 2)
        
print(New_array)