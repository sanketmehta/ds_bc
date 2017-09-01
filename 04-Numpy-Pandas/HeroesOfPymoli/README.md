
# Heroes of Pymoli Data Analysis

- OBSERVED TREND 1 : Male players dominate the user base with more than 80% of the total players. 

- OBSERVED TREND 2 : Players in the age group 'Between 20 & 25' are highest consumer group.

- OBSERVED TREND 3 : Players in the age group '40+' spend maximum Dollars per head, but currently account for lowest % share of all consumer age-groups.


```python
import pandas as pd
import numpy as np
import os

purchaseDataFile = os.path.join("raw_data","purchase_data.json")
purchase = pd.read_json(purchaseDataFile)
purchaseData = purchase
```

### Player Count


```python
totPlayers = purchaseData['SN'].nunique()
totPlayers_df = pd.DataFrame({'Total Players': totPlayers}, index=list(range(1)))
totPlayers_df
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
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>573</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Total)


```python
noOfUnqItems = purchaseData['Item Name'].nunique()
avgPrice = purchaseData['Price'].sum() / purchaseData['Item Name'].count()
noOfPurchases = purchaseData['Item Name'].count()
totRevenue = purchaseData['Price'].sum()
purAnalysis_df = pd.DataFrame({'Number Of Unique Items': noOfUnqItems,
                   'Average Price': avgPrice,
                   'Number of Purchases': noOfPurchases,
                   'Total Revenue': totRevenue},
                   index=list(range(1)))
purAnalysis_df['Average Price'] = purAnalysis_df['Average Price'].map('${:,.2f}'.format) 
purAnalysis_df['Total Revenue'] = purAnalysis_df['Total Revenue'].map('${:,.2f}'.format) 
purAnalysis_df = purAnalysis_df[['Number Of Unique Items', 'Average Price', 'Number of Purchases', 'Total Revenue']]
purAnalysis_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        font-family: "Courier New", Georgia, Serif;
        font-style: italic;
        text-align: right;
        font-size: 2px;
    }

    .dataframe thead th {
        font-family: "Courier New", Georgia, Serif;
        font-style: italic;
        text-align: left;
        font-size: 2px;
    }

    .dataframe tbody tr th {
        font-family: "Courier New", Georgia, Serif;
        font-style: italic;
        vertical-align: top;
        font-size: 2px;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number Of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2,286.33</td>
    </tr>
  </tbody>
</table>
</div>



### Gender Demographics


```python
genDemographics_df = pd.DataFrame(purchaseData.groupby('Gender').SN.nunique())
genDemographics_df.columns = [['Total Count']]
genDemographics_df.index.name = ''
genDemographics_df['Percentage of Players'] = round(((genDemographics_df['Total Count'] / totPlayers) * 100),2)
genDemographics_df = genDemographics_df[['Percentage of Players','Total Count']]
genDemographics_df.sort_values(by=['Total Count'], ascending=False)
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
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15</td>
      <td>465</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.40</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Gender)


```python
pd.DataFrame(purchaseData.groupby('Gender').SN.nunique())
pd.DataFrame(purchaseData.groupby('Gender').Price.sum())
pd.DataFrame(purchaseData.groupby('Gender').Price.mean())

purAnaByGen_df = pd.DataFrame({'Purchase Count': purchaseData.groupby('Gender').SN.nunique(),
                   'Average Purchase Price': purchaseData.groupby('Gender').Price.mean(),
                   'Total Purchase Value': purchaseData.groupby('Gender').Price.sum()})
purAnaByGen_df['Normalized Totals'] = purAnaByGen_df['Total Purchase Value'] / purAnaByGen_df['Purchase Count']
purAnaByGen_df['Average Purchase Price'] = purAnaByGen_df['Average Purchase Price'].map('${:,.2f}'.format) 
purAnaByGen_df['Total Purchase Value'] = purAnaByGen_df['Total Purchase Value'].map('${:,.2f}'.format) 
purAnaByGen_df['Normalized Totals'] = purAnaByGen_df['Normalized Totals'].map('${:,.2f}'.format) 
purAnaByGen_df = purAnaByGen_df[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value', 'Normalized Totals']]
purAnaByGen_df
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>100</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$3.83</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>465</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$4.02</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>8</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$4.47</td>
    </tr>
  </tbody>
</table>
</div>



### Age Demographies


```python
bins = [0,9,14,19,24,29,34,39,(purchaseData['Age'].max() + 1)]
group_names = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
ageGroup_df = purchaseData
ageGroup_df['AgeGroup'] = pd.cut(ageGroup_df['Age'], bins, labels=group_names)
ageDemographics_df = pd.DataFrame({'Total Count' : ageGroup_df.groupby('AgeGroup').SN.nunique()})
ageDemographics_df = ageDemographics_df.reindex(index=group_names)
ageDemographics_df['Percentage Of Players'] = round(((ageDemographics_df['Total Count'] / totPlayers) * 100),2)
ageDemographics_df = ageDemographics_df[['Percentage Of Players','Total Count']]
ageDemographics_df.index.name = ''
ageDemographics_df
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
      <th>Percentage Of Players</th>
      <th>Total Count</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.32</td>
      <td>19</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>4.01</td>
      <td>23</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.45</td>
      <td>100</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>45.20</td>
      <td>259</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>15.18</td>
      <td>87</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.20</td>
      <td>47</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.71</td>
      <td>27</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>1.92</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>



### Purchasing Analysis (Age)


```python
purAnaByAge_df = pd.DataFrame({'Purchase Count' : ageGroup_df.groupby('AgeGroup').SN.nunique(), 
                     'Average Purchase Price': ageGroup_df.groupby('AgeGroup').Price.mean(),
                    'Total Purchase Value': ageGroup_df.groupby('AgeGroup').Price.sum(),
                    'User Count': ageGroup_df.groupby('AgeGroup').SN.count()})
purAnaByAge_df = purAnaByAge_df.reindex(index=group_names)
purAnaByAge_df['Normalized Totals'] = purAnaByAge_df['Total Purchase Value'] / purAnaByAge_df['Purchase Count']
purAnaByAge_df = purAnaByAge_df[['Purchase Count', 'Average Purchase Price', 'Total Purchase Value', 'Normalized Totals']]
purAnaByAge_df['Average Purchase Price'] = purAnaByAge_df['Average Purchase Price'].map('${:,.2f}'.format) 
purAnaByAge_df['Total Purchase Value'] = purAnaByAge_df['Total Purchase Value'].map('${:,.2f}'.format) 
purAnaByAge_df['Normalized Totals'] = purAnaByAge_df['Normalized Totals'].map('${:,.2f}'.format) 
purAnaByAge_df.index.name = ''
purAnaByAge_df
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>19</td>
      <td>$2.98</td>
      <td>$83.46</td>
      <td>$4.39</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>23</td>
      <td>$2.77</td>
      <td>$96.95</td>
      <td>$4.22</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>100</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$3.86</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>259</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$3.78</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>87</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$4.26</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>47</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$4.20</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>27</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$4.42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>11</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$4.89</td>
    </tr>
  </tbody>
</table>
</div>



### Top Spenders


```python
topSpenders_df = pd.DataFrame({'Total Purchase Value': purchaseData.groupby('SN').Price.sum(),
                    'Average Purchase Price': purchaseData.groupby('SN').Price.mean(),
                    'Purchase Count': purchaseData.groupby('SN').Price.count()})
topSpenders_df = topSpenders_df[['Purchase Count','Average Purchase Price','Total Purchase Value']]
topSpenders_df = topSpenders_df.sort_values('Total Purchase Value', ascending=False).head()
topSpenders_df['Average Purchase Price'] = topSpenders_df['Average Purchase Price'].map('${:,.2f}'.format) 
topSpenders_df['Total Purchase Value'] = topSpenders_df['Total Purchase Value'].map('${:,.2f}'.format) 
topSpenders_df
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
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$3.41</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$3.39</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$3.18</td>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>3</td>
      <td>$4.24</td>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>3</td>
      <td>$3.86</td>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>



### Most Popular Items


```python
items_df = pd.DataFrame({'Purchase Count': purchaseData.groupby(['Item ID','Item Name']).Price.count(),
                    'Item Price': purchaseData.groupby(['Item ID','Item Name']).Price.mean(),
                    'Total Purchase Value': purchaseData.groupby(['Item ID','Item Name']).Price.sum()})
items_df = items_df[['Purchase Count','Item Price','Total Purchase Value']]
popItems_df = items_df.sort_values(['Purchase Count','Total Purchase Value'], ascending=False).head()
popItems_df['Item Price'] = popItems_df['Item Price'].map('${:,.2f}'.format) 
popItems_df['Total Purchase Value'] = popItems_df['Total Purchase Value'].map('${:,.2f}'.format) 
popItems_df
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
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>11</td>
      <td>$2.23</td>
      <td>$24.53</td>
    </tr>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>9</td>
      <td>$2.07</td>
      <td>$18.63</td>
    </tr>
    <tr>
      <th>13</th>
      <th>Serenity</th>
      <td>9</td>
      <td>$1.49</td>
      <td>$13.41</td>
    </tr>
  </tbody>
</table>
</div>



### Most Profitable Items


```python
profItems_df = items_df.sort_values(['Total Purchase Value','Purchase Count','Item Price'], ascending=False).head()
profItems_df['Item Price'] = profItems_df['Item Price'].map('${:,.2f}'.format) 
profItems_df['Total Purchase Value'] = profItems_df['Total Purchase Value'].map('${:,.2f}'.format) 
profItems_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        font-family: "Courier New", Georgia, Serif;
        font-style: italic;
        font-size: 2px;
        text-align: right;
    }

    .dataframe thead th {
        font-family: "Courier New", Georgia, Serif;
        font-style: italic;
        font-size: 2px;
        text-align: left;
    }

    .dataframe tbody tr th {
        font-family: "Courier New", Georgia, Serif;
        font-style: italic;
        font-size: 2px;
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>103</th>
      <th>Singed Scalpel</th>
      <td>6</td>
      <td>$4.87</td>
      <td>$29.22</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>8</td>
      <td>$3.61</td>
      <td>$28.88</td>
    </tr>
  </tbody>
</table>
</div>


