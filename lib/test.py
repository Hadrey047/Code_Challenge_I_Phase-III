

from customer import Customer
from review import Review
from restaurant import Restaurant

# Creating Instances for restaurant  and review
restaurant1 = Restaurant("Royal Cubanna")
restaurant2 = Restaurant("Pinnacle Cool Spot")

review1 = Review("Customer John", " Royal Cubanna", 2)
review2 = Review("Customer Dami", "Pinnacle Cool Spot", 4)
review3 = Review("Customer Bola", "Louge Restaurant", 7)


# Test the methods of the Restaurant class
print(restaurant1.name())
print(restaurant1.reviews())
print(restaurant1.customers())
print(restaurant1.average_star_rating())

print(restaurant2.name())
print(restaurant2.reviews())
print(restaurant2.customers())
print(restaurant2.average_star_rating())

# Creating instances for Customer
customer1 = Customer("Tolu", "Oladiti")
customer2 = Customer("Gbenga", "Ogunsade")

# Creating instances for Review
review1 = Review(customer1, "Threshing House", 1)
review2 = Review(customer2, " Baba Loja", 5)

# Add reviews for customers
customer1.add_review("Bank Capricon ", 3)
customer2.add_review("Fish Restaurant ", 2)

# Get all customers
all_customers = Customer.all()
print("All Customers:")
for customer in all_customers:
    print(customer.full_name())

# find all reviewed restaurants for a customer
customer1_restaurants = customer1.restaurants()
print("Customer 1 Reviewed Restaurants:")
for restaurant in customer1_restaurants:
    print(restaurant)

# find the number of reviews for a customer
customer2_num_reviews = customer2.num_reviews()
print("Customer 2 Number of Reviews:", customer2_num_reviews)

# Find customer by name
customer_found = Customer.find_by_name("")
if customer_found:
    print("Customer Found:", customer_found.full_name())
else:
    print("Customer Not Found")

# Search all the customers by given name
customers_with_given_name = Customer.find_all_by_given_name("")
print("Customers with Given Name 'Esther Ade':")
for customer in customers_with_given_name:
    print(customer.full_name())

# Get all review
all_reviews = Review.all()

print("All Reviews:")

for review in all_reviews:
    if isinstance(review.customer, Customer):
        print("Customer:", review.customer.full_name(), "| Restaurant:", review.restaurant, "| Rating:",review.rating)