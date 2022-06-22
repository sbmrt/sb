world_map = ['white','black','black','white','white','black','white','black','black','black',
       'black','white','white','black','white','white','black','white','black','white',
       'white','black','black','white','black','white','black']


class Robot:
    
    def __init__(self, world_map):
        '''
        (self, list) -> None 
        '''        
        self.world_map = world_map 
        self.possible_locations = set(range(len(world_map)))
        
        
    def sense(self):
        '''
        (self) -> str
        Prompt the user for a sensor reading at the current location and return it
        ''' 
        invalid_input = True 
        while invalid_input: 
            sensor_value = input("Input observed colour (black/white):")
            if sensor_value == "white" or sensor_value == "black":
                invalid_input = False
            else:
                print("Invalid input!")
        return sensor_value
    
    
    def localize(self, sensor_value):
            """
            (self,str) -> NoneType
            Examine all the possible locations and remove those that are
            not consistent with sensor_value
            """
            # self.possible_locations contains the set of all possible locations
            # given the new sensor reading (sensor_value) remove any locations
            # that can not be the current position
            
            new_locations = set()
            for location in self.possible_locations:
                if self.world_map[location] == sensor_value:
                    new_locations.add(location)
            self.possible_locations = new_locations
        
        
    def move(self):
            '''
            (self)->NoneType
            Move one cell to the right (wrapping around)
            '''
            print("*** MOVE ***")
            
            new_locations = set()
            for location in self.possible_locations:
                location += 1 
                if location >= len(self.world_map):
                    location = 0
                new_locations.add(location)
                
            self.possible_locations = new_locations 
    
    
    def has_possible_locations(self):
        """
        (self) -> bool
        Return True if the robot has at least one location where it could be
        """
        
        # if sets are empty, returns False
        # if sets are not empty, returns True 
        return self.possible_locations
    
    
    def is_localized(self):
            """
            (self) -> bool
            Return True if the robot has only one location where it could be
            """
            return len(self.possible_locations) == 1
    
    def __str__(self):
            """
            (self)->str
            Return information about the state of the Robot in a string
            """
            s = "-------------\n"
            if self.is_localized():
                s += "\nLocalized at position: " + str(self.possible_locations) + "\n"
            else:
                s += "Not localized. Possible locations: " + str(self.possible_locations) + \
                "\n-------------\n"      
            return s    
    

'''         
# create localization instance
robot = Robot(world_map)

print("Before doing anything")
print(robot)

sensor_value = robot.sense()
robot.localize(sensor_value)
print(robot)

while(robot.has_possible_locations() and not robot.is_localized()):
    robot.move()
    sensor_value = robot.sense()
    robot.localize(sensor_value)
    print(robot)

if (not robot.has_possible_locations()):
    print("Something went wrong")
else:
    print("Success! The robot is at position: ", robot.possible_locations)



'''




# help(str)
# help(list)
# help(tuple)
# help(dict)
# help(set)

'''

list1 = [2, 2, 3, 4]
set1 = {1, 2, 3, 4}

list1.append("1")


set1.discard(1)


dictionary = {"k" : ["wee", "aiya"], 2:"woo", 3:"ye", 4:"meh", 5:"go"}
keys = []
items = []

for key, item in dictionary.items():
    keys.append(key)
    items.append(item)


print(keys)
print(items)

good = {1, 2, 3, 4}
bad = {3,4,5,6}
meh = good | bad
for mehs in meh:
    print(mehs)
 
items = dictionary.items()
keys = dictionary.keys()
values = dictionary.values()


a, list_keys, list_values = [],[],[]

for item in items:
    a.append(item)
for key in keys:
    list_keys.append(key)
for value in values:
    list_values.append(value)
    
for key in dictionary:
    for dictionary[key] in dictionary:
        print(key, dictionary[key])
print(list(items)[0])
print(list(keys)[1])
print(list(values)[0])
'''
class Node:
    '''An object that represents and element in a linked list'''
    
    def __init__ (self, cargo = None, next = None):
        '''
        (self,object,Node) -> NoneType
        '''        
        self.cargo = cargo 
        self.next = next 
        
    def __str__ (self):
        '''
        (self) -> str
        '''
        return str(self.cargo)
    
    def print_list(n):
        '''
        (Node) -> None
        Prints a linked list of Nodes
        '''
        while n != None:
            print(n)
            n = n.next
    
    def remove_second(list):
        if node is None:
            return 
        
        first = node
        second = node.next
        
        first.next = second.next
        second.next = None
        return second

    def print_backward(self):
        if self.next != None: 
            self.next.print_backward()       # recusion nooooooooooo
        print(self, end = " ")
    
    



node = Node("test")
print(node)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# link the nodes
node1.next = node2
node2.next = node3

# iterate through linked list
my_list = [3,4,5,6,7]
head = node1 
for c in my_list:
    n = Node(c)
    n.next = head
    head = n
    
n = head
while n != None:
    print(n)
    n = n.next