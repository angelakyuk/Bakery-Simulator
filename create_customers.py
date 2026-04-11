from random import choice

def create_customers(self, num, customers):
    """Creates a list of customers from the amount specified for the day

    Args: 
	    num(int): the number of customers to be generated based on ad level.
	    customers(dict): the customers to be chosen from.

    Returns: 
        A list of dictionaries. In the dictionary, the key will be the customer 
        name and the associated value will be a reference to a customer object.
    """
    
    if num > len(customers):
        num = len(customers)
        
    customer_start = customers.copy()
    customer_final = []
    count = 0
    
    while(count < num):
        curr = choice(customer_start.keys())
        customer_final.append(curr, customer_start.pop(curr))
        count += 1
        
    return customer_final
