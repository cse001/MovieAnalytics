import pandas as pd
import os
import seaborn as sns
import math
from matplotlib import pyplot as plt
##################################################################
######                Data Cleaning Functions               ######
##################################################################
############# Clean The Year
def cleanYear(year):
    length = len(str(year))
    if length > 4:
        year = year[0:4]
    if length < 4:
        year = 9999
    return year
############# Clean The Time
def cleanTime(strTime):
    if isinstance(strTime,float):
        if math.isnan(strTime):
            strTime = -1
    else:
        if isinstance(strTime,int):
            strTime = strTime
        else:
            strTime = strTime.replace("min","")
            strTime.strip()
    return strTime
############# Clean the Gross values to remove the $ and M
def cleanGross(gross):
    if isinstance(gross,float):
        gross =gross
    else:
        if isinstance(gross,int):
            print (gross)
        else:
            if gross[-1] == 'M':
                gross = gross[2:len(gross)-1]
    return gross
############# Clean the Genre to take only the first value as the prominent genre
def cleanGenre(genre):
    genre = genre.split(',')
    genre = genre[0]
    return genre
############# Clean the
def cleanCritic(rating):
    if isinstance(rating,float):
        if math.isnan(rating):
            rating = -1
        else:
            rating = math.floor(rating)
    return rating

def getData():
    ##################################################################
    ######                Reading The Data                      ######
    ##################################################################
    module_dir = os.path.dirname(__file__)
    file_path = os.path.join(module_dir, 'dataset.xls')
    # df = pd.read_excel(file_path)
    dataMoviesFull = pd.read_excel(file_path)
    dataMoviesFull.rename(columns={'Movie name':'MovieName'},inplace=True)
    dataMoviesFull.rename(columns={'Metascore':'CriticRating'},inplace=True)
    dataMoviesFull.rename(columns={'Rating':'PublicRating'},inplace=True)
    dataMoviesFull.rename(columns={'Gross':'GrossMillions'},inplace=True)
    # print (dataMoviesFull.head().MovieName)
    ##################################################################
    ######                 Data Cleaning                        ######
    ##################################################################

    ############# Apply Modification to the data
    dataMoviesFull.Year = dataMoviesFull.Year.apply(cleanYear)
    dataMoviesFull.Runtime = dataMoviesFull.Runtime.apply(cleanTime)
    dataMoviesFull.Genre = dataMoviesFull.Genre.apply(cleanGenre)
    dataMoviesFull.GrossMillions = dataMoviesFull.GrossMillions.apply(cleanGross)
    dataMoviesFull.CriticRating = dataMoviesFull.CriticRating.apply(cleanCritic)
    ############# Set the type of data that is to be handled
    dataMoviesFull.MovieName = dataMoviesFull.MovieName.astype('object')
    dataMoviesFull.CriticRating = dataMoviesFull.CriticRating.astype('int64')
    dataMoviesFull.Year = dataMoviesFull.Year.astype('int64')
    dataMoviesFull.Genre = dataMoviesFull.Genre.astype('category')
    dataMoviesFull.Runtime = dataMoviesFull.Runtime.astype('int64')
    dataMoviesFull.GrossMillions = dataMoviesFull.GrossMillions.astype('float64')
    return dataMoviesFull.copy()
    ############# Drop useless columns
    # columns = dataMoviesFull.columns.tolist()
    # print (columns)
    # naCount = dataMoviesFull.isna().sum()
    # for col in columns:
    #     if naCount[col] <len(dataMoviesFull)//10:
    #         print ("Good Data " + col)
    #     else:
    #         # del dataMoviesFull[col]
    #         print ("Bad Data " + col + " "+ str(naCount[col]) )
    # columns = dataMoviesFull.columns.tolist()
    # print (columns)
    ##################################################################
    ######                Some Analytics                        ######
    ##################################################################
    # dataMoviesFullCritic = dataMoviesFull.loc[dataMoviesFull.CriticRating > -1]
    # ar1 = sns.jointplot(data=dataMoviesFullCritic, x='CriticRating', y='PublicRating')
    # ar1.savefig("1.png")
    # ar1 = sns.jointplot(data=dataMoviesFullCritic, x='CriticRating', y='PublicRating', kind='hex')
    # ar1.savefig("2.png")
    # ar1 = sns.jointplot(data=dataMoviesFull, y='PublicRating', x='Runtime')
    # ar1.savefig("3.png")
    # ar1 =sns.jointplot(data=dataMoviesFullCritic, y='CriticRating', x='Runtime')
    # ar1.savefig("4.png")
    # ar1 = sns.jointplot(data=dataMoviesFull, y='GrossMillions', x='PublicRating')
    # ar1.savefig("5.png")
    # ar1 =sns.jointplot(data=dataMoviesFullCritic, x='CriticRating', y='GrossMillions')
    # ar1.savefig("6.png")
    # # sns.jointplot(data=dataMoviesFull, x='PublicRating', y='Vote')
    # # ar1.savefig("1.png")
    # ar1 =sns.jointplot(data=dataMoviesFull, x='Runtime', y='GrossMillions')
    # ar1.savefig("7.png")
    # return
    # print ("Lets get is NA ")
    # print (dataMoviesFull.isna().sum())
    # df = dataMoviesFull[pd.notnull(dataMoviesFull['GrossMillions'])].copy()
    # print (len(df))
    # gr= sns.jointplot(data=df, x='Rating', y='Year')
    # gr.savefig("avc.png")
    # plt.show()
    # df.GrossMillions = df.GrossMillions.apply(cleanGross)
    # df.GrossMillions = df.GrossMillions.astype('float64')
    # print (df.head())
    # print (max(df.GrossMillions))
    # df.assign(var1=df['var1'].str.split(',')).explode('var1')
    # print (df.groupby('Genre').count())
    # pf = df.groupby('Genre')
    # df.assign(Gross=df['Gross'].astype('str').str.split(','))
    # print (df.nlargest(10,['GrossMillions']))
    # print (df.nlargest(10,['PublicRating']))
    # print (df.describe())
    # print (dataMoviesFull.head())
    # print (dataMoviesFull.info())
    # print (dataMoviesFull.Genre.cat.categories)
getData()
