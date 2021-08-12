def isLabel(instn, labels, reg, var, opc):
	if instn[0][:-1] in var or instn[0][:-1] in reg or instn[0][:-1] in opc or instn[0][:-1] in labels:
		return False
	for i in instn[0][:-1]:
		if i.lower() not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
							 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
							 'z']:
			return False
	j = 0
	for i in instn[0][:-1]:
		if i.isalpha():
			j += 1
			break
	if(j == 0):
		return False
	return True

#Return incremented mem_addr if respective validations are correct 
def label(instn, labels, reg, var, opc, addr):
	if isLabel(instn, labels, reg, var, opc):
		addr[0] += 1
		a = bin(addr[0])[2:].zfill(8)
		labels[instn[0][:-1]] = a
	else:
		#FALSE: error
		raise Exception("Label name incorrect")

def isVar(instn, var, reg, opcode):
	#variable validation
	#return boolean
	if instn[1] in var or instn[1] in reg or instn[1] in opcode:
		return False
	for i in instn[1]:
		if i.lower() not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '_', 'a', 'b', 'c', 'd', 'e', 'f', 'g',
							 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
							 'z']:
			return False
	j = 0
	for i in instn[1]:
		if i.isalpha():
			j += 1
			break
	if(j == 0):
		return False
	return True


def variable(instn, var, reg, opcode):
	if isVar(instn, var, reg, opcode):
		#TRUE: append to variable dict 	(format -> var: addr)
	    var[instn[1]] = "00000000"
	else:
		raise Exception("variable name incorrect")
