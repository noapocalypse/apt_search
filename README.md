# apt_search
Simple check to return all APT groups their techniques and sectors based on a string search

Based on the collated works on APT groups by Thai cert, found here;
https://www.dropbox.com/s/ds0ra0c8odwsv3m/Threat%20Group%20Cards.pdf

Really basic search tool. String matches by sector, apt name ot technique and returns a pandas dataframe or de duplicated list depending on the request.

Will require the install of pandas https://pandas.pydata.org/pandas-docs/stable/install.html  and also tabulate (can pip install it).

The csv file should sit in the same folder as the python script and all should work well hopefully.
