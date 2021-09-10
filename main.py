# Step 1 take user input as max loop amount, i will be loop counter, solution will be output

n = int(input())
i = 0
solution = 0

# Step 2 run loop. take input, power will be last character in input, reassign p to minus last character
# find p to the power of power, and add to solution
while i < n:
    p = input()
    power = p[len(p) - 1]
    p = int(p[:-1])
    solution = (p ** int(power)) + solution
    i += 1
# Step 3 print solution
print(solution)

