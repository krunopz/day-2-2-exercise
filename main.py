# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
print(type(height));
print(type(weight));
bmi = float(weight) / (float(height)**2)

print(str(weight)+"/("+str(height)+"*"+str(height)+")="+str(round(bmi,2)))
print("\n Your BMI is:"+str(round(bmi)))