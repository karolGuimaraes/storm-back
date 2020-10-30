""""
Dados n inteiros não negativos representando um mapa de
elevação onde a largura de cada barra é 1, calcule quanta
água é capaz de reter após a chuva.
"""

def retention(elevation_map):
    retention = 0
    left = 0
    max_left = 0
    max_right = 0
    right = len(elevation_map) - 1

    while(left < right):
        if elevation_map[left] < elevation_map[right]:
            if elevation_map[left] >= max_left: 
                max_left = elevation_map[left]
            else:
                retention += (max_left - elevation_map[left])
            left+=1
        else:
            if elevation_map[right] >= max_right: 
                max_right = elevation_map[right]
            else:
                retention += (max_right - elevation_map[right])
            right-=1
    return retention
    
print(retention([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))