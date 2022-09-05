# 피연산자 : + / * -


from collections import deque

T = int(input())
  

for test_case in range(1, T + 1):         
    
    forth_check = True # error 여부 검사
    forth = deque([])  # 스택 초기화
    nums = input().split() 

    if nums.pop()!='.': # .이후에 어떠한 데이터가 들어오면 error
        forth_check = False
    
    else:
        for num in nums:       
            if num.isdigit(): # 데이터가 숫자라면 스택에 쌓음
                forth.append(int(num))
            elif len(forth)<2: # 피연산자를 만났을 때 숫자가 부족할 경우
                forth_check = False
                break
            else:
                a = int(forth.pop())
                b = int(forth.pop())
                if num == '+':
                    forth.append(b + a)   
                elif num == '*':
                    forth.append(b * a)    
                elif num == '-':
                    forth.append(b - a)   
                elif num == '/':
                    forth.append(b / a)

    if len(forth)==1 and forth_check: # 최종 결과가 숫자 1개라면 출력
        print(f'#{test_case} {forth[0]}')
    else: print(f'#{test_case} error') # 피연산자가 부족할 경우

