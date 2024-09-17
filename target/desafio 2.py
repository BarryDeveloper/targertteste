def contar_letra_a(texto):
    if not texto.isalpha():
        print("A entrada deve ser uma string, não um número ou caracteres especiais.")
        return

    quantidade_a = texto.lower().count('a')
    
    if quantidade_a > 0:
        print(f"A letra 'a' (maiúscula ou minúscula) ocorre {quantidade_a} vezes.")
    else:
        print("A letra 'a' (maiúscula ou minúscula) não ocorre na string.")


texto = input("Digite uma string: ")
contar_letra_a(texto)
