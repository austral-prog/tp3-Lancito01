def check_vowels():
    # Código a implementar utilizando input.
    name = input("Ingrese un nombre:\n> ")

    print(
        f"""
Contiene a: {"a" in name.lower()}
Contiene e: {"e" in name.lower()}
Contiene i: {"i" in name.lower()}
Contiene o: {"o" in name.lower()}
Contiene u: {"u" in name.lower()}
"""
    )


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
