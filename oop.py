#create super class  person 

class person():
    
    
    #define the constructor
    def __init__(self,Name=None,person_id=None,want_accomodation=None):
        self.Name=Name
        self.person_id=person_id
        self.want_accomodation=want_accomodation
        self.role=None
        
    
    #create the add persons method
    def add_person(self,occupant):
        name=self.Name
        id=self.person_id
        accomodation=self.want_accomodation
        occupant.append(name)
        occupant.append(id)
        occupant.append(accomodation)
        return occupant
    #create the remove person method
    def remove_person(self,occupant):
        self.occupant.clear()
        return occupant

#create the staff with person  as its parent class

class staff(person):
    #this
    def __init__(self,Name=None,person_id=None,want_accomodation=None):
        super().__init__(Name,person_id)
        self.want_accomodation='N'
        self.role='Staff'

#create class fellow with person as its parent class

class fellow(person):
    def __init__(self,Name=None,person_id=None,want_accomodation=None):
        super().__init__(Name,person_id)
        self.want_accomodation='Y'
        self.role='Fellow'

#create super class room


class room():
    
    
    #define the constructor
    def __init__(self,Name=None,max_capacity=None,purpose=None,occupant=None):
        self.Name=Name
        self.max_capacity=max_capacity
        self.purpose=purpose
        self.occupant=occupant
    def add_occupant(self):
        pass
    def remove_occupant(self):
        pass
class LivingRoom(room):
    def __init__(self,Name=None,max_capacity=None,purpose=None,occupant=None):
        super().__init__(Name,occupant)
        self.purpose='livingroom'
        self.max_capacity=4
class Office(room):
    def __init__(self,Name=None,max_capacity=None,purpose=None,occupant=None):
        super().__init__(Name,occupant)
        self.purpose='Office '
        self.max_capacity=6

