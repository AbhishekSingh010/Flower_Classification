# Iris Flower Classification with Flask Integration
## Iris Flower

This repository contains a machine learning project focused on classifying Iris flowers using a trained model. The project also includes a Flask web application that allows users to input flower attributes and get real-time predictions from the model.

Project Overview
In this project, we aim to demonstrate the process of building a machine learning model for classifying Iris flowers based on their sepal length, sepal width, petal length, and petal width. We use the popular Iris dataset and a machine learning algorithm to achieve accurate classification. The trained model is then integrated into a Flask web application for easy interaction.

Contents
iris_classification.ipynb: Jupyter Notebook containing the model building process, training, and evaluation using the Iris dataset.
app/: This directory contains the Flask web application files.
app.py: The main Flask application script handling routes and model integration.
templates/: Contains the HTML templates for the web interface.
Getting Started
To run the Flask web application locally and interact with the Iris flower classification model, follow these steps:

Clone the Repository: Begin by cloning this repository to your local machine:

bash
Copy code
git clone https://github.com/AbhishekSingh010/Flower_Classification
Navigate to the App Directory: Move into the app directory where the Flask application is located:



Copy code
python app.py
Access the Web App: Open your web browser and go to http://localhost:5000 to use the Iris flower classification app.

Model Integration
The trained machine learning model is integrated into the Flask web application. The model's prediction functionality is accessed through the /predict route of the Flask app. Input attributes (sepal length, sepal width, petal length, and petal width) are provided via a web form, and the model returns the predicted Iris species.

Dataset
The Iris dataset used for this project is available through the UCI Machine Learning Repository. It consists of 150 samples from three different species of Iris flowers.

Contribution
Contributions to this project are welcome! If you find any issues, have suggestions for improvements, or want to extend the functionality, feel free to open an issue or submit a pull request.

Credits
This project was developed by Abhishek. If you find this project useful or refer to it in your work, please provide credit by linking back to this repository.

License
This project is licensed under the MIT License, allowing you to modify and distribute the code for your own purposes.

I hope you enjoy using this Iris flower classification web application built with Flask. If you have any questions or feedback, don't hesitate to get in touch!







