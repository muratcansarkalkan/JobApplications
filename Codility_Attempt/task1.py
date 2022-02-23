# Easy task. It was about rotating other arrows except the one that was used most. 
# It solved 3 problems shown at test but the correctness test was 5 out of 8.

S = "<<<>>"

def solution(S):

    rotate = len(S) - S.count(max(S))
    # write your code in Python 3.6
    return rotate

solution(S)

