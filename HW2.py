# HW2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.


# Static ( class ) variable in StudentAccount is created outside the initializer .
# Private variables in Person and Staff uses double underscore notation and " cannct " be accessed outside the class .
# For str and repr ... :
#         1) define __str__ to return the correct string (for some you can copy it out of the doctest and insert the values )
#         2)  __repr __= __str__( with the same indentation level as all the function headers) >>alreaady provided 




import random

class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''
    #takes in 3 parameters. cid = represents a course name; cname=title of course; credits=is the number(intetger) of credits for each course
    #makes a callable string and makes use of == method 
    # returns a summary of course with its name and 3 or boolean whether a course being passed through is the same as previous

    def __init__(self, cid, cname, credits):
        self.cid=cid
        self.cname=cname
        self.credits=credits        
        


    def __str__(self):
        cred=str(self.credits)
        return f'{self.cid}({cred}): {self.cname}'

    __repr__ = __str__

    def __eq__(self, other):
        if self.cid==other:
            return True 
        else: 
            return False 



class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.courseOfferings
        {}
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming, 'CMPSC 360': CMPSC 360(3): Discrete Mathematics for Computer Science}
        >>> C.removeCourse('CMPSC 360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC 132': CMPSC 132(3): Programming and Computation II, 'MATH 230': MATH 230(4): Calculus and Vector Analysis, 'PHYS 213': PHYS 213(2): General Physics, 'CMPEN 270': CMPEN 270(4): Digital Design, 'CMPSC 311': CMPSC 311(3): Introduction to Systems Programming}
        >>> isinstance(C.courseOfferings['CMPSC 132'], Course)
        True
    '''

    def __init__(self):
        self.courseOfferings={}
        #takes in the same parameter from Course class
        #add to dictionary in init function
        #returns an indication of the success of adding the course to dictionary 
    def addCourse(self, cid, cname, credits):
        if cid not in self.courseOfferings:
            temp=Course(cid,cname,credits)
            self.courseOfferings[cid]=temp
            return f'Course added successfully'
        else: 
            return f'Course already added'

    #only takes in one parameter which is the course id or the key of dictionary
    #removes key from dictionary
    #returns condition of success of operation
    def removeCourse(self, cid):
        if cid in self.courseOfferings:
            del(self.courseOfferings[cid])
            return f'Course removed successfully'
        else:
            return f'Course not found'


    #takes in a csv file 
    #reads file and adds contents to dictionary
    #returns nothing 
    def _loadCatalog(self, file):
        with open(file, "r") as f:
            course_info = f.read()
        lst=course_info.split("\n")
        temp=[]
        for i in range(len(lst)):
            temp.append(lst[i].split(','))

        for i in range(len(temp)):
            self.addCourse(temp[i][0],temp[i][1],temp[i][2])



class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC 131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC 132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> spr22 = Semester()
        >>> spr22
        No courses
        >>> spr22.addCourse(cmpsc132)
        >>> isinstance(spr22.courses['CMPSC 132'], Course)
        True
        >>> spr22.addCourse(math230)
        >>> spr22
        CMPSC 132; MATH 230
        >>> spr22.isFullTime
        False
        >>> spr22.totalCredits
        7
        >>> spr22.addCourse(phys213)
        >>> spr22.addCourse(econ102)
        >>> spr22.addCourse(econ102)
        'Course already added'
        >>> spr22.addCourse(phil119)
        >>> spr22.isFullTime
        True
        >>> spr22.dropCourse(phil119)
        >>> spr22.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> spr22.totalCredits
        16
        >>> spr22.dropCourse(cmpsc131)
        'No such course'
        >>> spr22.courses
        {'CMPSC 132': CMPSC 132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''


    def __init__(self):
        self.courses={}

    #no parameters
    #makes a string of a summary of all cid(keys) of dictionary 
    #returns a string 
    def __str__(self):
        lst=[]
        for key in self.courses:
            lst+=[key]
        if len(lst)==0:
            return f'No courses'
        else:
            course_sum="; ".join(lst)
            return course_sum

    __repr__ = __str__

    #takes in a Course object 
    #adds a course details to dictionary
    #returns an updated course dictionary
    def addCourse(self, course):
        if isinstance(course,Course):
            if course.cid in self.courses:
                return "Course already added"
            else:
                self.courses[course.cid]=course
                print(self.courses)

    #takes in a Course object 
    #removes a key from dictionary
    #returns updated dictionary 
    def dropCourse(self, course):
        if isinstance(course,Course):
            if course.cid not in self.courses:
                return f'No such course'
            else:
                del(self.courses[course.cid])

    #no parameters
    #counts all the credits 
    #returns an integer of all credits  
    @property
    def totalCredits(self):
        total_cred=0
        for i in self.courses:
            total_cred+=self.courses[i].credits
        return total_cred

    #no parameter
    #determines a students status by their credits
    #returns boolean: True for 12 more credits or False for less than 12
    @property
    def isFullTime(self):
        if self.totalCredits>=12:
            return True
        else:
            return False

    
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    

    def __init__(self, amount):
        self.amount=amount
        self.loan_id=self.__getloanID

    #no parameters
    #creates callable string of balance of a student's account
    #returns a string 
    def __str__(self):
        return f'Balance: ${self.amount}'

    __repr__ = __str__
    #no parameter
    #finds a random number from 10,000 to 99,999 to represent a student's loan
    #returns random number to self.loan_id
    @property
    def __getloanID(self):
        return random.randrange(10000,99999)



class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''

    def __init__(self, name, ssn):
        self.name=name
        self.__ssn=ssn
    
    #no parameters
    #creates a callable string about a person's personal details
    #returns a string
    def __str__(self):
        lst_four=self.get_ssn()[7:]
        return f'Person({self.name}, ***-**-{lst_four})'
    __repr__ = __str__

    #no parameters
    #it is a getter function used to find a private class attribute
    #returns interger
    def get_ssn(self):
        return self.__ssn
    #takes in another person's details(another Person object)
    #compares their ssn numbers
    #returns boolean: True for same and False for different
    def __eq__(self, other):
        if self.__ssn == other.get_ssn():
            return True
        else:
            return False



class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC 132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC 360', C)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC 132}
    '''
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name,ssn)
        self.__supervisor=supervisor

    #no parameters
    #creates a callable string about a staff person's info
    #return a string 
    def __str__(self):
        return f'Staff({self.name}, {self.id})'
    __repr__ = __str__

    #no parameters
    #finds a person's initials and their last 4 ssn numbers
    #returns a string starting with 905 and followed by initials and last 4 ssn numbers
    @property
    def id(self):
        temp=self.name.split()
        temp2=""
        for i in temp:
            temp2+=i[0]
        initials=temp2.lower()
        lst_four=self.get_ssn()[7:]
        return f'905{initials}{lst_four}'
    #no parameters
    #getter fucntion for private Staff atribute 
    #returns private value 
    @property   
    def getSupervisor(self):
        return self.__supervisor

    #takes in a Staff object
    #sets new staff person to class
    # returns string about status of function execution
    def setSupervisor(self, new_supervisor):
        if isinstance(new_supervisor,Staff):
            self.__supervisor=new_supervisor
            return f'Completed!'
        else:
            return None
    
    #takes in a Student object
    #applies a boolean to student's hold atribute
    #returns status of functions execution
    def applyHold(self, student):
        if isinstance(student,Student):
            student.hold=True
            return f'Completed!'
        else:
            return None

    #takes in a Student object
    #applies a boolean to student's hold atribute
    #returns status of functions execution
    def removeHold(self, student):
        if isinstance(student,Student):
            student.hold=False
            return f'Completed!'
        else:
            return None

    #takes in a Student object
    #applies a boolean to student's active atribute
    #returns status of functions execution
    def unenrollStudent(self, student):
        if isinstance(student,Student):
            student.active=False
            return f'Completed!'
        else:
            return None
    #takes in a Person object
    #creates a new student object
    #returns Student object 
    def createStudent(self, person):
        if isinstance(person,Person):
            new=Student(person.name,self.get_ssn(),"Freshman")
            return new





class Student(Person):
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC 465', C)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132; CMPSC 360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC 360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC 360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC 132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: No courses}
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC 132, 2: CMPSC 360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)
        >>> s1.classCode
        'Sophomore'
    '''
    def __init__(self, name, ssn, year):
        random.seed(1)
        super().__init__(name,ssn)
        self.classCode=year
        self.semesters={}
        self.hold=False
        self.active=True
        self.account=self.__createStudentAccount()

    #no parameters
    #creates a summary of student's information
    #returns string 
    def __str__(self):
        return f'Student({self.name}, {self.id}, {self.classCode})'

    __repr__ = __str__

    #no parameters
    #meaks a StudentAccount object
    #returns StudentAccount object based on student's active status 
    def __createStudentAccount(self):
        if self.active==True:
            return StudentAccount(self)
        else:
            return None
    
    #no parameters
    #finds a person's initials and their last 4 ssn numbers
    #returns a string of initials and last 4 ssn numbers
    @property
    def id(self):
        temp=self.name.split()
        temp2=""
        for i in temp:
            temp2+=i[0]
        initials=temp2.lower()
        lst_four=self.get_ssn()[7:]
        return f'{initials}{lst_four}'
 
    #no parameters
    #creates a Semester object to be added to dictionary
    #returns updated dictionary 
    def registerSemester(self):
        if self.active==False or self.hold==True:
            return f'Unsucessful operation'
        else:
            self.semesters[len(self.semesters)+1]=Semester()
            if len(self.semesters)<=2:
                self.classCode='Freshman'
            elif len(self.semesters)>2 and len(self.semesters)<=4:
                self.classCode='Sophomore'
            elif len(self.semesters)>4 and len(self.semesters)<=6:
                self.classCode='Junior'
            else:
                self.classCode='Senior'


    #takes in 2 parameters: course id and Catalog object 
    #adds class to dictionary with keys as number of which semester
    #charges(adds to balance) student account 
    #returns indications to what happened to course id 
    def enrollCourse(self, cid, catalog):
        if self.active==False or self.hold==True:
            return f'Unsuccessful operation'
        
        elif isinstance(catalog,Catalog):
            courses=catalog.courseOfferings

        if cid in self.semesters.values():
            self.semesters[len(self.semesters)].addCourse[courses[cid]]
            self.account.balance+=(self.account.CREDIT_PRICE*int(courses[cid].credits))
            return f'Course added successfully'
        elif cid in self.semesters:
            return f'Course already enrolled'
        else:
            return f'Course not found'


    #takes in a course id
    #removes key(course) from dictionary 
    #removes half of value of course from student account balance 
    #returns indications for status of function execution
    def dropCourse(self, cid):
        if self.active==False or self.hold==True:
            return f'Unsuccessful operation'
        
        for key in self.semesters:
            if key == cid:
                del(self.semesters[key])
                self.account.balance+=(self.account.CREDIT_PRICE*int(key.credits))
                return f'Course dropped successfully'
            else:
                return f'Course not found'
        
    #takes in a integer
    #creates a Loan object to be added to student's account loan dictionary
    #returns indication of execution of function 
    def getLoan(self, amount):
        new=Loan(amount)
        if self.active==False:
            return f'Unsuccessful Operation'
        elif len(self.semesters)==0:
            return f'Not full-time'
        
        if new.loan_id not in self.account.loans:
            self.account.loans[new.loan_id]=amount
        else:
            self.account.loans[new.loan_id]+=amount






class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C._loadCatalog("cmpsc_catalog_small.csv")
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC 360', C)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN 270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC 132', C)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN 270', C)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''
    
    def __init__(self, student):
        self.student=student
        self.balance=0
        self.loans={}
        self.CREDIT_PRICE=1000


    #no parameter
    #creates a string with student info
    #returns a string 
    def __str__(self):
        return f'Name: {self.student.name} \nID: {self.student.id} \nBalance: ${self.balance}'

    __repr__ = __str__

    #takes in an integer 
    #subracts from balance of student balance
    #returns updated balance 
    def makePayment(self, amount):
        for key in self.loans:
            self.loans[key]-=amount
        self.balance-=amount
        return self.balance

    #takes in an integer 
    #adds amount to balance
    #returns updated balance 
    def chargeAccount(self, amount):
        for key in self.loans:
            self.loans[key]+=amount
        self.balance+=amount
        return self.balance



if __name__=='__main__':
    import doctest
    doctest.testmod()  # OR
    doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True) # replace Course for the class name you want to test