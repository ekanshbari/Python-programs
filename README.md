# Python- general information...

Python Applications
Python is known for its general-purpose nature that makes it applicable in almost every domain of software development. 
Python makes its presence in every emerging field. It is the fastest-growing programming language and can develop any application.

Here, we are specifying application areas where Python can be applied.

1) Web Applications -> Django and Pyramid framework(Use for heavy applications),
                       Flask and Bottle (Micro-framework),
                       Plone and Django CMS (Advance Content management)

2) Desktop GUI Applications ->  Tkinter or Tk,
                                wxWidgetM,
                                Kivy (used for writing multitouch applications ),
                                PyQt or Pyside

3) Console-based Application -> Console-based applications run from the command-line or shell. 
These applications are computer program which are used commands to execute. This kind of application was more popular in the old generation of computers. 
Python can develop this kind of application very effectively. It is famous for having REPL, which means the Read-Eval-Print Loop that makes it the 
most suitable language for the command-line applications.Python provides many free library or module which helps to build the command-line apps.
The necessary IO libraries are used to read and write. It helps to parse argument and create console help text out-of-the-box. 
There are also advance libraries that can develop independent console apps.              

4) Software Development ->  SCons is used to build control,
                            Buildbot and Apache Gumps are used for automated continuous compilation and testing,
                            Round or Trac for bug tracking and project management

5) Scientific and Numeric ->    SciPy,
                                Scikit-learn,
                                NumPy,
                                Pandas,
                                Matplotlib  

6) Business Applications
Business Applications differ from standard applications. E-commerce and ERP are an example of a business application. This kind of 
application requires extensively, scalability and readability, and Python provides all these features.

Oddo is an example of the all-in-one Python-based application which offers a range of business applications. Python provides a 
Tryton platform which is used to develop the business application.

7) Audio or Video-based Applications
Python is flexible to perform multiple tasks and can be used to create multimedia applications. Some multimedia applications 
which are made by using Python are TimPlayer, cplay, etc. The few multimedia libraries are given below.

Gstreamer
Pyglet
QT Phonon

8) 3D CAD Applications
The CAD (Computer-aided design) is used to design engineering related architecture. It is used to develop the 3D representation of a part of a system. 
Python can create a 3D CAD application by using the following functionalities.

Fandango (Popular )
CAMVOX
HeeksCNC
AnyCAD
RCAM


9) Enterprise Applications
Python can be used to create applications that can be used within an Enterprise or an Organization. Some real-time applications are OpenERP, Tryton, Picalo, etc.

10) Image Processing Application
Python contains many libraries that are used to work with the image. The image can be manipulated according to our requirements. Some libraries 
of image processing are given below.

OpenCV
Pillow
SimpleITK                                                          

####################################################################################################################################################################

Identifier Naming
Variables are the example of identifiers. An Identifier is used to identify the literals used in the program. The rules to name an identifier are given below.

The first character of the variable must be an alphabet or underscore ( _ ).
All the characters except the first character may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore, or digit (0-9).
Identifier name must not contain any white-space, or special character (!, @, #, %, ^, &, *).
Identifier name must not be similar to any keyword defined in the language.
Identifier names are case sensitive; for example, my name, and MyName is not the same.
Examples of valid identifiers: a123, _n, n_9, etc.
Examples of invalid identifiers: 1a, n%4, n 9, etc.

------------------------------------------------------------------

The multi-word keywords can be created by the following method.

Camel Case - In the camel case, each word or abbreviation in the middle of begins with a capital letter. There is no 
intervention of whitespace. For example - nameOfStudent, valueOfVaraible, etc.
Pascal Case - It is the same as the Camel Case, but here the first word is also capital. For example - NameOfStudent, etc.
Snake Case - In the snake case, Words are separated by the underscore. For example - name_of_student, etc.

------------------------------------------------------------------

1. Assigning single value to multiple variables
x=y=z=50    
print(x)    
print(y)    
print(z)  

Output:
50  
50  
50

2. Assigning multiple values to multiple variables:
a,b,c=5,10,15    
print a    
print b    
print c 

Output:
5  
10  
15 
------------------------------------------------------------------

Python Operators
The operator can be defined as a symbol which is responsible for a particular operation between two operands. Operators are the pillars of a program on which the logic is built in a specific programming language. Python provides a variety of operators, which are described as follows.

Arithmetic operators
Comparison operators
Assignment Operators
Logical Operators
Bitwise Operators
Membership Operators
Identity Operators

Arithmetic Operators
Arithmetic operators are used to perform arithmetic operations between two operands. It includes + (addition), - (subtraction), 
*(multiplication), /(divide), %(reminder), //(floor division), and exponent (**) operators.
Consider the following table for a detailed explanation of arithmetic operators.
Operator	Description
+ (Addition)	It is used to add two operands. For example, if a = 20, b = 10 => a+b = 30
- (Subtraction)	It is used to subtract the second operand from the first operand. If the first operand is less than the second operand, the value results negative. For example, if a = 20, b = 10 => a - b = 10
/ (divide)	It returns the quotient after dividing the first operand by the second operand. For example, if a = 20, b = 10 => a/b = 2.0
* (Multiplication)	It is used to multiply one operand with the other. For example, if a = 20, b = 10 => a * b = 200
% (reminder)	It returns the reminder after dividing the first operand by the second operand. For example, if a = 20, b = 10 => a%b = 0
** (Exponent)	It is an exponent operator represented as it calculates the first operand power to the second operand.
// (Floor division)	It gives the floor value of the quotient produced by dividing the two operands.

Comparison operator
Comparison operators are used to comparing the value of the two operands and returns Boolean true or false accordingly. 
The comparison operators are described in the following table.
Operator	Description
==	If the value of two operands is equal, then the condition becomes true.
!=	If the value of two operands is not equal, then the condition becomes true.
<=	If the first operand is less than or equal to the second operand, then the condition becomes true.
>=	If the first operand is greater than or equal to the second operand, then the condition becomes true.
>	If the first operand is greater than the second operand, then the condition becomes true.
<	If the first operand is less than the second operand, then the condition becomes true.

Assignment Operators
The assignment operators are used to assign the value of the right expression to the left operand. The assignment operators are described in the following table.
Operator	Description
=	It assigns the value of the right expression to the left operand.
+=	It increases the value of the left operand by the value of the right operand and assigns the modified value back to left operand. For example, if a = 10, b = 20 => a+ = b will be equal to a = a+ b and therefore, a = 30.
-=	It decreases the value of the left operand by the value of the right operand and assigns the modified value back to left operand. For example, if a = 20, b = 10 => a- = b will be equal to a = a- b and therefore, a = 10.
*=	It multiplies the value of the left operand by the value of the right operand and assigns the modified value back to then the left operand. For example, if a = 10, b = 20 => a* = b will be equal to a = a* b and therefore, a = 200.
%=	It divides the value of the left operand by the value of the right operand and assigns the reminder back to the left operand. For example, if a = 20, b = 10 => a % = b will be equal to a = a % b and therefore, a = 0.
**=	a**=b will be equal to a=a**b, for example, if a = 4, b =2, a**=b will assign 4**2 = 16 to a.
//=	A//=b will be equal to a = a// b, for example, if a = 4, b = 3, a//=b will assign 4//3 = 1 to a.

Bitwise Operators
The bitwise operators perform bit by bit operation on the values of the two operands. Consider the following example.
Operator	Description
& (binary and)	If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied.
| (binary or)	The resulting bit will be 0 if both the bits are zero; otherwise, the resulting bit will be 1.
^ (binary xor)	The resulting bit will be 1 if both the bits are different; otherwise, the resulting bit will be 0.
~ (negation)	It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa.
<< (left shift)	The left operand value is moved left by the number of bits present in the right operand.
>> (right shift)	The left operand is moved right by the number of bits present in the right operand.

Logical Operators
The logical operators are used primarily in the expression evaluation to make a decision. Python supports the following logical operators.
Operator	Description
and	If both the expression are true, then the condition will be true. If a and b are the two expressions, a → true, b → true => a and b → true.
or	If one of the expressions is true, then the condition will be true. If a and b are the two expressions, a → true, b → false => a or b → true.
not	If an expression a is true, then not (a) will be false and vice versa.

Membership Operators
Python membership operators are used to check the membership of value inside a Python data structure. If the value is 
present in the data structure, then the resulting value is true otherwise it returns false.
Operator	Description
in	It is evaluated to be true if the first operand is found in the second operand (list, tuple, or dictionary).
not in	It is evaluated to be true if the first operand is not found in the second operand (list, tuple, or dictionary).


Identity Operators
The identity operators are used to decide whether an element certain class or type.
Operator	Description
is	It is evaluated to be true if the reference present at both sides point to the same object.
is not	It is evaluated to be true if the reference present at both sides do not point to the same object.


Operator Precedence
The precedence of the operators is essential to find out since it enables us to know which operator should be evaluated first. The precedence table of the operators in Python is given below.
Operator	Description
**	The exponent operator is given priority over all the others used in the expression.
~ + -	The negation, unary plus, and minus.
* / % //	The multiplication, divide, modules, reminder, and floor division.
+ -	Binary plus, and minus
>> <<	Left shift. and right shift
&	Binary and.
^ |	Binary xor, and or
<= < > >=	Comparison operators (less than, less than equal to, greater than, greater then equal to).
<> == !=	Equality operators.
= %= /= //= -= +=
*= **=	Assignment operators
is is not	Identity operators
in not in	Membership operators
not or and	Logical operators

------------------------------------------------------------------
































