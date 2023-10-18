row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

digit_1 = int(position[0])
digit_2 = int(position[1])


map[digit_2 -1][digit_1 -1] = "X"


print(f"{row1}\n{row2}\n{row3}")