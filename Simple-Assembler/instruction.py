#Parameters:
#instn - input instruction
#machine_code- list to store resultant machine code

#**IMPORTANT***
#addr_and_pc is a list
#addr_and_pc[0] -> mem_addr
#addr_and_pc[1] -> pc


# def isRegister(instn):
# 	#register validation and return boolean
# 	#create register dict

def isMem(instn):
	#memory validation and return boolean

def isImm(instn):
	#immediate validation and return boolean

def isHalt(instn):
	#halt instruction validation and return boolean


def get_opcode(command):
	#create dict , format -> {instn: opcode}
	#return corresponding opcode
	opcode = {"add": "00000", "sub" : "00001" , "movI" : "00010" , "movR" : "00011",
	"ld" : "00100" , "st" : "00101" , "mul": "00110" , "div" : "00111" ,
	"rs" : "01000" , "ls" : "01001" , "xor":"01010" ,"or" : "01011" ,
	"and" : "01100", "not" : "01101" ,"cmp" : "01110", "jmp":"01111" , 
	"jlt" : "10000" , "jgt": "10001" , "je" : "10010" , "hlt" : "10011"}
	return str(opcode[command])


def get_regAddr(reg1):
	#create reg dict, format -> {reg: reg_Addr}
	#return corresponding reg addr
	regdict = {"R0" : "000" , "R1" : "001" , "R2" : "010" , "R3" : "011" , "R4" : "100",
	"R5" : "101" , "R6" : "110" , "FLAGS" : "111"}



#---IMPORTANT----
#Return incremented mem_addr and machine code if respective validations are correct.

def typeA(instn, machine_code, addr_and_pc):
	# if get_regAddr(instn):
	# 	#TRUE: call correponding function
	# 	op = get_opcode(instn[0])
	# 	redudant = "00"

	# 	machine_code.append(op+redudant + )
	# 	#FALSE: error
	if(len(instn) == 4):
		

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
	if isHalt(instn):
		#TRUE: call correponding function
		#FALSE: error

def instruction(instn, machine_code, addr_and_pc):
	#like A -> all type A instructions -> "add", "sub", "mul" etc.
	index = instn[2].find('$')
	if(index == 0):
		instn[0] = "movI"
	else:
		instn[0]="movR"
	instn_type = { "A": ["add" , "sub" , "mul" , "xor" , "or" , "and" ],
	"B" : ["movI" , "rs","ls"], "C" : ["movR", "div" ,"not" , "cmp"] , "D" : ["ld" , "st"],
	"E" : ["jmp" , "jlp" , "jgt" , "je"] , "F" :["hlt"]}
	for i in instn_type:
		if instn[0] in instn_type["A"]:  typeA(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type["B"]:  typeB(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type["C"]:  typeC(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type["D"]:  typeD(instn, machine_code, addr_and_pc)
		elif instn[0] in instn_type["E"]:  typeE(instn, machine_code, addr_and_pc)
		else :  typeF(instn, machine_code, addr_and_pc)