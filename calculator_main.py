import sys
from PyQt5.QtWidgets import *
import numpy
import math

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        ### 각 위젯을 배치할 레이아웃을 미리 만들어 둠
        ### 사칙연산 배치변경
        layout_dog = QGridLayout()
        ###layout_clear_equal = QGridLayout()
        ###layout_number = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 위한 LineEdit 위젯 생성
        ##label_equation = QLabel("Equation: ")
        ##label_solution = QLabel("Number: ")
        ##self.equation = QLineEdit("")
        ##self.solution = QLineEdit("")
        
        ###숫자 입력/표시 부분 통합
        self.number_display = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식, 답 위젯을 추가
        ##layout_equation_solution.addRow(label_equation, self.equation)
        ##layout_equation_solution.addRow(label_solution, self.solution)
        layout_equation_solution.addRow(self.number_display)
        ### 사칙연상 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")
        
        ### 과제연산 버튼 생성
        button_rem =QPushButton("%")
        button_CE =QPushButton("CE")
        button_exp =QPushButton("x^2")
        button_inv =QPushButton("1/x")
        button_root =QPushButton("root")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))
        
        ### 과제연산 버튼을 클릭했을 때, 각 과제연산 부호가 수식창에 추가될 수 있도록 시그털 설정
        button_rem.clicked.connect(lambda state, operation = "%": self.button_operation_clicked(operation))
        button_exp.clicked.connect(self.button_exp_clicked)
        button_inv.clicked.connect(self.button_inv_clicked)
        button_root.clicked.connect(self.button_root_clicked)

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_dog.addWidget(button_plus,4,3,1,1)
        layout_dog.addWidget(button_minus,3,3,1,1)
        layout_dog.addWidget(button_product,2,3,1,1)
        layout_dog.addWidget(button_division,1,3,1,1)
        
        ### 과제연산 버튼을 layout_operation 레이아웃에 추가
        layout_dog.addWidget(button_rem, 0,0,1,1)
        layout_dog.addWidget(button_CE,0,1,1,1)
        layout_dog.addWidget(button_exp,1,1,1,1)
        layout_dog.addWidget(button_inv,1,0,1,1)
        layout_dog.addWidget(button_root,1,2,1,1)

        ### =, clear, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_C = QPushButton("C")
        button_backspace = QPushButton("<[x]")

        ### =, clear, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_C.clicked.connect(self.button_C_clicked)
        button_CE.clicked.connect(self.button_CE_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, clear, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_dog.addWidget(button_C,0,2,1,1)
        layout_dog.addWidget(button_backspace,0,3,1,1)
        layout_dog.addWidget(button_equal,5,3,1,1)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number+5, 3)
                layout_dog.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_dog.addWidget(number_button_dict[number], 5, 1)

        ### 소숫점 버튼과 00 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_display(num))
        layout_dog.addWidget(button_dot, 5, 2)

        button_double_zero = QPushButton("00")
        button_double_zero.clicked.connect(lambda state, num = "00": self.number_button_clicked(num))
        layout_dog.addWidget(button_double_zero, 5, 0)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_dog)
        ###main_layout.addLayout(layout_clear_equal)
        ###main_layout.addLayout(layout_number)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################
    def number_button_clicked(self, num):
        number = self.number_display.text()
        number += str(num)
        self.number_display.setText(number)

    def button_operation_clicked(self, operation):
        number= self.number_display.text()
        number += operation
        self.number_display.setText(number)
          
    def button_equal_clicked(self):
        number = self.number_display.text()  
        solution = eval(number)
        self.number_display.setText(str(solution))

    def button_C_clicked(self):
        self.number_display.setText("")
        
    def button_CE_clicked(self):
            self.number_display.setText("")
        
    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)
    
    def button_exp_clicked(self):
        number=self.number_display.text()
        number+='**2'
        self.number_display.setText(number)
    def button_inv_clicked(self):
        number=self.number_display.text()
        number+='**-1'
        self.number_display.setText(number)
    def button_root_clicked(self):
        number=self.number_display.text()
        number+='**(1/2)'
        self.number_display.setText(number)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())