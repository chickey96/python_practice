def sum_list(list):
  sum = 0
  for num in list:
    # print(num)
    sum += num

  # print(sum)
  return sum

number_list = [1, 2, 3]
print(sum_list(number_list))
number_list.append(4)
print(sum_list(number_list))
