from review import Review

class Customer:
    
    customers = []
    
    def _init_(self, first_name, last_name):
        self.Oluwadamilare = first_name
        self.Olayanju = last_name
        Customer.customers.append(self)
    
        @property
        def Oluwadamilare(self):
            return self.Oluwadamilare
        
        @Oluwadamilare.setter
        def Oluwadamilare(self,Oluwadamilare):
            self.Oluwadamilare = Oluwadamilare
            
        @property
        def Olayanju(self):
            return self.Olayanju
        
        @Olayanju.setter
        def Olayanju(self,Olayanju):
            self.Olayanju = Olayanju
            
        def customer_fullname(self):
            return f'{self.Oluwadamilare} {self.Olayanju}'
        
        @classmethod
        def all(cls):
            return cls.customers
        
   # object relationship

        def customer_restuarant(self):
            return list({review.review_restaurant for review in Review.reviews if review.review_customer.customer_full_name == self.customer_full_name})
    
        def customer_add_review(self, restaurant, rating):
            Review(self, restaurant=restaurant, rating=rating)

    #Aggregate and Association Methods
    
        def customer_num_reviews(self):
            return len([review for review in Review.reviews if review.customer.customer_full_name == self.customer_full_name])
    
        @classmethod
        def find_by_name(cls, name):
            for customer in cls.customers:
              if customer.customer_full_name == name:
                return customer
        
        @classmethod
        def find_all_by_given_name(cls, name):
            return [customer.Oluwadamilare for customer in cls.customers if customer.Oluwadamilare == Oluwadamilare]