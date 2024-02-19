# main.py

class StudentsInMLOps:
    def __init__(self):
        self.total_strength = 0
        self.class_name = "MLOps"

    def enrollStudents(self, count):
        """
        Enroll students in the class.

        Parameters:
        - count (int): Number of students to enroll.
        """
        self.total_strength += count

    def dropStudents(self, count):
            """
            Drop students from the class.

            Parameters:
            - count (int): Number of students to drop.
            """
            if count <= self.total_strength:
                self.total_strength -= count
            else:
                raise ValueError("Error: Cannot drop more students than the total strength.")

    def getTotalStrength(self):
        """
        Get the total strength of students in the class.

        Returns:
        - int: Total strength of students.
        """
        return self.total_strength

    def getClassName(self):
        """
        Get the name of the class.

        Returns:
        - str: Name of the class.
        """
        return self.class_name

# Example usage
if __name__ == "__main__":
    mlops_class = StudentsInMLOps()
    mlops_class.enrollStudents(20)
    print(f"Total strength in {mlops_class.getClassName()}: {mlops_class.getTotalStrength()}")

    mlops_class.dropStudents(5)
    print(f"After dropping students, total strength: {mlops_class.getTotalStrength()}")
