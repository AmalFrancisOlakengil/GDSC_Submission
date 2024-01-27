sentence = input("Enter a sentence:\n")

List_sent = sentence.split()
new_word = ""
for i in range(0,len(List_sent)):
      word = List_sent[i]
      if word == word[::-1]:
          new_word += word+" "
      else:
        new_word += word[:-1]+word[::-1]+" "
print(new_word)
