#Inheritance
from OopsDemo import Calculator

class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChildImpl()
print(obj.getCompleteData())

#Visual


'''            Calculator (Parent)
              ───────────────────
   #           num = 100
              Summation() → first + second + 100
                      │
                      │ inheritance
                      ▼

              ChildImpl (Child)
              ─────────────────
              num2 = 200
              firstNumber = 2
              secondNumber = 10

getCompleteData()
        │
        ▼

200 + 100 + (2 + 10 + 100)

200 + 100 + 112

= 412
'''