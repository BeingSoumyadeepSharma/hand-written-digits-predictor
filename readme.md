# Canvas Play - The Digit Predictor :stars:

## Description :page_with_curl:

This a Web Application developed using Flask and TensorFlow. This Application can predict any digit between 0 and 9 drawn on the canvas. A Deep Neural Network model trained on the MNIST Dataset is being used here. The **main_model.py** is the file where I have created the model using TensorFlow and Keras and saved it for later use. After a digit is drawn on the canvas, this application sends the image URI using the Fetch API to the Flask backend **(app.py)**.

In the backend, the URI is processed into an image. The processing of the image is done using the **image_processor.py** file. In this file, the image is generated using File Handling techniques which is then send to an OpenCV model where the image is converted to data (numpy array). This array is then returned back to the Flask app.

The numpy array returned is then passed as parameter to the **digitPredictor()** function present in the **digit_predictor.py**. In the **digit_predictor.py** , the prediction is made using the model created in the **main_model.py** file. The result generated is send back to the Flask app from where it is send to the frontend to be displayed on the webpage.

### Python Modules used :wrench:

The following modules have been used to build this Project
 - Flask
 - TensorFlow
 - OpenCV
 - Numpy

## Installation and Running the App :rocket:

### Step 1:

Clone the repository using the following commands and then change the directory.

```sh
$ git clone https://github.com/BeingSoumyadeepSharma/hand-written-digits-predictor.git
$ cd hand-written-digits-predictor
```

The above part is same for Windows.

### Step 2:

We need to create an environment for this project. We can use either **virtualenv** (which I used) or **pipenv**. It is preferred that we use a Python version lower than v3.7.9, as I have used v3.7.9 to build this project.

 - #### Virtualenv
    
    - **On Linux**
        ```sh
        $ pip install virtualenv
        $ venv env
        $ source env/bin/activate
        ```
    - **On Windows**
        ```cmd
        pip install virtualenv
        virtualenv env
        env\Scripts\activate.bat
        ```
    
 - #### Pipenv
    
    - **On Linux**
        ```sh
        $ pip install pipenv
        $ pipenv shell
        ```
    - **On Windows**
        ```cmd
        pip install pipenv
        pipenv shell
        ```

### Step 3:

Now we need to install all the required modules. For this we will use the **requirements.txt** file

 - #### Virtualenv

    - **On Linux**
        ```sh
        $ pip install -r requirements.txt
        ```
    - **On Windows**
        ```cmd
        pip install -r requirements.txt
        ```

 - #### Pipenv
    
    - **On Linux**
        ```sh
        $ pipenv install -r requirements.txt
        ```
    - **On Windows**
        ```cmd
        pipenv install -r requirements.txt
        ```

### Step 4: (Final Step)

Now we just have to run the **app.py** file, redirect to http://127.0.0.1:5000/ or http://localhost:5000/ and enjoy the Web App.

```
python app.py
```



##### Created by Soumyadeep Sharma