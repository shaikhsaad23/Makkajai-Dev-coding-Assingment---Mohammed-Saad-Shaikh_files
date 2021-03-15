input1=list(map(str,input('Input Quantity, Item and price:').split()))


quantity=int(input1[0])


item=''.join(input1[1:-2])


price=float(input1[-1])



taxExempt={"book","Chochlate_Bar","Headache_pills"}



basicTax={"music_CD","Bottle_of_perfume"}



importedTax={"box_of_imported_Chochlate"}



bothTax={"Imported_bottle_of_perfume"}



if item in taxExempt:
    
    print("Output:")
    
    print(quantity, item, price)
    


elif item in basicTax:
    
    salesTax=quantity*10*price/100

    taxprice=price+salesTax

    print("Output:")

    print(quantity, item, taxprice)

    print("salesTax:",salesTax)

    print("Total:" , taxprice+salesTax)

    

elif item in importedTax:

    salesTax=quantity*5*(price/100)

    taxprice=price+salesTax

    print("Output:")

    print("salesTax:",salesTax)

    print("Total:" , taxprice+salesTax)



elif item in bothTax:

    salesTax=quantity*15*(price/100)

    taxprice=price+salesTax

    print("Output:")

    print(quantity, item, taxprice)

    print("salesTax:",salesTax)

    print("Total:" , taxprice+salesTax)
  




  
    
    
    
    