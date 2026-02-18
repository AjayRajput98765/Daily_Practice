def convert_temp(celsius):

    F = (celsius * 9/5) + 32

    return F



temp = float(input("Enter temp in Celsius :"))

faraday = convert_temp(temp)
print(faraday)