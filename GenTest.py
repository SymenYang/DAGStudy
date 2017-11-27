#coding=utf-8 
filename = raw_input("input filename")

fd = open(filename,'a')

for i in range(2,100,1):
    point = "POINT,知识点%d,这是知识点%d，测试数据,end,,,,\n" %(i,i)
    fd.write(point)
    for j in range(1,5,1):
        prob = "PROBLEM,测试题，这道题选第%d个,A,B,C,D,%d,end\n" %(j,j)
        fd.write(prob)
    link1 = "LINK,http://www.baidu.com,,,,,,\n"
    link2 = "LINK,http://www.google.com,,,,,,\n"
    rela = "RELATION,%d,,,,,,,\n" % max(1,i - 6)
    fd.write(link1)
    fd.write(link2)
    fd.write(rela)
    if i > 7:
        rela2 = "RELATION,%d,,,,,,,\n" % (i - 6 + 1)
        fd.write(rela2)
    
