import sys

#Solicita o usuario a colocar a sequencia de bytes em hexa
print("Por favor, insira a sequência de bytes em hexadecimal (pressione ENTER para finalizar):")

hex_data = ""
while True:
    line = input()
    if line.strip() == "":  # Se a linha estiver em branco, finalize a entrada
        break
    hex_data += line + " "

# Remove espaços extras e converte a sequência para ASCII
ascii_data = bytes.fromhex(hex_data.replace(" ", "").replace("\n", "")).decode('utf-8', 'ignore')

print("\nTexto ASCII convertido:\n")
print(ascii_data)
