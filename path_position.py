import random


test = [3, 4, 10, 100, 3000]




print(random.sample(test, 2)[1])
print(random.sample(test, 2)[0])



random.seed(random.sample(test, 2)[0])

print(random.sample(test, 2)[1])
print(random.sample(test, 2)[0])




"""print(test)

position_object_1 = random.seed(test)

print(position_object_1)"""
"""self.position_object_2 = random.seed(self.list_random_position[1])
self.position_object_3 = random.seed(self.list_random_position[2])

return self.position_object_1, self.position_object_2, self.position_object_3""" 


