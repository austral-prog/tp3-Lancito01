def check_vowels():
    name = input("Ingrese un nombre:\n> ").lower()

    print(f"Contiene a: {"a" in name}")
    print(f"Contiene e: {"e" in name}")
    print(f"Contiene i: {"i" in name}")
    print(f"Contiene o: {"o" in name}")
    print(f"Contiene u: {"u" in name}")

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
