# Dark Index (DIX) calculated with Python  
  
This is a simple script that automates getting the daily DIX.  This pulls data from FINRA's API for the last trading day and then sums short volume, total volume, and divides short/total to calculate the DIX.  All that is needed is to set up FINRA API credentials and replace the file path in the script with the location of the credentials.  Credentials can be set up in the [FINRA console](https://gateway.finra.org/app/dfo-console).  
  
Read more about the DIX in the paper by squeezemetrics [here](https://squeezemetrics.com/monitor/download/pdf/short_is_long.pdf).  
   
In summary, high DIX has historically been bullish due to high short volume (as % of total volume) typically being a result of high buying volume.  This somewhat counterintuitive result is due to how MM's provide liquidity. 