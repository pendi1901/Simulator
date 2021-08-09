def isLabel(instn):
	#label validation
	#return boolean

#addr_and_pc is a list
#addr_and_pc[0] -> mem_addr
#addr_and_pc[1] -> pc

#Return incremented mem_addr if respective validations are correct 
def label(instn, labels, addr_and_pc):
	if isLabel(instn):
		
		#TRUE: append to label dict  (format -> label: addr)
	else:
		#FALSE: error

def isVar(instn):
	#variable validation
	#return boolean

def variable(instn, vars):
	if isVar(instn)
		#TRUE: append to variable dict 	(format -> var: addr)
	else:
		#FALSE: throw error
