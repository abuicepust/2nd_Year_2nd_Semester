class pip:
    def __init__(self,jobno,profit,deadline):
        self.jobno=jobno
        self.profit=profit
        self.deadline=deadline
def Greedy_method(Matrix,jobno):
    profit=0;
    slot=[-1]*jobno
    for pip in Matrix:
        for j in reversed(range(pip.deadline)):
            if j<jobno and slot[j] == -1:
                slot[j]=pip.jobno
                profit+=pip.profit
                break
    print(f"The sequence are : {list(filter(lambda var:var!=-1,slot))}" )
    return profit

jobno = 5
Matirx=[pip(1,3,1),pip(2,25,3),pip(3,1,2),pip(4,6,1),pip(5,30,2)]
Matirx.sort(key=lambda var:var.profit,reverse=True)
print(f"The maximum profit is : {Greedy_method(Matirx,jobno)}")


