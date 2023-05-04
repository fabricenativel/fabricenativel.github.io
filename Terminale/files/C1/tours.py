import hanoi


def solution(nb_disque,dep,inter,arr):
    if nb_disque>1:
        solution(nb_disque-1,dep,arr,inter)
        hanoi.deplace_disque(dep,arr)
        solution(nb_disque-1,inter,dep,arr)
    else:
        hanoi.deplace_disque(dep,arr)

hanoi.dessine_depart(6)
solution(6,1,2,3)
hanoi.fin()