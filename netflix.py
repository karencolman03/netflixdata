import pandas as pd

df = pd.read_csv('ViewingActivity.csv')
df = df.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df.dtypes

df = df.set_index('Start Time')

df.index = df.index.tz_convert('US/Eastern')

df = df.reset_index()

office = df[df['Title'].str.contains('The Office (U.S.)', regex=False)]

office = office[(office['Duration'] > '0 days 00:01:00')]

office['Duration'].sum()

office['weekday'] = office['Start Time'].dt.weekday

office['hour'] = office['Start Time'].dt.hour

%matplotlib inline
import matplotlib

office['weekday'] = pd.Categorical(office['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)

office_by_day = office['weekday'].value_counts()
office_by_day = office_by_day.sort_index()

matplotlib.rcParams.update({'font.size': 22})

office_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')
