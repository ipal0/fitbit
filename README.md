## Get data from FitBit API and Save to HDF5 file

### Getting Data from Fitbit Web-API
* Go to https://dev.fitbit.com/ and Register an app.
* After registering, open the app details and go to OAuth2.0 Tutorial Page in a new tab:  https://dev.fitbit.com/apps/oauthinteractivetutorial
* In the webpage, copy the app details and click the redirect website link. 
* This will open the redirect web link with all the required string supplied in the address. 
* Copy the link address and paste in the box provided. The box will parse the address and give you the code string. 
* Put the code string in the GetData.py or just use option -c with code string.
### Run GetData.py
* Run the GetData.py. Without any option this will get the data for the previous day. If you specify the starting day, then it will get all the days from starting day to previous day. For every day, it gets two json files, one for heart data and other for activity data. 
## Save to HDF5 File
* After you get all the json files, you can add them to one single HDF5 database file for easy recording and plotting.
* Run the Save2HDF5.py and this will parse all json files and add them to a the database file called fitbit.h5
* After saving the json files to fitbit.h5, move them to a different directory. 
* For plotting and reviewing the data, you can download HDFView from https://support.hdfgroup.org/products/java/hdfview/
## Visualize the data from hdf file.
* Run the Visualize.py and plot the data.
* This collects all the attributes from the hdf file for all dates. 
* This plots the correlation matrix of all attributes.
* This plots all the attributes individually in subplots.
