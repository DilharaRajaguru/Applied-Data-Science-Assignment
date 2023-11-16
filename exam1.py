# -*- coding: utf-8 -*-
"""
Spyder Dilhara

This is a temporary script file."""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Read the excel file
#Data in Exam result from 2014 to 2018
df_exam = pd.read_excel("examinfo.xlsx")
print(df_exam)

#plot line chart using above data frame
def plot_line():
    
    #plot the line chart
    plt.figure()
    plt.plot(df_exam['Year'], df_exam['AQA'], label='AQA')
    plt.plot(df_exam['Year'], df_exam['Pearson'], label='Pearson')
    plt.plot(df_exam['Year'], df_exam['OCR'], label='OCR')
    plt.plot(df_exam['Year'], df_exam['WJEC'], label='WJEC')
    plt.plot(df_exam['Year'], df_exam['CCEA'], label='CCEA')

    plt.xlabel('Year')
    plt.ylabel('Exam')
    plt.xticks([2014, 2015, 2016, 2017, 2018])
    plt.title('Examination result analysis of 2014 - 2018')
    plt.legend()

    plt.savefig('line_chart.png')
    plt.show()

#call the function
plot_line()

#plot bar chart using data frame
def plot_bar ():
    df = df_exam.iloc[0:5]           
    plt.figure()
    plt.bar(df['Year'], df['AQA'], linewidth=100000000)
    plt.xlabel('Year')
    plt.ylabel('Exam Result')
    plt.xticks([2014, 2015, 2016, 2017, 2018])
    plt.yticks([0])
    plt.title('Examination result analysis of 2014 - 2018')
    plt.legend()
    
    plt.savefig('line_chart.png')
    plt.show()
    
#call line chart
plot_bar()

#plot pie chart
def plot_pie():
    
    
    plt.figure()
    plot = df_exam.groupby(['Year']).sum().plot.pie(y='Total', autopct='%1.0f%%', figsize=(10,10))
    plt.title('Examination result analysis of 2014 - 2018')
    plt.legend()
    
    plt.savefig('line_chart.png')
    plt.show()
    
    plt.figure()
    plot = df_exam.groupby(['Year']).sum().plot.pie(y='AQA', autopct='%1.0f%%', figsize=(10,10))
    plt.title('AQA Examination result analysis of 2014 - 2018')
    plt.legend()
    
    plt.savefig('line_chart.png')
    plt.show()
    
#call function plot_pie
plot_pie()