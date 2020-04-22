
def move(f,t):
    print(f'Move disc from {f} to {t}!')
    

# n number of discs
# f from position, h helper(via) and target pin
def hanoi(n,f,h,t):
    if n == 0:  # Prevent from moving 0 or negative discs
        pass
    else:
        hanoi(n-1,f,t,h) # move all but bottom to helper (A to B using C)
        move(f,t) # move bottom disc to target (from A to C)
        hanoi(n-1,h,f,t) # move rest from helper to target via from (from B to C using A)

hanoi(5, 'A', 'B', 'C')
