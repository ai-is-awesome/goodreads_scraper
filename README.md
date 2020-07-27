<h1>How to use the scraper</h1>


<ul>

<li><h3>Open the main.py module</h3></li>


<li><h3>Set the FILE_PATH constant to the csv/xlsx file you want to check the ISBN number of.</h3></li>

<li><h3>Set the ISBN_COLUMN_NAME equal to the isbn column name  of the csv / xlsx file</h3></li>

<li><h3>Set the file format value equal to either 'csv' or 'xlsx' depending on the file in the FILE_PATH</h3></li>

<li><h3>To search for the isbn number, set the value of ISBN equal to the string of ISBN number</h3></li>

<li><h3>Run main()</h3></li>

<h2>The program will search for ISBN numbers in the CSV file, if the ISBN number is found in CSV the program stops. 
<br>

Otherwise, the program runs the GoodRead Scraper and fetches the results , returns a pandas DataFrame


</ul>