# SuicideRatesDataImputation
## This project is to assign the average suicide rates of adjacent counties to the counties that don't have suicide death record. Here I used 2015 suicide death data 
## that was downloaded from CDC Wonder- Underlying Cause of Death: https://wonder.cdc.gov/ucd-icd10.html

### The county adjacent data is downloaded from Census.gov: 
#### https://www.census.gov/geographies/reference-files/2010/geo/county-adjacency.html#:~:text=The%20county%20adjacency%20file%20lists%20each%20county%2C%20or,Mariana%20Islands%2C%20Guam%2C%20and%20the%20U.S.%20Virgin%20Islands%29.

## Step 1: The original county adjacent file is formatted as following screenshot: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step1.png" alt="County Adjacent File" title="County Adjacent File">

## Step 2: After adding the county information to the adjacent counties: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step2.png" alt="County Adjacent File" title="County Adjacent File">

## Step 3: by using some algorithms, I created a list of county fips of adjacent counties and they are shown in the data frame with a column called Neighbor Code: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step3.png" alt="County Adjacent File" title="County Adjacent File">

## Step 4: The raw suicide death data from CDC wonder is as the following table and about 900 counties have suicide death records every year: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/suicide_15.png" alt="County Adjacent File" title="County Adjacent File">

## Step 5: Use a function to find the average suicide rates of adjacent counties: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step4.png" alt="County Adjacent File" title="County Adjacent File">

## Step 6: With more counties having suicide rates, using the function again to assign the average suicide rates of adjacent counties to the county: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step5.png" alt="County Adjacent File" title="County Adjacent File">

## Step 7: Using the function again: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step6.png" alt="County Adjacent File" title="County Adjacent File">

## Step 8: Using the function again: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step7.png" alt="County Adjacent File" title="County Adjacent File">

## Step 9: After using the function 4 times, more than 3000 counties have suicide rates data already. Using plotly package, the suicide death rates map is as follow: 
<img src="https://github.com/Wenhuan2516/SuicideRatesDataImputation/blob/main/step8.png" alt="County Adjacent File" title="County Adjacent File">

# By replacting the suicide data in different years, we can impute suicide data for other years easily. 
