import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
import numpy as np
import datetime

if __name__ == "__main__":
    movie_data = pd.read_csv("movie_data_2022.csv")
    movie_data["Watch Date"] = pd.to_datetime(movie_data["Watch Date"], format="%d/%m/%Y")
    movie_data["Year of Release"] = pd.to_datetime(movie_data["Year of Release"], format="%Y")
    
    # print(movie_data.dtypes)
    # Plot frequency by month
    #movie_data["Watch Date"].groupby(movie_data["Watch Date"].dt.month).count().plot(kind="bar")
    # plt.show()

    # Plot frequency by Year Made Decade
    year_of_release = movie_data[["Year of Release"]]
    # print(year_of_release)

    decades = np.array([datetime.date(1930,1,1), datetime.date(1940,1,1), datetime.date(1950,1,1), datetime.date(1960,1,1), 
                        datetime.date(1970,1,1), datetime.date(1980,1,1), datetime.date(1990,1,1), datetime.date(2000,1,1), datetime.date(2010,1,1), 
                        datetime.date(2020,1,1)])
    frequencies = np.zeros(decades.size)

    for index, row in year_of_release.iterrows():
        release_years = row['Year of Release']
        
        if release_years >= pd.Timestamp(decades[-1]):
            frequencies[-1] = frequencies[-1] + 1
        else:
            for i in range(decades.size):
                if release_years > pd.Timestamp(decades[i]) and release_years < pd.Timestamp(decades[i+1]):
                    frequencies[i] = frequencies[i] + 1
                    break

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    plot_dates = matplotlib.dates.date2num(decades)
    print(decades)
    print(plot_dates)
    ax.bar(plot_dates,frequencies)
    plt.show()

    # decade_data = year_of_release.resample('10AS', on="Year of Release").sum()
    # print(decade_data)

    # movie_data["Year of Release"].groupby(movie_data["Year of Release"].dt.year).count().plot(kind="bar")
    # plt.show()

