

# find modular multiplicative inverse or find private_key such public_key * private_key = 1 (mod phi)
def calculate_private_key(public_key, phi):
    for private_key in range(1, phi + 1):
        if (public_key * private_key):
            return private_key


def power_mod(a, n, m):
    if (n == 0):
        return 1 % m
    else:
        ans = power_mod(a, n // 2, m)
        ans = ans * ans % m
        if (n % 2 == 1):
            ans = ans * a % m
        return ans


def encrypt(message, public_key, m):
    return power_mod(message, public_key, m)


def decrypt(message, private_key, m):
    return power_mod(message, private_key, m)


if __name__ == "__main__":
    q = 31
    p = 37

    e = 23  # public key

    n = p * q
    phi = (q - 1) * (p - 1)

    public_key = e
    private_key = calculate_private_key(public_key, phi)

    message = 1001
    print("message =", message)

    encrypt_message = encrypt(message, public_key, n)
    print("message has been encrypt with public key =", encrypt_message)

    decrypt_message = decrypt(message, private_key, n)
    print("message after decrypt =", decrypt_message)
