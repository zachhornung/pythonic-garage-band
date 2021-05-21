class Band:
    
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)
        
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return tuple(solos)
        
    @classmethod
    def to_list(cls):
        return cls.instances

class Musician:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'{self.__class__.__name__} instance. Name = {self.name}'


class Guitarist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play guitar'
    def get_instrument(self):
        return 'guitar'
    def play_solo(self):
        return 'face melting guitar solo'

class Bassist(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play bass'
    def get_instrument(self):
        return 'bass'
    def play_solo(self):
        return 'bom bom buh bom'

class Drummer(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play drums'
    def get_instrument(self):
        return 'drums'
    def play_solo(self):
        return 'rattle boom crash'
