class pip:
    def __init__(self, Jobno, deadline, profit):
        self.Jobno = Jobno
        self.deadline = deadline
        self.profit = profit
def Greedy_method(Matrix, T):
    profit = 0
    slot = [-1] * T
    for pip in Matrix:
        for j in reversed(range(pip.deadline)):
            if j < T and slot[j] == -1:
                slot[j] = pip.Jobno
                profit += pip.profit
                break
    print("Maximum profit sequence: ",list(filter(lambda var: var !=-1, slot)))
    return profit





Matrix=[pip(1,1,3),pip(2,3,5),pip(3,4,20),pip(4,3,18),pip(5,2,1),pip(6,1,6),pip(7,2,30)]
job_no=5
Matrix.sort(key=lambda var: var.profit, reverse=True)
print("Maximum profit: ", Greedy_method(Matrix,job_no))
