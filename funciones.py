#Hector Alejandro Franco Berrios
#Rene Ismael Fuentes Benitez

def valuser(user):
    length = len(user)
    if length < 6:
        print("El usuario debe de tener un minimo de 6 caracteres.")
    elif length > 12: 
        print("El usuario debe de tener un maximo de 12 caracteres.")
    else:
        if user.isalnum():
            print("Usuario valido!")
        else:
            print("El usuario solo puede contener letras y numeros.")

def check_space(string): 
    count = 0
    for i in string: 
        if i == " ": 
            count += 1
    return count 

def valpas(password):
    length = len(password)
    if length <8:
        print("La contraseña elegida no es segura.")
    elif check_space(password) != 0:
        print("La contraseña elegida no es segura.")
    else:
        print("Contraseña valida!")
