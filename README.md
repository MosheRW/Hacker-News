# Top Stories and Comments Scraper

This project involves scraping top stories and their top comments from a website using an API, saving the data into CSV files, calculating statistics from the collected data, and visualizing the statistics. The following are the detailed requirements, functionalities, workflow, classes, and modules involved in the project.

## Requirements:
1. Scrape the top stories and save all information about them in a CSV file.
2. Scrape the top comments for each top story and save the information in a CSV file.
3. Calculate statistics for all the stories and comments (such as averages) and save these statistics in a CSV file.
4. Display the statistics to the user visually (not in the terminal).

## Functionality:
- **Input from user:** None
- **Output:**
  - The program will create and save three CSV files:
    - Information about all the top stories.
    - Information about all the top comments of the top stories.
    - Statistical information calculated from the data contained in the previous two files.
  - The program will display the statistics saved in the third CSV file graphically on the screen.

## Program Workflow:
1. The program will access the website via the API and retrieve information about the top stories.
2. The program will scrape the top stories.
3. The program will create an object of type `Record` to store information about each story.
4. The program will save all story records in a dedicated one-dimensional array.
5. The program will iterate over the array of stories and scrape the top comments for the stories.
6. The program will create an object of type `Record` to store information about each comment (possibly including pointers and/or indices, i.e., information that we generate ourselves and not scraped from the website).
7. The program will save all comment records in a dedicated one-dimensional array.
8. The program will calculate statistics for the data we have.
9. The program will save the scraped data as well as the statistics in CSV files.
10. The program will display the statistics to the user on the screen.
11. The program will terminate.

## Classes:
- **Record**

## Modules:
- **API module:** To communicate with the website.
- **Record module**
- **Main module**

## Data:
- The data will be stored in one-dimensional arrays.
- There is no external database, except for extensive use of a small `Record` object.

## Instructions for Running the Program:
1. **Setup the environment:** Ensure you have Python installed along with necessary libraries like `requests`, `pandas`, `matplotlib`, 'os', 'datetime', 'csv' and tqdm
2. **Run the main module:** This module will handle the entire workflow from scraping data to saving and visualizing the statistics.

## Files:
- `top_stories.csv`: Contains information about the top stories.
- `top_comments.csv`: Contains information about the top comments for each top story.
- `statistics.csv`: Contains statistical information calculated from the top stories and comments data.
- the files will saved in a special folder in the files folder

## Visualization:
- The program will generate graphs and charts to visualize the statistics calculated from the data, providing an easy-to-understand representation of the information.

By following the above structure, this project will efficiently scrape, store, analyze, and visualize data from the website's top stories and comments.

## Threading:
- the program will use threading to save time, when scriping