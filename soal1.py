def getMiddleNumber(number1, number2, number3):
    sortedNumbers = sorted([number1, number2, number3])
    middleNumber = sortedNumbers[1]
    return middleNumber

number1 = int(input("Masukkan angka pertama: "))
number2 = int(input("Masukkan angka kedua: "))
number3 = int(input("Masukkan angka ketiga: "))

middleNumber = getMiddleNumber(number1, number2, number3)

print("Bilangan yang merupakan nilai tengah adalah:", middleNumber)
