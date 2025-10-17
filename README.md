🎓 UniPerformer — Student Academic Performance Prediction App
📘 Project Overview

UniPerformer is a machine learning–powered web app that predicts a student’s academic performance category (e.g., Excellent, Average, or Poor) based on key academic and personal factors.

The goal of this project is to demonstrate how machine learning can be used to help schools and educators identify students who may need additional support — turning data into actionable insights.

🧠 How It Works

The model analyzes multiple features (like study hours, attendance, scores, and behavior metrics) and predicts the performance category a student is most likely to belong to.

The app was built using Streamlit, allowing users to input their details and instantly see predicted outcomes in a simple web interface.

⚙️ Steps Followed

Step 1: Data Preprocessing

Loaded and cleaned student academic data.

Handled missing values and standardized feature names.

Encoded categorical variables and normalized numeric data.

Step 2: Model Training

Trained a classification model using Scikit-Learn.

The best-performing model was saved as model.pkl.

Feature scaling and encoding steps were stored in scaler.pkl and feature_columns.pkl.

Step 3: Model Deployment with Streamlit

Built a simple and interactive web app (student_performance_app.py) that loads the model and scaler.

The app allows users to input data and receive predictions in real time.

Step 4: Model Testing

Tested the model using unseen data samples.

Achieved strong accuracy and generalization performance.

🧩 Tech Stack

Python

Streamlit – for deployment

Pandas, NumPy – for data handling

Scikit-Learn – for model building and preprocessing

Pickle – for model serialization

🚀 How to Run This Project

Step 1: Clone the Repository

git clone https://github.com/yourusername/uniperformer.git
cd uniperformer


Step 2: Install the Required Libraries
Make sure Python (3.8 or higher) is installed, then run:

pip install -r requirements.txt


Step 3: Run the App

streamlit run student_performance_app.py


Step 4: Interact with the Model

Input student data (attendance, study time, etc.).

Click Predict to see the predicted performance category.

📊 Example Output
Input Features	Predicted Category
80% attendance, 4 study hours/day	Excellent
60% attendance, 2 study hours/day	Average
💡 Future Improvements

Add visualization for student performance insights.

Deploy online using Streamlit Cloud or Render.

Integrate with school management systems.

👨‍💻 Author

Macnelson Chibuike
📧 mcibuike6@gmail.com

🔗 linkedin.com/in/macnelson-chibuike-b9126b292
