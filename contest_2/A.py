import pandas as pd
import matplotlib.pyplot as plt
import typing as tp
from matplotlib.axes import Axes


class CatExam:
    def __init__(self, path_to_df: str="cat_exam_data.csv"): # task0
      self.df = pd.read_csv(path_to_df)

    def task1(self) -> pd.DataFrame:
      return self.df.head(5)
    
    def task2(self) -> tp.List[str]:
      col = self.df.isna().any()
      res = list()
      for i in range(0, len(col)):
        if (col[i]):
          res.append(self.df.columns[i])
      return res

    def task3(self) -> pd.DataFrame:
      return self.df.dropna()
    
    def task4(self) -> pd.DataFrame:
      return self.task3().describe()
    
    def task5(self) -> int:
      return len(self.task3()[self.task3()['test_score'] == 100])
    
    def task6(self) -> pd.DataFrame:
      new_table = self.task3()[self.task3()['test_score'] == 100]
      new_table = new_table.groupby('school').aggregate({'test_score': 'count', 'number_of_students': 'first'})
      new_table = new_table.reset_index()
      new_table = new_table.rename(columns={'test_score': 'cnt_100'})
      new_table = new_table.sort_values(by = ['cnt_100', 'school'], ascending=[False, False])
      new_table = new_table[['school', 'number_of_students', 'cnt_100']]
      return new_table

    def task7(self) -> pd.DataFrame:
      new_table = self.task3().groupby('school').mean()
      new_table = new_table.reset_index()
      new_table = new_table.sort_values(by = 'test_score', ascending=False)
      return new_table.head(10)
      
    def task8(self) -> pd.DataFrame:
      new_table = self.task3().groupby('school').mean()
      new_table = new_table.reset_index()
      new_table = new_table.sort_values(by = 'test_score', ascending=True)
      return new_table.head(10)

    def task9(self) -> Axes:
      big_schools = self.task3()[self.task3()['number_of_students'] > 1000]
      small_shools = self.task3()[self.task3()['number_of_students'] <= 1000]
      plt.hist(big_schools['test_score'], edgecolor = 'black', bins = 10, alpha=0.5, label='Big schools')
      plt.hist(small_shools['test_score'], edgecolor = 'black', bins = 10, alpha=0.5, label='Small schools')      
      plt.xlabel('Test score')
      plt.ylabel('Number of students')
      plt.title('Test score depending on the size of the school')
      plt.legend() 
      return plt.gca()
