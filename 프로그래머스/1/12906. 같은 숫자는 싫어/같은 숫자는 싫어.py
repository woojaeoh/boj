def solution(arr):
    answer = []
    for i in range(len(arr)):
         if not answer or answer[-1]!=arr[i]:
                answer.append(arr[i])       
                
                

    return answer

#연속되는값이 아닐경우 answer에 append한다.
            