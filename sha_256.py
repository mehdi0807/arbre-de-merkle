# Les constants de SHA-256
K_i = ['428a2f98', '71374491', 'b5c0fbcf', 'e9b5dba5', '3956c25b', '59f111f1', '923f82a4', 'ab1c5ed5', 'd807aa98', '12835b01', '243185be', '550c7dc3', '72be5d74', '80deb1fe', '9bdc06a7', 'c19bf174', 'e49b69c1', 'efbe4786', '0fc19dc6', '240ca1cc', '2de92c6f', '4a7484aa', '5cb0a9dc', '76f988da', '983e5152', 'a831c66d', 'b00327c8', 'bf597fc7', 'c6e00bf3', 'd5a79147', '06ca6351', '14292967', '27b70a85', '2e1b2138', '4d2c6dfc', '53380d13', '650a7354', '766a0abb', '81c2c92e', '92722c85', 'a2bfe8a1', 'a81a664b', 'c24b8b70', 'c76c51a3', 'd192e819', 'd6990624', 'f40e3585', '106aa070', '19a4c116', '1e376c08', '2748774c', '34b0bcb5', '391c0cb3', '4ed8aa4a', '5b9cca4f', '682e6ff3', '748f82ee', '78a5636f', '84c87814', '8cc70208', '90befffa', 'a4506ceb', 'bef9a3f7', 'c67178f2']
K=[]
for i in range(64):
    l = len(bin(int(K_i[i], 16))[2:])
    if l == 32:
        K.append(bin(int(K_i[i], 16))[2:])
    else:
        K.append('0'*(32-l) + bin(int(K_i[i], 16))[2:])

# Les fonctions utilisées
def ascii_(message):
    result = ''
    for character in message:
        result = result + bin(ord(character))[2:]
    return result

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def solve_congruence(a, b, m):
    gcd, x, y = extended_gcd(a, m)
    if b % gcd != 0:
        return None  # No solution
    else:
        a_inv = x
        x = (a_inv * (b // gcd)) % m
        return x

def padding(message):
    l = len(message)
    k= solve_congruence(1, (448-(l+1)), 512)
    l_binary = (64-len(bin(l)[2:]))*'0' + bin(l)[2:]
    message = message + '1' + '0'*k + l_binary
    return message

def parsing(message):
    l = len(message)
    k = int(l/512)
    blocks = []
    for j in range(k):
        block = {}
        for i in range(16):
            block[f'M_{j}_{i}'] = message[512*j+i*32:512*j+i*32+32]
        blocks.append(block)
    return blocks

def rotr(n, x):
    """
    La fonction effectue le déplacement avec n de chaque bit de x vers la gauche en rotation
    """
    new_x = x[-n:]
    for i in range(len(x)-n):
        new_x = new_x + x[i]
    return new_x

def shr(n, x):
    """
    La fonction effectue le déplacement avec n de chaque bit vers la gauche 
    mais pas de rotation on remplace les n premiers bits par des zeros
    """
    new_x = '0'*n
    for i in range(len(x)-n):
        new_x = new_x + x[i]
    return new_x

def add2(a, b):
    return ''.join('0' if i == j else '1' for i, j in zip(a,b))
def add3(a,b,c):
    return add2(add2(a,b),c)
def add4(a,b,c,d):
    return add2(add3(a,b,c), d)
def add5(a,b,c,d,e):
    return add2(add4(a,b,c,d),e)

def petit_sigma_0(x):
    result = add3(rotr(7, x), rotr(18, x), shr(3, x))
    return result

def petit_sigma_1(x):
    result = add3(rotr(17, x), rotr(19, x), shr(10, x))
    return result

def schedule(block, j):
    """
    'j' est l'indice du bloc
    """
    W = {}
    for i in range(16):
        W[f'W_{i}'] = block[f'M_{j}_{i}']
    for i in range(16, 64):
        W[f'W_{i}'] = add4(petit_sigma_1(W[f'W_{i-2}']), W[f'W_{i-7}'], petit_sigma_0(W[f'W_{i-15}']), W[f'W_{i-16}'])
    return W

def grand_sigma_0(x):
    result = add3(rotr(2,x), rotr(13,x), rotr(22,x))
    return result

def grand_sigma_1(x):
    result = add3(rotr(6,x), rotr(11,x), rotr(25,x))
    return result

def ch(x,y,z):
    """
    Elle prend 3 nombres binaires
    et bit par bit: 
    Si le bit du premier nombre est 1, on prnd le bit du deuxième nombre
    Si non on prend le bit du troisème nombre
    """
    result = ''.join(j if i == 1 else k for i, j, k in zip(x,y,z))
    return result

def maj(x,y,z):
    """
    On prend toujours le bit majoritaire entre les 3 nombres
    """
    result = ''.join('0' if (((i=='0') & (j=='0') & (k=='0')) | ((i=='1') & (j=='0') & (k=='0')) | ((i=='0') & (j=='1') & (k=='0')) | ((i=='0') & (j=='0') & (k=='1'))) else '1'for i, j, k in zip(x,y,z))
    return result

# Fonction de hachage
def sha_256(message):
        H_0 = '01101010000010011110011001100111'
        H_1 = '10111011011001111010111010000101'
        H_2 = '00111100011011101111001101110010'
        H_3 = '10100101010011111111010100111010'
        H_4 = '01010001000011100101001001111111'
        H_5 = '10011011000001010110100010001100'
        H_6 = '00011111100000111101100110101011'
        H_7 = '01011011111000001100110100011001'
        message = ascii_(message)
        message = padding(message)
        blocks = parsing(message)
        k = len(blocks)
        for i in range(k):
            W = schedule(blocks[i], i)
            a = H_0
            b = H_1
            c = H_2
            d = H_3
            e = H_4
            f = H_5
            g = H_6
            h = H_7
            for i in range(64):
                T_1 = add5(h, grand_sigma_1(e), ch(e,f,g), K[i], W[f'W_{i}'])
                T_2 = add2(grand_sigma_0(a), maj(a,b,c))
                h=g
                g=f
                f=e
                e = add2(d, T_1)
                d=c
                c=b
                b=a
                a = add2(T_1, T_2)
                H_0 = add2(a, H_0)
                H_1 = add2(b, H_1)
                H_2 = add2(c, H_2)
                H_3 = add2(d, H_3)
                H_4 = add2(e, H_4)
                H_5 = add2(f, H_5)
                H_6 = add2(g, H_6)
                H_7 = add2(h, H_7)
        return H_0 + H_1 + H_2 + H_3 + H_4 + H_5 + H_6 + H_7