def weightConversion():

    weight = input("Please enter your weight: ")
    conversion = input("Are you using (L)bs or (K)g? Please Type L for Lbs and K for Kg: ")

    if conversion == "l":
        print(conversion)
        weight = float(weight)
        weight = weight * 0.45359237
        weight = round(weight, 2)
        print("You are " + str(weight) + " kilos")
    else:
        print("this is the conversion" + conversion)
        weight = float(weight)
        weight = weight * 2.20462
        weight = round(weight, 2)
        print("You are " + str(weight) + " pounds")

weightConversion()