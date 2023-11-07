card_number = input("enter your card number")
card_number = [int(c) for c in card_number]
card_number.pop()
card_number.reverse()
length_num = len(card_number)
for num in (num for num in range(length_num) if num % 2 == 0):
    card_number[num] *=2
if sum(card_number) % 10 == 0:
    print("card numberis vallid")
else :
    print("card number is invallid")
            