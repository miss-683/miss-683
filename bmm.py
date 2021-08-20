a= int(input())
b= int(input())

if a > b :
    print("wrong answer...try again.")

for i in range(1 , a + 1):
    if a % i == 0 and b % i == 0 :
        bmm= i 

print("the answer is:")
print(bmm)