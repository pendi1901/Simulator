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
	if instn[0] in opcode:
		return True
	else:
		False

def isBlankLine(line):
	#check for blank line and return boolean
    if line == '':
		return True
	else:
		return False


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
	machine_code = []
	storereg = ["R0", "R1", "R2", "R3", "R4", "R5", "R6", "FLAGS"]
	#mem_ins = {}

	#add a case for the movI and the movR as well otherwise they'll
	#come under errors 
	#f = read_from_file()
	for each in stdin:
		line = each[:-1].strip().split()

		if isBlankLine(line):
			prog_cnter = prog_cnter + 1
			continue

		elif hlt_count == 1:
			raise Exception(prog_cnter - 1, "halt not the last instruction")

		elif line[0][-1] == ":":
			labelVar.label(line, storeLabel, storereg, storeVar, opcode, addr_and_pc)
			mem_addr = addr_and_pc[0]
			if len(line) == 2:
				if line[1] == "hlt":
					hlt_count = 1
		elif line[0] == "var":
			if len(line) != 2:
				raise Exception("syntax")
			if mem_addr != -1:
				raise Exception("variable dec in between")
			labelVar.variable(line, storeVar, storereg, opcode)
		elif line[0] == "hlt":
			if len(line) == 1:
				hlt_count = 1
				mem_addr += 1
		else:
			mem_addr += 1
		prog_cnter += 1

	for v in storeVar.keys():
		mem_addr += 1
		memad = bin(mem_addr)[2:].zfill(8)
		storeVar[v] = memad

	prog_cnter = 1
	mem_addr = -1

	for each in stdin:
		line = each[:-1].strip().split()

		if isBlankLine(line):
			prog_cnter = prog_cnter + 1
			continue

		elif hlt_count == 1:
			raise Exception("halt not the last instruction")

		elif line[0][-1] == ":":
			labelVar.label(line, storeLabel, storereg, storeVar, opcode, addr_and_pc)
			if len(line) == 1:
				continue
			if isInstruction(line[1:]):
				instruction.itr(line, machine_code, addr_and_pc, storeLabel, storeVar)
			else:
				raise Exception("Wrong instruction")

		elif line[0] == "var":
			prog_cnter += 1
			continue

		elif isInstruction(line[0]):
			instruction.itr(line, machine_code, addr_and_pc, storeLabel, storeVar)
		else:
			# error(general error perhaps) statement
		    raise Exception("General Error")
		prog_cnter += 1
	if hlt_count == 0:
		raise Exception("Halt statement missing")
	# <<modify var dict (add mem_addr after hlt instruction)>>

	#for z in mem_ins.keys():
		#intruction(mem_ins[z], machine_code, z, storeVar, storeLabel)
	#displaying final result
	for result in machine_code:
		print(result)

if __name__ == '__main__':
	main()