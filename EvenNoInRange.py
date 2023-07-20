def EvenNoInRange(array,query):
    result=[]
    for q in query:
        start=q[0]
        end=q[1]

        count=0
        for i in range(start,end+1):
            if array[i]%2==0:
                count+=1
        result.append(count)

    return result

array=list(map(int,input().split()))
query=[]
q=int(input("No of Queries : "))
for i in range(q):
    query.append(list(map(int,input().split())))

print(EvenNoInRange(array,query))