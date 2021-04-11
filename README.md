# File Data Rendering into html

# Flask
  Flask is a web application framework written in Python.

# Pre-requisites
  We need to have a basic knowledge on HTML,CSS,Python and JS.
  For using flask we need to have the current version of python installed in the system.
  Path should be added while installing python
  
  # 1.Virtual Environment
      virtualenv is a virtual Python environment builder. 
      It helps a user to create multiple Python environments side-by-side
        pip install virtualenv  # for windows
  # 2.Install Flask
        pip install Flask
  Create a project folder to execute the application
  # 3.Compling and Deployment
        python <file_name>.py
      It will compile sucessfully by giving the local address with which the model runs on local server.
      We are actually importing render_template function provided by the Flask and then rendering our HTML template
# Intership Task - Flask Application
  Task is given as of 5 steps...
    - Reciving data only one time.
    - Need to render the data by reading data file into a HTML page.
    - Endpoint should accept target file name as optional variable part of URL and default to file1.txt
    - running a loop to return a specific part or as a whole.
    - error page should be generated with exception details.
  - For reading a file we will also read the starting and ending point inside it.
  - Data is read from the given name of ile and retured into the HTML page i.e index.html
  - After opening the file, the data inside it will be encoded and taken as one data.
  - If the file not found then FileNotFoundError exception will be generated.
 
   

      
  
