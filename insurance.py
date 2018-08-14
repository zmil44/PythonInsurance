"""
Zach Miller
9/16/2103
How Much Insurance program
"""

def main():
    replacementCost=float(input("Please enter the replacement cost: "))
    percentInsured=(.8)
    minimumInsurance=(replacementCost*percentInsured)
    printStatement(replacementCost,percentInsured,minimumInsurance)
    
def printStatement(replacement,percent,insurance):
  
    print('Replacement cost: ',format(replacement, ',.2f'))
    print('Percent Insured: ',format(percent,'.1%'))
    print('Minimum insurance: ',format(insurance, ',.2f'))

#call main function
main()
