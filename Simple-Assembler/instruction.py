#Parameters:
#instn - input instruction
#machine_code- list to store resultant machine code

#**IMPORTANT***
#addr_and_pc is a list
#addr_and_pc[0] -> mem_addr
#addr_and_pc[1] -> pc

def isImm(instn):
	#immediate validation and return boolean
	return int(instn) < 256

def isHalt(instn):
	return len(instn) == 1

def get_opcode(command):
	#create dict , format -> {instn: opcode}
	#return corresponding opcode
	opcode = {"add": "00000", "sub" : "00001" , "movI" : "00010" , "movR" : "00011",
	"ld" : "00100" , "st" : "00101" , "mul": "00110" , "div" : "00111" ,
	"rs" : "01000" , "ls" : "01001" , "xor":"01010" ,"or" : "01011" ,
	"and" : "01100", "not" : "01101" ,"cmp" : "01110", "jmp":"01111" , 
	"jlt" : "10000" , "jgt": "10001" , "je" : "10010" , "hlt" : "10011"}
	return str(opcode[command])

#the exception here is left 
def get_regAddr(reg1, line_no):
	#create reg dict, format -> {reg: reg_Addr}
	#return corresponding reg addr
	regdict = {"R0" : "000" , "R1" : "001" , "R2" : "010" , "R3" : "011" ,
	 			"R4" : "100", "R5" : "101" , "R6" : "110"}
	if reg1 == "FLAGS":
		raise Exception("Illegal use of FLAGS at line number", line_no)
	if(reg1 in regdict):
		return str(regdict[reg1])
	else : 
		raise Exception("Error : Register Not Found","At Line number: ", line_no)

def get_regAddrfl(reg1, line_no):
	#create reg dict, format -> {reg: reg_Addr}
	#return corresponding reg addr
	regdict = {"R0" : "000" , "R1" : "001" , "R2" : "010" , "R3" : "011" ,
	 			"R4" : "100", "R5" : "101" , "R6" : "110" , "FLAGS" : "111"}
	if(reg1 in regdict):
		return str(regdict[reg1])
	else :
		raise Exception("Error : Register Not Found","At Line number: ", line_no)

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
		rd = get_regAddr(instn[1], addr_and_pc[1])
		rs1 = get_regAddr(instn[2], addr_and_pc[1])
		rs2 = get_regAddr(instn[3], addr_and_pc[1])
		opcode = get_opcode(instn[0])
		unused = "00"
		machine_code.append(opcode + unused + rd + rs1 + rs2 )
		addr_and_pc[0] += 1
	else:
		raise Exception("Error : Not Enough Arguments","At line number", addr_and_pc[1])
		

		

def typeB(instn, machine_code, addr_and_pc):
	if(len(instn) == 3):
		if(isImm(instn[2][1:])):
			rd = get_regAddr(instn[1], addr_and_pc[1])
			opcode = get_opcode(instn[0])
			i = int(instn[2][1:])
			binary = bin(i)[2:]
			imm = binary.zfill(8)
			machine_code.append(opcode + rd + imm)
			addr_and_pc[0] += 1
			
		else : 
			raise Exception("Error  : Given Number isn't a 8 bit value","At line number",addr_and_pc[1])
	else:
		raise Exception("Error : Not Enough Arguments","At line number",addr_and_pc[1] )


	#TRUE: call correponding function
	#FALSE: error

def typeC(instn, machine_code, addr_and_pc):
	if(len(instn) == 3):
		if instn[0] == "movR":
			rd = get_regAddr(instn[1], addr_and_pc[1])
			rs = get_regAddrfl(instn[2], addr_and_pc[1])
		else:
			rd = get_regAddr(instn[1], addr_and_pc[1])
			rs = get_regAddr(instn[2], addr_and_pc[1])
		opcode = get_opcode(instn[0])
		unused = "00000"
		machine_code.append(opcode + unused + rd + rs)
		addr_and_pc[0] += 1
	else:
		raise Exception("Error : Not Enough Arguments","At line number", addr_and_pc[1])


#complete this function
def typeD(instn, machine_code, addr_and_pc, vars):
	if (len(instn) ==3):
		a = get_regAddr(instn[1], addr_and_pc[1])
		op = get_opcode(instn[0])
		try:
			memad = vars[instn[2]]
		except:
			raise Exception("Variable not declared")
		machine_code.append(op + a + memad)
		addr_and_pc[0] += 1
	else:
		raise Exception("Syntax")

		#TRUE: call correponding function
		#FALSE: error

#complete this function
def typeE(instn, machine_code, addr_and_pc, labels):
	if(len(instn)==2):
		op = get_opcode(instn[0])
		redundant = "000"
		try:
			memad = labels[instn[1]]
		except:
			raise Exception("Invalid label")
		machine_code.append(op + redundant + memad)
		addr_and_pc[0] += 1
	else:
		raise Exception("Syntax")



		#TRUE: call correponding function
		#FALSE: error

#complete this function to check the if halt is the last statement
def typeF(instn, machine_code, addr_and_pc):
	# no point checking this. Checked in main itself
	#a = isHalt(instn[0])
	if(isHalt(instn)):
		# not returning val of hlt_count, so cannot keep track
		opcode =get_opcode(instn[0])
		unused = "00000000000"
		machine_code.append(opcode + unused)
		addr_and_pc[0] += 1
		addr_and_pc[2] = 1
	else:	
		raise Exception("Syntax")

				
			

	#TRUE: call correponding function
	#FALSE: error

def itr(instn, machine_code, addr_and_pc, labels, vars):
	#like A -> all type A instructions -> "add", "sub", "mul" etc.
	if instn[0] == "mov":
		try:
			index = instn[2].find('$')
		except:
			raise Exception("Syntax")
		if(index == 0):
			instn[0] = "movI"
		else:
			instn[0] = "movR"

	instn_type = { "A": ["add" , "sub" , "mul" , "xor" , "or" , "and" ],
				   "B" : ["movI" , "rs","ls"], 
				   "C" : ["movR", "div" ,"not" , "cmp"] , 
				   "D" : ["ld" , "st"],
				   "E" : ["jmp" , "jlp" , "jgt" , "je"] ,
				   "F" :["hlt"]
				 }
	#for i in instn_type:
	if instn[0] in instn_type["A"]:
		typeA(instn, machine_code, addr_and_pc)
	elif instn[0] in instn_type["B"]:
		typeB(instn, machine_code, addr_and_pc)
	elif instn[0] in instn_type["C"]:
		typeC(instn, machine_code, addr_and_pc)
	elif instn[0] in instn_type["D"]:
		typeD(instn, machine_code, addr_and_pc, vars)
	elif instn[0] in instn_type["E"]:
		typeE(instn, machine_code, addr_and_pc, labels)
	else:
		typeF(instn, machine_code, addr_and_pc)
	#return mem_addr, machine_code
		