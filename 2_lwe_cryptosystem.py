import numpy as np
import random # It is used to select random numbers

print("Post-Quantum Learning With Errors Cryptography")

# In real life, n would be around 500, q around 2^32, etc. 
# The values ​​here are small to understand the logic.
n = 5       # Hidden key length (vector length). The longer, the better.
q = 20      # module (limit of our integer ring)
m = 10      # number of equations (public key size)

print(f"system started: system started(n)={n}, module(q)={q}")

# BOB: Key Generation
def generate_keys():
    print("\n[BOB] Keys are produced")

    #np.random.randint: It gives us the ability to randomly fill an entire matrix with a single 
    # command, instead of individual numbers.
    #Choose numbers between 0 and q and create a matrix with m rows and n columns.
    # Matrix A: a matrix mxn of random numbers (public)
    
    A = np.random.randint(0, q, (m, n))
    
    # 's' Vector: Our secret (Private Key)
    s = np.random.randint(0, q, n)
    
    # e Vector: Noise
    # We choose very small numbers, like -1, 0, or 1.
    e = np.random.randint(-1, 2, m) 
    
    
    # Vector b: A*s + e (mod q) (Public)
    #Linear Algebra: Multiply A by s, add error.
    b = (np.dot(A, s) + e) % q
    
    print(f"  -> secret key (s): {s}")
    print(f"  -> error vector (e): {e}") 
    print(" -> public key (A and b)")
    
    return (A, b), s

# Bob should make the keys.
public_key, private_key = generate_keys()


# ALICE: Encryption
def encrypt(bit, pub_key):
    print(f"\n[ALICE] '{bit}' bit is encrypted...")
    A, b = pub_key
    
    # A random vector r (for masking) consists of 0s and 1s.
    r = np.random.randint(0, 2, m)
    
    # u = A_transpoz * r (mod q)
    u = np.dot(A.T, r) % q
    
    # v = b * r + (q/2 * message)  (mod q)
    # The logic here is: We scale the message by q/2 (i.e., 10).
    # If the bit is 0, we add 0; if the bit is 1, we add 10.
    scale = int(q/2) if bit == 1 else 0
    v = (np.dot(b, r) + scale) % q
    
    return (u, v)

# Alice wants to send the message '1'.
mesaj = 1
ciphertext = encrypt(mesaj, public_key)
print(f"  -> encrypted text (u, v): {ciphertext}")
print("  -> (The encrypted text appears to be random numbers.)")


#BOB: Decryption
def decrypt(cipher, priv_key):
    print("\n message is decoding...")
    u, v = cipher
    s = priv_key
    
    # Mathematical Magic: Decrypt = v - (s . u)
    # This process removes the mask, leaving behind "Scaled Message + Minor Error".
    noisy_message = (v - np.dot(s, u)) % q
    
    print(f"  -> noisy result: {noisy_message}")
    
    # Decision Making: Is the result closer to 0 or closer to q/2 (10)? 
    # We measure distance (similar to Euclidean logic)
    center = q / 2
    if abs(noisy_message - center) < (q / 4):
        return 1
    else:
        return 0

# Let's see if Bob can solve it.
cozulmus_mesaj = decrypt(ciphertext, private_key)

print(f"\n[conclusion] Original: {mesaj} -> Solved: {cozulmus_mesaj}")

if mesaj == cozulmus_mesaj:
    print("CONGRATULATIONS! The LWE system worked successfully.")
else:
    print("ERROR! The noise was too loud, the message was corrupted.")