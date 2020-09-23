
var = input("Eneter equation:")
#var2 = ["5","5","10","5","5"]
var = var.split("+")
sum = 0
for term in var:
    sum += int(term)

print(sum)