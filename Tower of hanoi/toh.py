def towerOfHanoi(n,from_rod,to_rod,helper_rod):
    if (n==1):
        print(f"Move disk "+(str(n))+" from rod "+from_rod+" to rod "+ to_rod)
        return
    towerOfHanoi(n-1,from_rod,helper_rod,to_rod)
    print("Move disk "+(str(n))+" from rod "+from_rod+" to rod "+ to_rod)
    towerOfHanoi(n-1,helper_rod,to_rod,from_rod)
    



towerOfHanoi(2,"A","C","B")