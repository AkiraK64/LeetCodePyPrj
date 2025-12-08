class CFSolution:
    def __init__(self):
        pass
    # 4A - Watermelon
    def solution_4A():
        w = int(input())
        print("YES" if w % 2 == 0 and w > 3 else "NO")
    # 71A - Way Too Long Words
    def solution_71A():
        n = int(input())
        for _ in range(n):
            st = input()
            if len(st) <= 10:
                print(st)
            else:
                print(st[0] + str(len(st)-2) + st[-1])