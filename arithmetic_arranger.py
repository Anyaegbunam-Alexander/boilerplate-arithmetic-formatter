def check_list_len(problems):
  return len(problems) <= 5

def check_chrs_len(chr1, chr2):
  return len(chr1) and len(chr2) <= 4

def check_digits(chr1, chr2):
  try:
    int(chr1) and int(chr2)
    return True
  except:
    return False

def check_operand(b):
  for i in b:
    i = i.split()
    if i[1] == '+' or i[1] == '-':
      res = True
    else:
      res = False
      break
  return res

def arithmetic_arranger(problems, ans=False):
  if not check_list_len(problems):
    return 'Error: Too many problems.'

  if not check_operand(problems):
    return "Error: Operator must be '+' or '-'."

  line1 = line2 = line3 = line4 = ""
  s_space = "    "
  begin  = True
  for arr in problems:
    b = arr.split()
    num1, oper, num2 = b[0], b[1], b[2]
    if not check_chrs_len(num1, num2):
      return 'Error: Numbers cannot be more than four digits.'
        
    if not check_digits(num1, num2):
      return 'Error: Numbers must only contain digits.'
    
    space = (max(len(num1), len(num2)))

    if begin:
      line1 += num1.rjust(space + 2)
      line2 += oper + ' ' + num2.rjust(space)
      line3  += '-'*(space + 2)
      if oper == '+':
        line4 += str(int(num1) + int(num2)).rjust(space + 2)
      else:
        line4 += str(int(num1) - int(num2)).rjust(space + 2)

      begin = False
    else:
      line1 += num1.rjust(space + 6)
      line2 += oper.rjust(5) + ' ' + num2.rjust(space)
      line3  += s_space + '-'*(space + 2)
      if oper == '+':
        line4 += s_space + str(int(num1) + int(num2)).rjust(space + 2)
      else:
        line4 += s_space + str(int(num1) - int(num2)).rjust(space + 2)
  if ans == True:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3
  
  return arranged_problems

print(arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]))
