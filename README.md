Book Recommendation and Intelligence Engine (B.R.I.E.) - README FILE    
     
This text file contains a general overview of BRIE's codebase denoting which parts of the codebase contain what functionalities  
    
Folder src - Entire data collection and data loading.  
	Folder gcp_data_loading - Trials to load data into Google Cloud Platform  
	Folder data_migration - Loading appropriate data into MySQL and Mongo database  
  
  
Folder data - All the cleaned and uncleaned data split into appropriate batches  
    
Folder extra - Some MongoDB queries for reference  
    
Folder Brie - The entire Django Web Framework  
	Folder Brie - Some basic settings of the product  
	Folder app - The required pages, templates and rendering of the product  
		Folder templates - Actual HTML pages  
		Folder static - The necessary static files such as images and stylesheets  
		Folder migrations - Data loading into MySQL supported by Django  
		views.py - The View file of the MVC pattern. One can find all functionalities here  

**Instruction to Set-up Pipeline**  
  
- Main python script to load data to mongoDB  
	- src/data_migration/final_data_migrate.py (book)  
	- src/data_migration/load_sim_books.py (book_similar)  
	- src/data_migration/load_goodreads_desc.py (book_goodreads_desc)  

- MongoDB Hosting
	- local : mongodb://brie:brie1234@localhost:27017/Brie
	- mongoDB Atlas Cloud with AWS : mongodb+srv://brie:brie1234@brie-mongo-cluster-m0oah.mongodb.net/Brie