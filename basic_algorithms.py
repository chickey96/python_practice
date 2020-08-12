def sum_list(list):
  sum = 0
  for num in list:
    sum += num

  print(sum)
  return sum

# number_list = [1, 2, 3]
# sum_list(number_list)
# number_list.append(-4)
# sum_list(number_list)

# does not handle punctuation or capitalization at the moment
def reverse_words(sentence):
  words = sentence.split(" ")
  answer = []

  for word in words:
    answer.append(word[::-1])

  answer = " ".join(answer)
  print(answer)
  return answer

reverse_words("Here are some words to reverse")