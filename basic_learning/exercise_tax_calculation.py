# Excercise 1 : calculate tax based on state with common professional tax of 10%

def calculate_tax(state , gross):
    # reduce common tax slab -10%
    professional_tax = gross*10/100
    # State wise tax slab in dictionary
    state_tax_slab={'London':50,'Manchester':10,'Leeds':20,'Scotland':30}
    if state in state_tax_slab:
        state_tax=gross*state_tax_slab[state]/100
        net_income = gross - professional_tax-state_tax
        print("Tax % for " + state+ " is "+str(state_tax_slab[state])+"% and income after deduction is "+str(net_income))
    else:
        print("Your state not in tax slab list")

calculate_tax("Leeds",10000)



