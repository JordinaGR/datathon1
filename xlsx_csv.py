import pandas as pd 
  
read_file = pd.read_excel ("/home/jordina/Desktop/datathon/Datathon_Students_enrolled_in_bachelors_and_masters_degrees_22-23_place_of_residence_course_V2.xlsx") 

read_file.to_csv ("dades2.csv",  index = None, header=True) 