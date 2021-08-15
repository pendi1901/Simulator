import Execution_Engine
from sys import stdin

def memory_initialisation(mem):
    for inst in stdin:
        line = inst.strip().split()
        if len(line) == 0:
            continue
        mem.append(line)

def display(PC, reg):
    pc = bin(PC)[2:]
    pc = pc.zfill(8)
    print(pc, end = " ")
    regs = reg.keys()
    regs = list(regs)
    for i in regs[:-1]:
        val = bin(reg[i])[2:]
        val = val.zfill(16)
        print(val, end=" ")
    flgs = reg["111"].zfill(16)
    print(flgs)

def main():

    memory = []
    PC = 0
    hlt = 1
    PC_and_Halt = [PC, hlt]
    CC = 0
    var = {}
    register_file = {"000": 0, "001": 0, "010": 0, "011": 0, "100": 0, "101": 0, "110": 0, "111": "0000"}
    memory_initialisation(memory)
    while PC_and_Halt[1]:
        instn = memory[PC][0]
        Execution_Engine.exec(instn, PC_and_Halt, register_file, var)
        display(PC, register_file)
        PC = PC_and_Halt[0]
        CC += 1
    i = len(memory)
    while i != 256:
        memory.append(["0000000000000000"])
        i = i + 1
    for line in memory:
        print(line[0])

if __name__ == '__main__':
    main()


