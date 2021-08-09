#Parameters:
#instn - input instruction
#machine_code- list to store resultant machine code

#**IMPORTANT***
#addr_and_pc is a list
#addr_and_pc[0] -> mem_addr
#addr_and_pc[1] -> pc


def isRegister(instn):
	#register validation and return boolean
	#create register dict

def isMem(instn):
	#memory validation and return boolean

def isImm(instn):
	#immediate validation and return boolean

def isHalt(instn):
	#halt instruction validation and return boolean


def get_opcode(command):
	#create dict , format -> {instn: opcode}
	#return corresponding opcode
	opcode = {"add": 0000, .....}
	return str(opcode[command])


def get_regAddr():
	#create reg dict, format -> {reg: reg_Addr}
	#return corresponding reg addr



#---IMPORTANT----
#Return incremented mem_addr and machine code if respective validations are correct.

def typeA(instn, machine_code, addr_and_pc):
	if isRegister(instn):
		#TRUE: call correponding function
		op = get_opcode(instn[0]);
		machine_code.append(op+ 3 registers addr)
		#FALSE: error

def typeB(instn, machine_code, addr_and_pc):
	if isRegister(instn):

	if isImm(instn):
		#TRUE: call correponding function
		#FALSE: error

def typeC(instn, machine_code, addr_and_pc):
	if isRegister(instn):
		#TRUE: call correponding function
		#FALSE: error

def typeD(instn, machine_code, addr_and_pc):
	if isRegister(instn):

	if isMem(instn):
		#TRUE: call correponding function
		#FALSE: error

def typeE(instn, machine_code, addr_and_pc):
	if isMem(instn):
		#TRUE: call correponding function
		#FALSE: error

def typeF(instn, machine_code, addr_and_pc):
	if isHalt(instn)
		#TRUE: call correponding function
		#FALSE: error

def instruction(instn, machine_code, addr_and_pc):
	#like A -> all type A instructions -> "add", "sub", "mul" etc.
	instn_type = { A: [instn of A ], B: [instn of B] , so on}
	for i in instn_type:
		if instn[0] in instn_type[A]:  typeA(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type[B]:  typeB(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type[C]:  typeC(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type[D]:  typeD(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type[E]:  typeE(instn, machine_code, addr_and_pc)
		else typeF(instn, machine_code, addr_and_pc)