import tokenize
from io import BytesIO

# Lista de palabras reservadas y funciones integradas en Python
PALABRAS_RESERVADAS = {
    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
    'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
    'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
    'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
    'try', 'while', 'with', 'yield'
}

FUNCIONES_INTEGRADAS = {
    'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 
    'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 
    'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 
    'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 
    'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 
    'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max', 'memoryview', 
    'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 
    'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 
    'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'
}

# Combinar ambas listas
RESERVADAS_E_INTEGRADAS = PALABRAS_RESERVADAS.union(FUNCIONES_INTEGRADAS)

codigo_ejemplo = """
x = 10.50
if x > 5:
    print("Mayor que 5")
"""

codigo_en_bytes = codigo_ejemplo.encode('utf-8')
archivo_virtual = BytesIO(codigo_en_bytes)
lista_de_tokens = tokenize.tokenize(archivo_virtual.readline)

contador = 0

print("N°\tTipo de token\t\tValor")
print("-" * 50)

for token in lista_de_tokens:
    if token.type in (tokenize.ENCODING, tokenize.ENDMARKER):
        continue
    
    # Determinar el nombre del tipo
    if token.type == tokenize.NAME and token.string in RESERVADAS_E_INTEGRADAS:
        nombre_del_tipo = "NAMER"  # Para palabras reservadas y funciones integradas
    else:
        nombre_del_tipo = tokenize.tok_name[token.type]  # Para todo lo demás
    
    contador += 1
    print(f"{contador}\t{nombre_del_tipo}\t\t{token.string}")