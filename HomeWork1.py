'''
Kullanıcıdan 5 değer alınıp, alınan değerler ekrana yazdırılacak ve değerlerin türü ekrana yazdırılacak.
f-string ve format kullanılacak.
'''

one = int(input("1st Value :"))
two = input("2nd Value :")
three = int(input("3rd Value :"))
four = float(input("4th Value :"))
five = input("5th Value :")

print(f'1st Value : {one}, Type of value 1st :{type(one)}')
print(f'2nd Value : {two}, Type of value 2nd :{type(two)}')
print("3rd Value : {}, Type of value 3rd :{}".format(three,type(three)))
print("4th Value : {}, Type of value 4th :{}".format(four,type(four)))
print(f'5th Value : {five}, Type of value 2nd :{type(five)}')
