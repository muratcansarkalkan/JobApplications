# Hard task. Got 1 out of the 11 correctness test, but the 3 tests still worked, interesting.
# The task was making signs from another sign, eg. you can make "BILL" from "BILLOBILLOBILL" 3 times. The program is supposed to find this

S = ""
L = ""

def solution(S, L):
    possi = 0
    
    for i in L:
        if i in S:
            possi = (S.count(i))
            if possi > 0:
                S = S.strip(i)
                roxy = (S.count(i))
                if roxy == 0:
                    break
                else:
                    possi = possi + roxy
            else:
                break

    # write your code in Python 3.6
    return possi
