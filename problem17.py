def worderize(n):
  output = None
  tens_list = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
  ones_list = ['one', 'two', 'three','four', 'five', 'six', 'seven', 'eight', 'nine']
  teens = ['ten', 'eleven', 'twelve', 'thirteen','fourteen', 'fifteen', 'sixteen', 'seventeen','eighteen', 'nineteen']

  string_n = str(n)
  if len(string_n) == 1:
    output = ones_list[n-1]
  elif len(string_n) == 2:
    tens_place = int(string_n[0])
    ones_place = int(string_n[1])
    if tens_place == 1:
      output = teens[ones_place]
    else:
      if ones_place == 0:
        output = tens_list[tens_place-2]
      else:
        output = tens_list[tens_place-2] +' '+ones_list[ones_place-1]
  elif len(string_n) == 3:
      ones_place = int(string_n[2])
      tens_place = int(string_n[1])
      hundreds_place = int(string_n[0])
      if ones_place == 0 and tens_place == 0:
        output = ones_list[hundreds_place-1]+' hundred'
      else:
        if tens_place != 1:
          output = ones_list[hundreds_place-1] + ' hundred and '
          if tens_place == 0:
            output += ones_list[ones_place-1]
          else:
            if ones_place == 0:
              output += tens_list[tens_place-2]
            else:
              output += tens_list[tens_place-2] + ' '
              output += ones_list[ones_place-1]
        else:
          output = ones_list[hundreds_place-1] + ' hundred and '
          output += teens[ones_place]

  return output   
  
def letterCounter(s):
  count = 0
  for c in s:
    if c.isalpha():
      count += 1
  return count

lettercount = 0
for n in range(1, 1000):
  wordnum = worderize(n)
  lettercount += letterCounter(wordnum)

print(lettercount + 11)

# Output: 21124
