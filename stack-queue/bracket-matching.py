def cek_bracket(ekspresi):

    stack = []

    pasangan = {")": "(", "}": "{", "]": "["}

    for char in ekspresi:
        if char in "([{":
            stack.append(char)
            print(f"Push: {char}, Stack: {stack}")
        elif char in ")]}":
            if len(stack) == 0:
                print(f"Error: Tidak ada pasangan untuk {char}")
                return False
            elif stack[-1] == pasangan[char]:
                stack.pop()
                print(f"Pop: {char}, Stack: {stack}")

        if len(stack) == 0:
            print("Ekspresi valid")
            return True
        else:
            print("Ekspresi tidak valid")
            return False


# Simulasi Penggunaan

cek_bracket("(){}[]")  # Valid
cek_bracket("([)]")  # Tidak Valid
cek_bracket("((()")  # Tidak Valid
