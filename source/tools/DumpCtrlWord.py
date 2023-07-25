import sys


def readRomContent(fileName):
    with open(fileName, "rb") as rom0File:
        return rom0File.read()


def printHeader():
    print("                - - -         ")
    print("        -       P P S         ")
    print("        P - - I C C E  A C    ")
    print("        C M M L C C Q  L O    ")
    print("        S W A O L L R  U N D S")
    print("        E R C A K K S  O S E R")
    print("        L I C D H L T  P T S C")
    print("------  ----------------------")


def printControlWord(addr):
    src = rom0[addr] & 0x0F
    des = (rom0[addr] & 0xF0) >> 4
    const = rom1[addr] & 0x0F
    aluOp = (rom1[addr] >> 4) | ((rom2[addr] & 0x01) << 5)
    seqRst = (rom2[addr] & 0x02) >> 1
    pcClkLo = (rom2[addr] & 0x04) >> 2
    pcClkHi = (rom2[addr] & 0x08) >> 3
    iLoad = (rom2[addr] & 0x10) >> 4
    mAccess = (rom2[addr] & 0x20) >> 5
    mWrite = (rom2[addr] & 0x40) >> 6
    pcSel = (rom2[addr] & 0x80) >> 7

    print("{:05X}:  {:01X} {:01X} {:01X} {:01X} {:01X} {:01X} {:01X} {:02X} {:01X} {:01X} {:01X}"
       .format(addr, pcSel, mWrite, mAccess, iLoad, pcClkHi, pcClkLo, seqRst, aluOp, const, des, src))


rom0 = readRomContent("D:\\AppleWinSAP\\SAP6502_ROM0.bin")
rom1 = readRomContent("D:\\AppleWinSAP\\SAP6502_ROM1.bin")
rom2 = readRomContent("D:\\AppleWinSAP\\SAP6502_ROM2.bin")
rom3 = readRomContent("D:\\AppleWinSAP\\SAP6502_ROM3.bin")
rom4 = readRomContent("D:\\AppleWinSAP\\SAP6502_ROM4.bin")

printHeader()

inst = 0x85
addr = inst
printControlWord(addr)

addr += 0x100
printControlWord(addr)

addr += 0x100
printControlWord(addr)

addr += 0x100
printControlWord(addr)
