#B shift_only

def divisor(n):
    i=0
    while n%2==0:
        n=n/2
        i+=1
    return i
  
N =input()
nums = map(int,input().split())
cnt  = min(map(divisor,nums))
print(cnt)
