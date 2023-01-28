def multiplication_or_sum(num1, num2):
    # calculcate the two numbers
    product = num1 * num2
#print('The result is :',product)
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = multiplication_or_sum(20, 30)
print ("The multiple value is:", result)
result = multiplication_or_sum(40, 50)
print ("The sum value is:", result)


