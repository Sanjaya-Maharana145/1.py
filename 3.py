def up_side_doenEqual(S):
    for i in range(len(S)):
        if (S[i] not in ('0', '1', '2', '5', '6','8','9','11','16','18','19')):
            return "No"
    return "Yes"
 
input1 = 8
c = 0
for i in range(1,1000):
    if (up_side_doenEqual(str(i)) == 'Yes'):
        res = i
        c = c+1
    if c==input1:
        break
print(res)
