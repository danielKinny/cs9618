class Lesson:

    def __init__(self, title, duration, req):

        self.__title = title
        self.__duration = duration
        self.__req = req

    def getLessonTitle(self):
        return self.__title
        
    def getLessonDuration(self):
        return self.__duration
        
    def getLabRequired(self):
        return self.__req
    
    def getLessonDetails(self):
        print("The lesson's name is: "+self.getLessonTitle())
        print("The lesson's duration is: ",self.getLessonDuration())
        print(f"Does this require a lab? "+str(self.getLabRequired()))
        

class Assessment:

    def __init__(self, title, max):
        
        self.__assessmentTitle = title
        self.__maxMark = max

    def getAssessmentTitle(self):
        return self.__assessmentTitle

    def getMaxMark(self):
        return self.__maxMark
    
    def getAssessmentDetails(self):
        print("The assessment name is: "+ self.getAssessmentTitle())
        print("The assessment's max mark is: ",self.getMaxMark())
    
class Course:
      
    def __init__(self, title, maxstudents):
            
        self.__courseTitle = title
        self.__maxStudents = maxstudents
        self.__lessonsNumber = 0
        self.__lessons = []
        self.__assessment = None

    def getTitle(self):
        return self.__courseTitle
    
    def getMaxStudents(self):
        return self.__maxStudents
    
    def getLessonsNumber(self):
        return self.__lessonsNumber
    
    def incrementLessonsNumber(self):
        self.__lessonsNumber += 1


    def addLesson(self, lTitle, lDuration, lReq):
        self.__lessons.append(Lesson(lTitle, lDuration, lReq))
        self.incrementLessonsNumber()

    def addAssessment(self, aTitle, aMax):
        self.__assessment = Assessment(aTitle, aMax)

    def outputCourseDetails(self):
        print("-------------------")
        print("This Course's name is: "+self.getTitle())
        print("This Course's max students are: ",self.getMaxStudents())
        print("This Course has",self.getLessonsNumber()," lessons")

        for lesson in self.__lessons:
            lesson.getLessonDetails()

        self.__assessment.getAssessmentDetails()
            
      
#main prog

course = Course("A Level Computer Science",30)

course.addLesson("Python OOP Basics", 60, True)
course.addAssessment("Python Inheritance", 75)

course.outputCourseDetails()