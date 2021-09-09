def check_answer(choice):
  """Checks followers against user's guess 
  and returns True if they got it right.
  Or False if they got it wrong.""" 
  if choice == 4:
    return choice == 4
  else:
    return choice == 1000


choice = int(input("What number is between 3 and 5? "))

is_correct = check_answer(choice)

print("VALUE OF is_correct:")
print(is_correct)

if is_correct:
  print("THAT IS RIGHT!")

else:
  print("That's wrong!!!!!!!!!")

