t = int(input())

for i in range(t):
    women = list()
    men = list()
    
    n = int(input())
    for j in range(n):
        st = input()
        men.append(st.split())
        men[j] = [int(i) for i in men[j]]
    for j in range(n):
        st = input()
        women.append(st.split())
        women[j] = [int(i) for i in women[j]]
    
    wi = [-1]*n
    mi = [1]*n
    
    while -1 in wi:
        for m0 in range(n):
            w0 = men[m0][mi[m0]] -1      
            if(wi[w0] < 0):
                wi[w0] = m0
            else: 
                p0 = women[w0][1:].index(wi[w0]+1)
                p1 = women[w0][1:].index(m0+1)
                if p1 < p0:
                    mi[wi[w0]] = mi[wi[w0]] + 1
                    wi[w0] = m0
                elif p0 < p1:
                    mi[m0] = mi[m0] + 1
        
    for w in range(n):
        print(w+1,wi[w]+1)  
        