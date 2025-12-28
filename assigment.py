'''
BU24SEN1069
NAME - Ogunmokun Oluwadamilare Ayomide
program - software engineering
COS ASSIGNMENT
'''

def run():
    print("Filing Status: \n 0 - Single filers \n 1 - married filing jointly or qualified widower \n 2 - married filing separately \n 3 - head of household ")

    userInput1 = int(input("Enter Filing Status: "))
    
    match userInput1:
        case 0:
            SingleInput = int(input("Enter Taxable Income: "))
            if SingleInput <= 8350:
                Tax1 = 0.1 * SingleInput
                print(f"so Taxable Income is ${Tax1}")
            elif SingleInput <= 33950: #15% single
                SingletaxableIncome15 = (0.1 * 8350) + 0.15 * (SingleInput - 8350)
                print(f"so Taxable Income is ${SingletaxableIncome15}")
            elif SingleInput <= 82250: #25% single
                SingletaxableIncome25 = (0.15 * 33950) + 0.25 * (SingleInput - 33950)
                print(f"so Taxable Income is ${SingletaxableIncome25}")  
            elif SingleInput <= 171550: #28% single
                SingletaxableIncome28 = (0.25 * 82250) + 0.28 * (SingleInput - 82250)
                print(f"so Taxable Income is ${SingletaxableIncome28}")
            elif SingleInput <= 372950: #33% single
                SingletaxableIncome33 = (0.28 * 171550) + 0.33 * (SingleInput - 171550)
                print(f"so Taxable Income is ${SingletaxableIncome33}")                                                            
            else:
                SingletaxableIncome35 = (0.33 * 372950) + 0.35 * (SingleInput - 372950) #35% single
                print(f"so Taxable Income is ${SingletaxableIncome35}")
        case 1:
            MarriedFilingJointly_Input = int(input("Enter Taxable Income: "))
            if MarriedFilingJointly_Input <= 16700:
                Tax2 = 0.1 * MarriedFilingJointly_Input
                print(f"so Taxable Income is ${Tax2}")
            elif MarriedFilingJointly_Input <= 67900: #15% single
                MarriedtaxableIncome15 = (0.1 * 16700) + 0.15 * (MarriedFilingJointly_Input - 16700)
                print(f"so Taxable Income is ${MarriedtaxableIncome15}")
            elif MarriedFilingJointly_Input <= 137050: #25% single
                MarriedtaxableIncome25 = (0.15 * 67900) + 0.25 * (MarriedFilingJointly_Input - 67900)
                print(f"so Taxable Income is ${MarriedtaxableIncome25}")
            elif MarriedFilingJointly_Input <= 208850: #28% single
                MarriedtaxableIncome28 = (0.25 * 137050) + 0.28 * (MarriedFilingJointly_Input - 137050)
                print(f"so Taxable Income is ${MarriedtaxableIncome28}")
            elif  MarriedFilingJointly_Input <= 372950: #33% single
                MarriedtaxableIncome33 = (0.28 * 208850) + 0.33 * (MarriedFilingJointly_Input - 208850)
                print(f"so Taxable Income is ${MarriedtaxableIncome33}")
            else:
                MarriedtaxableIncome35 = (0.33 * 372950) + 0.35 * (MarriedFilingJointly_Input - 372950) #35% single 
                print(f"so Taxable Income is ${MarriedtaxableIncome35}")
        case 2:
            MFS_Input = int(input("Enter Taxable Income: "))
            if MFS_Input <= 8350:
                Tax3 = 0.1 * MFS_Input 
                print(f"so Taxable Income is ${Tax3}")   
            elif  MFS_Input <= 33950: #15% single
                MFS_taxableIncome15 = (0.1 * 8350) + 0.15 * (MFS_Input - 8350)
                print(f"so Taxable Income is ${MFS_taxableIncome15}")  
            elif  MFS_Input <= 68525: #25% single
                MFS_taxableIncome25 = (0.15 * 33950) + 0.25 * (MFS_Input - 33950)
                print(f"so Taxable Income is ${MFS_taxableIncome25}")
            elif  MFS_Input <= 104425: #28% single
                MFS_taxableIncome28 = (0.25 * 68525) + 0.28 * (MFS_Input - 68525)
                print(f"so Taxable Income is ${MFS_taxableIncome28}")
            elif  MFS_Input <= 186475: #33% single
                MFS_taxableIncome33 = (0.28 * 104425) + 0.33 * (MFS_Input - 104425)
                print(f"so Taxable Income is ${MFS_taxableIncome33}")
            else:
                MFS_taxableIncome35 = (0.33 * 186475) + 0.35 * (MFS_Input - 186475) #35% single 
                print(f"so Taxable Income is ${MFS_taxableIncome35}") 
        case 3:
            HOH_input = int(input("Enter Taxable Income as Head of household: "))
            if HOH_input <= 11950:
                Tax4 = 0.1 * HOH_input 
                print(f"so Taxable Income is ${Tax4}")
            elif  HOH_input <= 45500: #15% single
                HOH_taxableIncome15 = (0.1 * 11950) + 0.15 * (HOH_input - 11950)
                print(f"so Taxable Income is ${HOH_taxableIncome15}")
            elif  HOH_input <= 117450: #25% single
                HOH_taxableIncome25 = (0.15 * 45500) + 0.25 * (HOH_input - 45500)
                print(f"so Taxable Income is ${HOH_taxableIncome25}")
            elif HOH_input <= 190200: #28% single
                HOH_taxableIncome28 = (0.25 * 117450) + 0.28 * (HOH_input - 117450)
                print(f"so Taxable Income is ${HOH_taxableIncome28}")  
            elif HOH_input <= 372950: #33% single
                HOH_taxableIncome33 = (0.28 * 190200) + 0.33 * (HOH_input - 190200)
                print(f"so Taxable Income is ${HOH_taxableIncome33}")
            else:
                HOH_taxableIncome35 = (0.33 * 372950) + 0.35 * (HOH_input - 372950) #35% single
                print(f"so Taxable Income is ${ HOH_taxableIncome35}")                
                                                                                                                                             
run()    