# sqlFaker

sqlFaker is a fake data generator for your relational database.

Check out the package in action @ [alles-tools](https://alles-tools.com/fakemydb)

## Changes/updates to be done:

* DISPLAY ERROR WHEN THE SCRIPT IS SYNTACTICALLY WRONG
* Make the size to display size in size parameter
* The parser doesnt display error if given Varchar[20] instead of varchar(20).The data_type becomes Varchar[20] which raises a "no required data type found" exception.
* Include Primary key display
* Remove check identification
* Display the script in identification page
* We support auto increment so remove it from the description in front page
* Check if e.__Cause__ correctly displays the error raised.

## LICENSE 

