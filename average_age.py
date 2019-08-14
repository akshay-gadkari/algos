class User:
  def __init__(self, age):
    self.age = age


users = [User(20), User(10), User(30)]
print(users)

def find_average_age(users):
  num_of_users = len(users)
  sum = 0
  for user in users:
    sum += user.age
  print(sum)
  average = sum / num_of_users
  print(average)
  return average

find_average_age(users)
