#!/usr/bin/python3
import dis

# Votre bytecode complet
bytecode_instructions = [
    (0, 'LOAD_CONST', 1),
    (3, 'LOAD_CONST', 2),
    (6, 'IMPORT_NAME', 'magic_calculation_102'),
    (9, 'IMPORT_FROM', 'add'),
    (12, 'STORE_FAST', 'add'),
    (15, 'IMPORT_FROM', 'sub'),
    (18, 'STORE_FAST', 'sub'),
    (21, 'POP_TOP', None),
    (22, 'LOAD_FAST', 0),
    (25, 'LOAD_FAST', 1),
    (28, 'COMPARE_OP', 0),
    (31, 'POP_JUMP_IF_FALSE', 94),
    (34, 'LOAD_FAST', 'add'),
    (37, 'LOAD_FAST', 0),
    (40, 'LOAD_FAST', 1),
    (43, 'CALL_FUNCTION', (2, 0)),
    (46, 'STORE_FAST', 'c'),
    (49, 'SETUP_LOOP', 38),
    (52, 'LOAD_GLOBAL', 'range'),
    (55, 'LOAD_CONST', 3),
    (58, 'LOAD_CONST', 4),
    (61, 'CALL_FUNCTION', (2, 0)),
    (64, 'GET_ITER', None),
    (65, 'FOR_ITER', 21),
    (68, 'STORE_FAST', 'i'),
    (71, 'LOAD_FAST', 'add'),
    (74, 'LOAD_FAST', 'c'),
    (77, 'LOAD_FAST', 'i'),
    (80, 'CALL_FUNCTION', (2, 0)),
    (83, 'STORE_FAST', 'c'),
    (86, 'JUMP_ABSOLUTE', 65),
    (89, 'POP_BLOCK', None),
    (90, 'LOAD_FAST', 'c'),
    (93, 'RETURN_VALUE', None),
    (94, 'LOAD_FAST', 'sub'),
    (97, 'LOAD_FAST', 0),
    (100, 'LOAD_FAST', 1),
    (103, 'CALL_FUNCTION', (2, 0)),
    (106, 'RETURN_VALUE', None),
    (107, 'LOAD_CONST', None),
    (110, 'RETURN_VALUE', None),
]

# Afficher le bytecode personnalisé
for instruction in bytecode_instructions:
    print(instruction[0], instruction[1], instruction[2])
