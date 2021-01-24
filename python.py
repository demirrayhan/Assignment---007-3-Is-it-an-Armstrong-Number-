while True:
  number = round(float(input('Please enter a positive number: ')))
  x = list(str(number))
  if int(number) >0:
    sum_a = 0
    for i in x: 
      int(i)**len(x)
      sum_a += int(i) ** len(x)
    if sum_a == int(number):
      print('{} is an Armstrong number'.format(number))
      break
    else :
      print('{} is not an Armstrong number'.format(number))
      break
  else:
    print(number,"is not a positive number")