This project is aimed at simplifying the grading process optimiziting the time taken to grade the assesments and increasing the accuracy to more than 50%.
The idea of this project is to automatically grade the answers provided by the students to the questions provided using machine learning algorithms and store the results along with the details of the students in the firebase database.
The Dataset_collector.py is a python code which collects the anwers from the students by providing a localhost website (a html template is created with questions being mentioned beforehand).
GivvVal.py code when executed checks and grades the answers based on the model answers and keywords provided in the database and stores the result in the database.
