print('Welcome')
lan=input('enter any language--')
if lan=='hindi':
		print('aapne hindi select kiya')
		pas=int(input('enter any pass--'))
		if pas==1384:
			print('select withdraw or check balance')
			money=input('withdraw or check balance')
			if money=='check balance':
				print('10000')
				print('Welcome for using this atm')
			elif money=='withdraw':
				cash=int(input('enter any number'))
				if money<='withdraw':
					print(10000-cash)
					print('Welcome for using this atm') 	
				
		elif pas!=1384:
			print('incorrect password')
    
	
elif lan=='english':
			print('you are selected english language')
			pas=int(input('enter any pass--'))
			if pas==1384:
				print('select withdraw or check balance')
				money=input('withdraw or check balance')
				if money=='check balance':
					print('10000')
					print('Welcome for using this atm')
				elif money=='withdraw':
					cash=int(input('enter any number'))
					if money<='withdraw':
						print(10000-cash)
						print('Welcome for using this atm') 	
					
			elif pas!=1384:
				print('incorrect password')
			
else:
	print("aapki language wrong hai")