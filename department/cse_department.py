class CSE:
    def __init__(self):
        """
        Initializes Department
        """
        pass

    def number_of_students(self):
        """

        :rtype: int
        :return: int number
        """
        return 40

    def number_of_professors(self):
        """
        
        :return: int number 
        """
        return 20

    def professors_to_student_ratio(self):
        print('Ratio:', int(self.number_of_students())/int(self.number_of_professors()))