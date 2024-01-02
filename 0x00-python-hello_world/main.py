import dis

# Votre bytecode
bytecode = b'\x64\x00\x00\x64\x01\x00\x17\x64\x02\x00\x83\x64\x03\x00\x01'
# Convertir le bytecode en code Python
code_object = dis.Bytecode(bytecode)
instructions = list(code_object)

# Afficher les instructions sous forme de code Python
for instr in instructions:
    print(dis.opname[instr.opcode], instr.argval)
