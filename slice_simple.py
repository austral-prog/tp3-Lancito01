def slice_simple():
    texto = "Awesome"

    print(texto[:3].lower())
    from_index = len(texto)//2-1
    print(texto[from_index:from_index+3].lower())
    print((texto[:3+1] + texto[-3:]).lower())
    # Código a implementar, se debe utilizar la variable 'texto' para resolver el ejercicio.
    # No se debe modificar la definición de la función, ni ingresar otro valor mediante input.

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_slice_simple_test.py` o `python tp3_slice_simple_test.py`
