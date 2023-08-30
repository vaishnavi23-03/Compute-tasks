if __name__ == '__main__':
    
    N = int(input())
    l=[]
    for i in range(N):
        command = input()
        command1 = command.split()
        if command1[0]=="insert":
            l.insert(int(command1[1]), int(command1[2]))
        elif command1[0]=="print":
            print(l)
        elif command1[0]=="remove":
            l.remove(int(command1[1]))
        elif command1[0]=="append":
            l.append(int(command1[1]))
        elif command1[0]=="sort":
            l.sort()
        elif command1[0]=="pop":
            l.pop()
        elif command1[0]=="reverse":
            l.reverse()
        