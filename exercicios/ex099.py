def maior(* valor):
    print('-=' * 30)
    print('Analisando os valores passados...')    
    for num in valor:
        print(f'{num}', end=' ')
    print(f'Foram informados {len(valor)} valores ao todo.')        
    print(f'O maior valor informado foi {max(valor)}')

    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(0)
