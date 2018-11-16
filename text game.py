import random

def msg(room):
    if room['msg']=='': #there is a custom message
        return "You Have entered the " + room['name'] + '.'
    else:
        return room['msg']

def get_choice(room,dir):
    if dir=='N':
        choice = 0
    elif dir=='E' :
        choice = 1
    elif dir=='S':
        choice = 2
    elif dir=='W':
        choice = 3
    else:
        return  -1

    if roomp['directions'][choice] == 0:
        return 4
    else:
        return choice

    def main():
        dirs = (0,0,0,0)   #default

        enterance = {'name' : 'Entrance way' , 'directions' : dirs, 'msg ' : ''}
        livingroom = {'name' : 'Livingroom' , 'directions' : dirs, 'msg ' : ''}
        hallway = {'name' : '' , 'Hallway' : dirs, 'msg ' : ''}
        kitchen = {'name' : 'Kitchen' , 'directions' : dirs, 'msg ' : ''}
        diningroom = {'name' : 'Diningroom' , 'directions' : dirs, 'msg ' : ''}
        family_room = {'name' : 'Family Room' , 'directions' : dirs, 'msg ' : ''}

        #directions are tuples : rooms to the (n,e,s,w)
        entrance['directions'] = (kitchen,livingroom,0,0)
        livingroom['directions'] = (diningroom,0,0,enterance)
        hallway['directions'] =  (0,kitchen,0,family_room)
        kitchen['directions'] = (0,0,livingroom,kitchen)
        diningroom['directions'] = (0, 0, livingroom, kitchen)
        family_room['directions'] = (0,hallway,0,0)

        #rooms where johny,s basket might be
        room = [livingroom,hallway,kitchen,diningroom,family_room]
        room_with_eggs = random.choice(rooms)
        eggs_delivered =  False
        room=entrance
        print('Welcome, Bunny! Can you find Johnny\'s basket?')

        while True:
            if eggs_delivered and room['name'] == 'Entrance  Way' :
                print('you have delivered the eggs and returned to the entrance. ' + 'yo  u can now leve. Congrats!')
                break;
            elif not eggs_delivered and room['name'] == room_with_eggs['name']:
                eggs_delivered = True
                print(msg(room) + 'There\'s the basket and johnny is sleeping ' +
                      'right next to it ! You have delivered the eggs. '+
                      'Now get out quick!')
                room['msg'] = ('you are back in the ' + room ['name'] +
                               '! You already delivered the eggs. ' +
                               'Get out of here before Johny wakes up!')
            else:
                print(msg(room))
                room['msg'] = 'You are back in the ' + room['name']


            stuck = True
            while stuck:
                dir = input ("which direction do you want to go : N ,E,S,or, W?")
                choice = get_choice(room,dir)
                if choice == -1:
                    dir = print("Please enter N,E S,or W?")
                elif choice == 4:
                    dir = print('You cannot go in the direction.')
                else:
                    room = room['directions'][choice]
                    stuck = False
        main()







