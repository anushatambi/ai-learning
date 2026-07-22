def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        category = "Normal"
    else:
        category = "Overweight"
    return f"BMI: {bmi:.2f}, Category: {category}" 
print(calculate_bmi(80, 1.8))
#note: return exits the function immediately,the moment Python hits it, 
#      it leaves the function. Everything below it is ignored.


def word_count(text):
    words = text.split(" ")
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1 
    return count
print(word_count("Hello, how are you?"))


celsius_to_fahrenheit = lambda c : (c*(9/5))+32
print(celsius_to_fahrenheit(20)) 


def get_evens(*numbers):
    even = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
    return even
print(get_evens(2, 3, 4, 5, 6, 7, 8))
