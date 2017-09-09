
# Pyber Ride Sharing Data

## Analysis

-  Observed Trend 1 : Urban market has the highest fare share of approximately 63%

-  Observed Trend 2 : Urban market has the highest ride share of approximately 68.4%

-  Observed Trend 3 : Urban market has the highest driver share of approximately 77.8%


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

cityData = pd.read_csv('raw_data/city_data.csv')
rideData = pd.read_csv('raw_data/ride_data.csv')
typColor = {'Urban':'lightcoral','Suburban':'lightskyblue','Rural':'gold'}
colors = ["gold","lightskyblue","lightcoral"]
explode = (0, 0, 0.1)
```

### Bubble Plot of Ride Sharing Data


```python
df_cityDataFinal = pd.DataFrame({'AverageFare': rideData.groupby('city').fare.mean(),
                   'NoOfRides': rideData.groupby('city').ride_id.nunique(),
                   'DriverCount': cityData.groupby('city').driver_count.sum(),
                    'type': cityData.groupby('city').type.apply(lambda x : ''.join(x.unique()))})
df_cityDataFinal['TotalFare'] = df_cityDataFinal['AverageFare'] * df_cityDataFinal['NoOfRides']
```


```python
df_cityDataFinal.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>AverageFare</th>
      <th>DriverCount</th>
      <th>NoOfRides</th>
      <th>type</th>
      <th>TotalFare</th>
    </tr>
    <tr>
      <th>city</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Alvarezhaven</th>
      <td>23.928710</td>
      <td>21</td>
      <td>31</td>
      <td>Urban</td>
      <td>741.79</td>
    </tr>
    <tr>
      <th>Alyssaberg</th>
      <td>20.609615</td>
      <td>67</td>
      <td>26</td>
      <td>Urban</td>
      <td>535.85</td>
    </tr>
    <tr>
      <th>Anitamouth</th>
      <td>37.315556</td>
      <td>16</td>
      <td>9</td>
      <td>Suburban</td>
      <td>335.84</td>
    </tr>
    <tr>
      <th>Antoniomouth</th>
      <td>23.625000</td>
      <td>21</td>
      <td>22</td>
      <td>Urban</td>
      <td>519.75</td>
    </tr>
    <tr>
      <th>Aprilchester</th>
      <td>21.981579</td>
      <td>49</td>
      <td>19</td>
      <td>Urban</td>
      <td>417.65</td>
    </tr>
  </tbody>
</table>
</div>




```python
plt.figure(figsize=(18,12))
patches11 = [ plt.plot([],[], marker="o", ms=10, ls="", mec="black", mew=0.7, color=list(typColor.values())[i]) [0]  for i in range(len(typColor))]
plt.scatter(x=df_cityDataFinal['NoOfRides'], y=df_cityDataFinal['AverageFare'], s=(df_cityDataFinal['DriverCount']*10), c=df_cityDataFinal['type'].apply(lambda x: typColor[x]), edgecolor="k", linewidth=0.7)
plt.legend(patches11,typColor.keys(),loc="best", frameon=True, edgecolor='black', labelspacing=1, title="City Types")
plt.gca().set(xlabel='Total Number of Rides(Per City)', ylabel='Average Fare($)', title='Pyber Ride Sharing Data(2016)')
plt.show()
```


![png](output_9_0.png)


### Total Fares By City Type


```python
sFare = df_cityDataFinal.groupby('type').TotalFare.sum()
fbct_df = pd.DataFrame(sFare)
plt.pie(fbct_df['TotalFare'], explode=explode, labels=fbct_df.index, colors=colors, autopct="%1.1f%%", shadow=True, startangle=120)
plt.title("% of Total Fares by City Type")
plt.show()
```


![png](output_11_0.png)


### Total Rides By City Type


```python
sRide = df_cityDataFinal.groupby('type').NoOfRides.sum()
rbct = pd.DataFrame(sRide)
plt.pie(rbct['NoOfRides'], explode=explode, labels=rbct.index, colors=colors, autopct="%1.1f%%", shadow=True, startangle=120)
plt.title("% of Total Rides by City Type")
plt.show()
```


![png](output_13_0.png)


### Total Drivers By City Type


```python
sDrivers = df_cityDataFinal.groupby('type').DriverCount.sum()
dbct = pd.DataFrame(sDrivers)
plt.pie(dbct['DriverCount'], explode=explode, labels=dbct.index, colors=colors, autopct="%1.1f%%", shadow=True, startangle=120)
plt.title("% of Total Drivers by City Type")
plt.show()
```


![png](output_15_0.png)

