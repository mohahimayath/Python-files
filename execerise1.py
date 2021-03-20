#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    rate_per_adult = 37550.0
    rate_per_child = (1/3)*rate_per_adult
    service_tax = 7/100
    discount = 10/100
    #Write your logic here
    cost_of_adult = no_of_adults*rate_per_adult
    cost_of_child = no_of_children*rate_per_child
    ticket_cost = cost_of_adult+cost_of_child
    ticket_cost = (discount * ticket_cost) - ticket_cost 
    total_ticket_cost = (service_tax*ticket_cost) + ticket_cost
    return abs(total_ticket_cost)


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)