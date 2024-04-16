#Create a TV class with properties and Specify brand in a constructor parameter.
class TVClass: #all python3 classes inherit from object
        def __init__(self, volume = 0, channel = 0):
                self.volume = volume
                self.channel = channel

        def setVolume(self, volume): #reference to instance as first arg
                if not 0 <= volume <= 100:
                        print('Volume out of bounds.')
                        return #return without setting member
                self.volume = volume #setting member

        def setChannel(self, channel):
                if not 0 <= channel<= 100:
                        print('Channel out of bounds.')
                        return
                self.channel = channel

        def __str__(self): #for printing it
                return 'Volume is {} and channel is {}.'.format(self.volume, self.channel)

tv = TVClass() #calling init

while True:
        choice = input('''ClassTV

0 - Turn off TV
1 - TV status
2 - Change channel
3 - Change volume
''')
        if choice == '0': break
        if choice == '1':
                print(tv) #calling __str__
                continue
        if choice == '2':
                tv.setChannel(int(input('New channel: ')))
                continue
        if choice == '3':
                tv.setVolume(int(input('New volume: ')))
                continue
        print('Unkown command.')