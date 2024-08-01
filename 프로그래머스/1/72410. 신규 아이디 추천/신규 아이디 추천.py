def solution(new_id):
    
    new_id=new_id.lower() #1단계: 소문자로 변환 

    tmp=""

    for char in new_id:
        if char.isdigit() or  char.isalpha() or char in ['-','_','.']:
            tmp+=char #2단계: 특수문자 제거

    new_id=tmp

    while ".." in new_id:
        new_id=new_id.replace("..",".") #3단계: 연속된 점 제거
  
    if len(new_id)>0 and new_id[0]==".": #4단계 .이 맨앞이나 뒤일경우 제거.
        new_id=new_id[1:]
     
    if len(new_id)>0 and new_id[-1]==".":
        new_id=new_id[:-1]
     

    if new_id=="":#5단계 빈 문자열인 경우 a추가
        new_id='a'

    if len(new_id)>15: #6단계 길이가 15이상인경우 앞의 15자리만 표시
        new_id=new_id[:15]
        if new_id[-1]=='.':
            new_id=new_id[:-1]

    while len(new_id)<3: #7단계..
        new_id+=new_id[-1]
        

    return new_id