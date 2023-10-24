

class Magazine:
    all_magazines = []
    
    
    def __init__(self,name,category):
        self.name = name 
        self.category = category 
        Magazine.all_magazines.append(self)
        
    def magazine(self):
        return self.name
    
    def magazine_category(self):
        return self.category
    
    @classmethod
    def magazine_all(cls):
       return cls.all_magazines
        
    pass
    
s2 = Magazine("Punch","Print Media")

print(s2.magazine_all())
        
        