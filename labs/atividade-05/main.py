
def maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao):
    
    s = 0
    r = 0
    for figurinhas_da_maria in figurinhas_da_maria:
        s += 1      
        if figurinhas_da_maria not in figurinhas_da_joao:
            y = figurinhas_da_joao
            figurinhas_da_maria = y
        else:
            s -= 1 
        if figurinhas_da_maria in figurinhas_da_joao:
            r += 2
    s -= r 
    if s < 0:
        s = 0                   
    return s


if __name__ == '__main__':
    A, B = input().split(' ')
    figurinhas_da_maria = input().split(' ')
    figurinhas_da_joao = input().split(' ')
    print(maximizar_troca_de_figurinhas(figurinhas_da_maria, figurinhas_da_joao))
