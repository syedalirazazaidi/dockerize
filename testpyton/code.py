# print("Hello Python world!")
# message:str ="i this is aliraza"
# print(message.capitalize())

# first_name:str = "ada"
# last_name:str = "lovelace"
# full_name:str = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}!")

# name:str = "ada lovelace"
# print(name.title())

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)

# mycar:list[str] = ["car1","car2","car3",1]
# print(mycar)

# bicycles: list[str] = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles[-1])

# cars:list[str] = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# motorcycles :list[str] = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)

# too_expensive: str = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"A {too_expensive.title()} is too expensive for me.")

# motorcycles:list[str] = []

# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')

# print(motorcycles)

# motorcycles: list[str] = ['honda', 'yamaha', 'suzuki']

# motorcycles.insert(0, 'ducati')
# print(motorcycles)

# motorcycles:list[str] = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# del motorcycles[0]

# motorcycles.remove("suzuki")
# print(motorcycles)

# motorcycles:list[str] = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)

# popped_motorcycle:str = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles:list[str] = ['honda', 'yamaha', 'suzuki']

# last_owned:str = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")
# print(f"The last motorcycle I owned was a {motorcycles}.")

# dimensions:tuple[int,int] = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# dimensions:tuple[int,int,str] = (200, 50,"alir")
# print(dimensions[0])
# print(dimensions[2])
# dimensions[0] = 250

# dimensions:tuple[int,int] = (200, 50,1,2,3,4)
# for dimension in dimensions:
#     print(dimension)

# dimensions:tuple[int,int] = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions:tuple[int,int] = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# even_numbers:list[int] = list(range(3, 30, 3))
# print(even_numbers)

# for value in range(1, 5):
#     print(value)

# for value in range(1, 6):
#     print(value)

# for value in range(1, 6):
      
#           print("Modified dimensions: {value}")


# number:int = (range(1, 6))
# print(number)

# numbers:list[int] = list(range(1, 6))
# print(numbers)


# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[2:5])

# my_foods:list[str] = ['pizza', 'falafel', 'carrot cake']
# friend_foods:list[str] = my_foods[0:1]

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# my_foods:list[str] = ['pizza', 'falafel', 'carrot cake']
# friend_foods:list[str] = my_foods[:]

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)



# my_foods:list[str] = ['pizza', 'falafel', 'carrot cake']

# # This doesn't work:
# friend_foods = my_foods

# my_foods.append('cannoli')
# friend_foods.append('ice cream')

# print("My favorite foods are:")
# print(my_foods)

# print("\nMy friend's favorite foods are:")
# print(friend_foods)


# magicians:list[str] = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)


# magicians:list[str] = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# magicians:list[str] = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")

# print("Thank you, everyone. That was a great magic show!")

# magicians:list[str] = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
# print(f"I can't wait to see your next trick, {magician.title()}.\n")

# players:list[str] = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])

# players:list[str] = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-3:])

# squares:list[str] = []
# for value in range(1, 11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

# squares:list[int] = [value**2 for value in range(1, 11)]
# print(squares)

# dimensions:tuple[int, int] = (200, 50)
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)

# dimensions:tuple[int,int] = (400, 100)
# print("\nModified dimensions:")
# for dimension in dimensions:
#     print(dimension)

# numbers:tuple[int,int] = tuple(range(1, 6))

# numbers[0]=10
# print(numbers[0])
# banned_users: list[str] = ['andrew', 'carolina', 'david']
# user: str = 'andrew'

# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish.")
# else:
#     print(f"{user.title()}, this person is banned.")


# cars:list[str] = ['audi', 'bmw', 'subaru', 'toyota']

# for car in cars:
#     if car == 'bmw':
#         print(car.upper())
#     else:
#         print(car.title())
# answer:int = 17

# if answer != 42:
#     print("That is not the correct answer. Please try again!")

# alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])

# alien_0 = {'color': 'green', 'points': 5}

# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}

# alien_0['color'] = 'green'
# alien_0['points'] = 5

# print(alien_0)

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'color': 'green'}
# print(f"The alien is {alien_0['color']}.")

# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}.")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
# print(f"Original position: {alien_0['x_position']}")

# #  -----    answer :"Original position: 0"

# # Move the alien to the right.
# # Determine how far to move the alien based on its current speed.
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # This must be a fast alien.
#     x_increment = 3

# # The new position is the old position plus the increment.
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# #  ------  0 = 0 + 2
# print(f"New position: {alien_0['x_position']}")

# ------  New position 2


# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0)

# del alien_0['points']
# print(alien_0)

# alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['color'])

# alien_0 = {'color': 'green', 'speed': 'slow'}

# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]
# print(f"{aliens}")

# for alien in aliens:
#   print(alien)


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print("...")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")