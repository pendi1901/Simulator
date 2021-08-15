
def exec(instn, pch, reg, var):
    opc = instn[:5]
    #fnc_call_gen = {"00000": add(instn, pch, reg), "00001": sub(instn, pch, reg), "00010": movI(instn, pch, reg),
     #               "00011": movR(instn, pch, reg), "00100": load(instn, pch, reg, var), "00101": store(instn, pch, reg),
      #              var), "00110": mul(instn, pch, reg), "00111": div(instn, pch, reg), "01000": rshift(instn, pch, reg),
       #             "01001": lshift(instn, pch, reg), "01010": xor(instn, pch, reg), "01011": OR(instn, pch, reg),
        #            "01100": AND(instn, pch, reg), "01101": invert(instn, pch, reg), "01110": cmp(instn, pch, reg),
         #           "01111": jmp(instn, pch, reg), "10000": jlt(instn, pch, reg), "10001": jgt(instn, pch, reg),
          #          "10010": je(instn, pch, reg), "10011": hlt(pch, reg)}
    if opc == "00010":
        movI(instn, pch, reg)
    elif opc == "00101":
        store(instn, pch, reg, var)
    elif opc == "10010":
        je(instn, pch, reg)
    elif opc == "00000":
        add(instn, pch, reg)
    elif opc == "00001":
        sub(instn, pch, reg)
    elif opc == "00011":
        movR(instn, pch, reg)
    elif opc == "00100":
        load(instn, pch, reg, var)
    elif opc == "00110":
        mul(instn, pch, reg)
    elif opc == "00111":
        div(instn, pch, reg)
    elif opc == "01000":
        rshift(instn, pch, reg)
    elif opc == "01001":
        lshift(instn, pch, reg)
    elif opc == "01010":
        xor(instn, pch, reg)
    elif opc == "01011":
        OR(instn, pch, reg)
    elif opc == "01100":
        AND(instn, pch, reg)
    elif opc == "01101":
        invert(instn, pch, reg)
    elif opc == "01110":
        cmp(instn, pch, reg)
    elif opc == "01111":
        jmp(instn, pch, reg)
    elif opc == "10000":
        jlt(instn, pch, reg)
    elif opc == "10001":
        jgt(instn, pch, reg)
    else:
        hlt(pch, reg)

def overflow(register, reg):
    if reg[register] > 65535:
        reg[register] %= 65536
        reg["111"] = "1000"
    elif reg[register] < 0:
        reg[register] = 0
        reg["111"] = "1000"

def add(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-9:-6]
    r2 = instn[-6:-3]
    r3 = instn[-3:]
    reg[r1] = reg[r2] + reg[r3]
    pch[0] += 1
    overflow(r1, reg)

def sub(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-9:-6]
    r2 = instn[-6:-3]
    r3 = instn[-3:]
    reg[r1] = reg[r2] - reg[r3]
    pch[0] += 1
    overflow(r1, reg)

def movI(instn, pch, reg):
    reg["111"] = "0000"
    imm = instn[-8:]
    r1 = instn[-11:-8]
    reg[r1] = int(imm, 2)
    pch[0] += 1

def movR(instn, pch, reg):
    r1 = instn[-6:-3]
    r2 = instn[-3:]
    if r2 == "111":
        reg[r1] = int(reg[r2], 2)
    else:
        reg[r1] = reg[r2]
    pch[0] += 1
    reg["111"] = "0000"

def load(instn, pch, reg, var):
    reg["111"] = "0000"
    vr = instn[-8:]
    vr = int(vr, 2)
    r1 = instn[-11:-8]
    if vr not in var.keys():
        var[vr] = 0
    reg[r1] = var[vr]
    pch[0] += 1

def store(instn, pch, reg, var):
    reg["111"] = "0000"
    vr = instn[-8:]
    r1 = instn[-11:-8]
    var[int(vr, 2)] = reg[r1]
    pch[0] += 1

def mul(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-9:-6]
    r2 = instn[-6:-3]
    r3 = instn[-3:]
    reg[r1] = reg[r2] * reg[r3]
    pch[0] += 1
    overflow(r1, reg)

def div(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-6:-3]
    r2 = instn[-3:]
    if reg[r2] != 0:
        reg["000"] = reg[r1] // reg[r2]
        reg["001"] = reg[r1] % reg[r2]
    pch[0] += 1

def rshift(instn, pch, reg):
    reg["111"] = "0000"
    imm = instn[-8:]
    r1 = instn[-11:-8]
    rs = int(imm, 2)
    if rs > 15:
        reg[r1] = 0
    else:
        d = 2**rs
        reg[r1] //= d
    pch[0] += 1

def lshift(instn, pch, reg):
    reg["111"] = "0000"
    imm = instn[-8:]
    r1 = instn[-11:-8]
    rs = int(imm, 2)
    if rs > 15:
        reg[r1] = 0
    else:
        d = 2**rs
        temp = reg[r1]
        temp *= d
        reg[r1] = temp % 65536
    pch[0] += 1

def xor(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-9:-6]
    r2 = instn[-6:-3]
    r3 = instn[-3:]
    reg[r1] = reg[r2] ^ reg[r3]
    pch[0] += 1

def OR(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-9:-6]
    r2 = instn[-6:-3]
    r3 = instn[-3:]
    reg[r1] = reg[r2] | reg[r3]
    pch[0] += 1

def AND(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-9:-6]
    r2 = instn[-6:-3]
    r3 = instn[-3:]
    reg[r1] = reg[r2] & reg[r3]
    pch[0] += 1

def invert(instn, pch, reg):
    reg["111"] = "0000"
    r1 = instn[-6:-3]
    r2 = instn[-3:]
    reg[r1] = ~ reg[r2]
    pch[0] += 1

def cmp(instn, pch, reg):
    r1 = instn[-6:-3]
    r2 = instn[-3:]
    if reg[r1] < reg[r2]:
        reg["111"] = "0100"
    elif reg[r1] > reg[r2]:
        reg["111"] = "0010"
    else:
        reg["111"] = "0001"
    pch[0] += 1

def jmp(instn, pch, reg):
    addr = instn[-8:]
    pch[0] = int(addr, 2)
    reg["111"] = "0000"

def jlt(instn, pch, reg):
    addr = instn[-8:]
    if reg["111"][1] == '1':
        pch[0] = int(addr, 2)
    else:
        pch[0] += 1
    reg["111"] = "0000"

def jgt(instn, pch, reg):
    addr = instn[-8:]
    if reg["111"][2] == '1':
        pch[0] = int(addr, 2)
    else:
        pch[0] += 1
    reg["111"] = "0000"

def je(instn, pch, reg):
    addr = instn[-8:]
    if reg["111"][-1] == '1':
        pch[0] = int(addr, 2)
    else:
        pch[0] += 1
    reg["111"] = "0000"

def hlt(pch, reg):
    pch[0] += 1
    pch[1] = 0
    reg["111"] = "0000"