class StudentException(Exception):
    def __init__(self):
        pass

    def student_not_found(self):
        print('Student Not Found.')

    def professor_not_found(self):
        print('Professor Not Found.')