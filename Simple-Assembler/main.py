import labelVar
import instruction
from sys import stdin


#def read_from_file():
	#read data from stdin and return file object
 #   comp_input = sys.stdin.read()
#	return comp_input

def isInstruction(instn):
	# intruction validation
	opcode = ["add", "sub", "mov","ld", "st", "mul", "div",
	"rs","ls","xor" ,"or" ,"and", "not","cmp", "jmp", "jlt", "jgt", "je"
	, "hlt"]
	return instn in opcode

def isBlankLine(line):

	return line == ""


def main():
	prog_cnter = 1
	mem_addr = -1
	hlt_count= 0
	opcode = ["add", "sub", "mov", "ld", "st", "mul", "div",
		  "rs", "ls", "xor", "or", "and", "not", "cmp", "jmp", "jlt", "jgt", "je"
	       , "hlt"]
	addr_and_pc = [ mem_addr, prog_cnter, hlt_count]
	storeLabel = {}
	storeVar = {}
	input_list = []
	machine_code = []
	storereg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS"]
	mem_ins = {}

	# add a case for the movI and the movR as well otherwise they'll
	# come under errors 
	# f = read_from_file()
	for each in stdin:
		line = each.strip().split()

		if isBlankLine(line):
			addr_and_pc[1] = addr_and_pc[1] + 1
			continue

		input_list.append(line)
		if addr_and_pc[2] == 1:
			raise Exception(addr_and_pc[1] - 1, "halt not the last instruction")

		elif line[0][-1] == ":":
			labelVar.label(line, storeLabel, storereg, storeVar, opcode, addr_and_pc)
			if len(line) == 1:
				addr_and_pc[1] += 1
				addr_and_pc[0] -= 1
				continue
			if line[1] == 'hlt':
				if len(line) == 2:
					addr_and_pc[2] = 1
				else:
					raise Exception("Syntax Error at line number", addr_and_pc[1])

		elif line[0] == "var":
			if len(line) != 2:
				raise Exception("syntax")
			if addr_and_pc[0] != -1:
				raise Exception("variable dec in between")
			labelVar.variable(line, storeVar, storereg, opcode)
		
		elif line[0] == "hlt":
			if len(line) == 1:
				addr_and_pc[2] = 1
				# addr_and_pc[0] += 1
				addr_and_pc[0] += 1
			else:
				raise Exception("Syntax Error at line number", addr_and_pc[1])
		
		else:
			addr_and_pc[0] += 1
			# addr_and_pc[0] += 1 
		addr_and_pc[1] += 1
	if addr_and_pc[2] == 0:
		raise Exception("Halt statement missing")

	for v in storeVar.keys():
		addr_and_pc[0] += 1
		memad = bin(addr_and_pc[0])[2:].zfill(8)
		storeVar[v] = memad

	addr_and_pc[1] = 1
	addr_and_pc[0] = -1
	# addr_and_pc[2] = 0

	# for each in input_list:
	for line in input_list:
	# for each in stdin:
		# # line = each.strip().split()
		# # print(each)

		# # if isBlankLine(line):
		# if each == "\n":
		# 	addr_and_pc[1] = addr_and_pc[1] + 1
		# 	continue

		# line = each.strip().split()
		# if isBlankLine(line):
		# if isBlankLine(line):
		# 	addr_and_pc[1] = addr_and_pc[1] + 1
		# 	continue
		# print(line)


		# if addr_and_pc[2] == 1:
		# 	raise Exception("halt not the last instruction")

		if line[0][-1] == ":":
			if len(line) == 1:
				addr_and_pc[1] += 1
				continue
			if isInstruction(line[1]):
				instruction.itr(line[1:], machine_code, addr_and_pc, storeLabel, storeVar)
				# addr_and_pc[0] = addr_and_pc[0]
				# addr_and_pc[2] = addr_and_pc[2]
			else:
				raise Exception("Wrong instruction")

		elif line[0] == "var":
			addr_and_pc[1] += 1
			continue

		elif isInstruction(line[0]):
			instruction.itr(line, machine_code, addr_and_pc, storeLabel, storeVar)
			# addr_and_pc[0] = addr_and_pc[0]
			# addr_and_pc[2] = addr_and_pc[2]
		else:
			# error(general error perhaps) statement
		    raise Exception("General Error")
		addr_and_pc[1] += 1

	# <<modify var dict (add addr_and_pc[0] after hlt instruction)>>

	#for z in mem_ins.keys():
		#intruction(mem_ins[z], machine_code, z, storeVar, storeLabel)
	#displaying final result
	for result in machine_code:
		print(result)

if __name__ == '__main__':
	main()