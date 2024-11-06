def solution(a, b, n):
    answer= 0 #총 받게된 콜라병 수
    while(n>=a):
        remain_bottle=n%a   #남은 콜라의 개수
        n=(n//a)*b #마트에서 받은 콜라의 개수       
        answer+=n #받은 콜라의 개수 업데이트
        n+=remain_bottle #현재 가지고 있는 콜라의 개수 업데이트
        
    return answer