score = input("Enter Score: ")
n = float(score)
x = 'Error'
if n >= 0.9:
    x = 'A'
elif n >= 0.8:
    x = 'B'
elif n >= 0.7:
    x = 'C'
elif n >= 0.6:
    x = 'D'
elif n < 0.6:
    x = 'F'
else:
    x = 'Error'
print (x)
