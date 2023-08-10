class Player:
    
    def __init__(self, name, agent, weapon):

        self.name = name
        self.agent = agent
        self.weapon = weapon

    def playerStats(self):
        
        print(f'Your username is {self.name} and your favorite agent is {self.agent}. You enjoy using the {self.weapon} but I think you should use the Judge instead.')

player1 = Player("McFoolery", "Jett", "Vandal")

player1.playerStats()