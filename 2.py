import csv
with open("data.csv") as csvfile:
    data = [tuple(data) for data in csv.reader(csvfile)]

d = []
for i in zip(*data):
    d.append(list(set(i)))

def consistant(h1,h2):
    for x,y in zip(h1,h2):
        if x!='?' and x!=y:
            return False
    return True

def candidate():
    G = {('?',)*(len(data[0])-1)}
    S = ['@']*(len(data[0])-1)
    no=0
    print("[{0}]:".format(no),G)
    print("[{0}]:".format(no),S)
    for item in data:
        no+=1
        inp,res = item[:-1],item[-1]
        if res in 'Yes':
            G = {g for g in G if consistant(g,inp)}
            i = 0
            for s,x in zip(S,inp):
                if s!=x:
                    S[i] = '?' if s!='@' else x
                i+=1
        else:
            Gprev = G.copy()
            for g in Gprev:
                for i in range(len(g)):
                    if g[i]=='?':
                        for val in d[i]:
                            if val!=inp[i] and val==S[i]:
                                g_new = g[:i] + (val,) + g[i+1:]
                                G.add(g_new)
                G.difference_update([ h for h in G if any([consistant(h,g1) for g1 in G if h!=g1])])
        print("[{0}]:".format(no),G)
        print("[{0}]:".format(no),S)
candidate()
                