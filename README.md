# Student Class Statistics
This Python code calculates and compares the average statistics of students in two schools, School A and School B. The statistics include age, height, and weight. The code utilizes the **statistics** module to compute the mean values.
## Code Explanation
1. The code begins by importing the necessary **mean** function from the **statistics** module.
2. The **School** class is defined, representing a school with student data.
3. The __init__ method initializes the class and prompts the user to input the number of students **(n)** in the school, as well as their ages, heights, and weights. The input values are stored in respective lists.
4. The miangin_kardan method calculates and prints the mean values of age, height, and weight for the students in the school using the mean function.
5. The get_student_count method returns the number of students in the school.
6. Instances of the School class, A and B, are created, and their respective statistics are computed and displayed.
7. The code compares the mean height of students in schools A and B. If the mean height of school A is greater than school B, it prints 'A'. If it is less, it prints 'B'. If the mean heights are equal, it compares the mean weights of the schools using a similar approach.
8. Finally, the code prints the number of students in school A and school B using the get_student_count method.
## Usage
1. Run the code.
2. Enter the number of students in school A.
3. Provide the age, height, and weight for each student in school A.
4. Repeat steps 2 and 3 for school B.
5. The code will display the mean statistics for each school and compare their heights and weights, determining which school has a higher average. It will also show the number of students in each school.

