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

def exibir_todas_opcoes(texto):
    print("Todas as possiveis decifrações")
    for deslocamento in range(1, 26):
        texto_decifrado = cifra_cesar(texto, -deslocamento)
        print(f"Deslocamento {deslocamento}: {texto_decifrado}")
        

def main():
    texto = input("Digite o texto a ser cifrado: ")
    exibir_todas_opcoes(texto)
if __name__ == "__main__":
    main()

#outro exemplo de uso
def cifra_cesar(texto, deslocamento):
    resultado = ""
    for char in texto:
        if char.isalpha():
            deslocamento_base = ord('a') if char.islower() else ord('A')
            resultado += chr((ord(char) - deslocamento_base + deslocamento) % 26 + deslocamento_base)
        else:
            resultado += char
    return resultado

def exibir_todas_opcoes(texto, palavra_chave=None):
    print("Todas as possiveis decifrações")
    for deslocamento in range(1, 26):
        texto_decifrado = cifra_cesar(texto, -deslocamento)
        print(f"Deslocamento {deslocamento}: {texto_decifrado}")
        if palavra_chave and palavra_chave in texto_decifrado:
            print(f"\nPalavra-chave '{palavra_chave}' encontrada no deslocamento {deslocamento}!")
            print(f"Texto decifrado: {texto_decifrado}")
            break

def main():
    texto = input("Digite o texto a ser decifrado: ")
    palavra_chave = input("Digite a palavra-chave para parar (ou deixe vazio para mostrar todas): ")
    palavra_chave = palavra_chave if palavra_chave else None
    exibir_todas_opcoes(texto, palavra_chave)

if __name__ == "__main__":
    main()