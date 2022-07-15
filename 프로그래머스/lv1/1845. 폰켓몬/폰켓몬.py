def solution(nums):
    N = len(nums) // 2
    choice = len(set(nums))

    if choice > N:
        return N
    else:
        return choice
