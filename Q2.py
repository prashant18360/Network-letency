
import statistics
inp_str = input ("Enter the string :")
inp_pack = input("Enter the no. of packets :")
list = []
for ele in range(0, len(inp_str)):
    if inp_str[ele] == "t" and inp_str[ele+1] == "i":
        str1 = inp_str[ele+5:ele+9]
        f = float(str1)
        list.append(f)

list.sort()
print(list)
median_a = statistics.median(list)
print("median is" , median_a)

a = int(0.90*int(inp_pack))
print("90 percentile latency" , list[a-1])

b = int(0.99*int(inp_pack))
print("99 percentile latency" , list[b-1])
