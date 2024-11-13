This is a reverse engineering challenge where u are given a exe file 

it is structured in a way that if you give "cyberyeti" in the input field u get 
returned with you win and if u give something else it will be returned with you 
lose 


now the challenge is to reverse engineer the file to change the file format
so tht if we give any string in the input field it should give you win 



using ida we  changed the jnz section which basically detects if the text is correct
or wrong 


jnz is jump if not 

we have to convert the jnz to jz 

go to hex dump > change the bits of jnz to jz then patch the file and run it 



