def cifra_cesar(texto, deslocamento):
    resultado = ""
    
    for char in texto:
        if char.isalpha():  # Verifica se o caractere é uma letra
            deslocamento_base = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - deslocamento_base + deslocamento) % 26 + deslocamento_base)
            
        else:
            resultado += char  # Mantém caracteres não alfabéticos inalterados
    
    return resultado

# teste da função
texto_original = "Exemplo de cifra de César!"
deslocamento = 3
texto_cifrado = cifra_cesar(texto_original, deslocamento)
print(f"Texto original: {texto_original}")
print(f"Texto cifrado: {texto_cifrado}")
# Exemplo de uso