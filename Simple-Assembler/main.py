import labelVar
import instruction


def read_from_file():
	#read data from stdin and return file object

def isInstruction(instn):
	# intruction validation

def isBlankLine(line):
	#check for blank line and return boolean


def main():
	prog_cnter = 0
	mem_addr = 0
	hlt_count= 0

	addr_and_pc = [ mem_addr, prog_cnter]
	storeLabel = {}
	storeVar = {}
	machine_code = []

	f = read_from_file()
	for each in f:
		line = each.strip().split()

		if isBlankLine(line):
			continue

		elif line[0] == "label":
			mem_addr = label(line, storeLabel, addr_and_pc)

		elif line[0] == "var":
			variable(line, storeVar)

		elif isInstruction(line[0]):
			mem_addr = intruction(line, machine_code, addr_and_pc)

			#<<check here for multiple hlts>> and display error

		else:
			# error(general error perhaps) statement
		prog_cnter += 1

	# <<modify var dict (add mem_addr after hlt instruction)>>

	#displaying final result
	for result in machine_code:
		print(result)

if __name__ == '__main__':
	main()