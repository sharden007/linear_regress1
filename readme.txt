Linear Regression provides actionable insights into spending patterns.

Orig steps
Convert the csv data file to json using  Prep_data python files.
Take a small sample of the data then:
👉 Prompt 1
This is the structure of my sales data in JSON format. Understand the structure and suggest five key data visualization metrics that would be the best fit to create an interactive sales dashboard. Also explain why we should use each one?

👉 Prompt 2
Now, I want you to create an interactive sales performance dashboard with the five key visualizations using HTML and JavaScript. Use the latest version of Plotly.js CDN and include an upload feature so that we can upload the JSON file. It should generate the dashboard based on the uploaded data.
Note: I need to upload the sales data from my local computer, and it should create the dashboard based on that data.
Please provide the solutuon as an HTML downloadable file

👉 Prompt 3 (if needed)
From the dashboard you created, change the style to glass morphism. Then, adjust the padding width of the charts to 40%, and change the background colour to icy blue. Can you also provide this as a downloadable HTML file?



requires numpy==1.26.4

$ pip install numpy==1.26.4 


Output
Console: Displays evaluation metrics (MSE and R-squared score).
CSV File: A file named predictions.csv containing actual and predicted values.
Visualization: A scatter plot of actual vs predicted values with a reference line.
