
simboli=["%", "$", "!", ",", ".", "-", "&", "£", "#",]
output = False
def controllopassword(password):
    if len(password) >= 5 and len(password) <= 10:
        print("La lunghezza è ok ✓")
        output = True
    if any(char.isdigit() for char in password):
        print("Contiene almeno una cifra ✓")
        output = True
    if any(char.isupper() for char in password):
        print("Contiene una maiuscola ✓")
        output = True
    if any(char.islower() for char in password):
        print("Contiene una minuscola ✓")
        output = True
    if any(char in simboli for char in password):
        print("Contiene almeno un simbolo ✓")
        output = True
    if output:
        return output

def main():
    password = input("Inserisci una password da validare: ")
    if controllopassword(password):
        print("La password non è sicura ✗")
    else:
        print("La password è sicura ✓")

if __name__ == '__main__':
    main()