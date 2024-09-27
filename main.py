numbers = [1,2,3,4,5]
number_i = 0

for i in numbers:
    number_i = i + number_i

print(number_i)

katta_kichi = [5,1,8,7,2]

katta_kichi.sort()
print(katta_kichi[0] ,katta_kichi[-1])
fruits = ['Anor', 'Banan', 'Olma', 'Nok',]
print(fruits)
new_fruit = input('New fruit: ')
change_fruit = input('Change fruit: ')


for i in range(len(fruits)):
    if fruits[i] == change_fruit:
        fruits.remove(fruits[i])
        fruits.insert(i, new_fruit)
print(fruits)


nums = [2, 6, 5, 8, 3, 5, 4] 
nums_len = 0
for i in nums:
  nums_len += 1


print(nums_len)