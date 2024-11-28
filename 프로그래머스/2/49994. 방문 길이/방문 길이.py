def solution(dirs):
    answer = 0
    x,y= 0,0
    walked_way=set()
    
    for i in dirs:
        previous_coordinate= (x,y)
        if i=="L" and x> -5:
            x-=1
        elif i=="R" and x< 5:
            x+=1
        elif i=="U" and y< 5:
            y+=1
        elif i=="D" and y> -5:
            y-=1
        else:
            continue
            
        current_coordinate= (x,y)
        
        if (previous_coordinate, current_coordinate) not in walked_way and (current_coordinate, current_coordinate):
            walked_way.add((previous_coordinate, current_coordinate))
            walked_way.add((current_coordinate, previous_coordinate))
            answer+=1
        
            
    return answer