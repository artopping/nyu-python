x = (raw_input("would you like to convert fahrenheit(f) or celsius(c)? "))
if x == "f":
    y = (raw_input("what is the fahrenheit?"))
    f = (int(y) - 32) * 5.0 / 9
    print ("and in celsius, that is: "),
    print (f)
elif x == "c":
    y = (raw_input("what is the celsius?"))
    f = (int(y) *9) / 5.0 + 32
    print ("and in fahrenheit, that is: "),
    print (f)
    else:
        print ("Error) 
