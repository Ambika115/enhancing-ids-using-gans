Enhancing Intrusion Detection System using GANs
Overview

This project focuses on improving the performance of an Intrusion Detection System (IDS) using Generative Adversarial Networks (GANs). Intrusion Detection Systems play a critical role in cybersecurity by monitoring network traffic and identifying suspicious or malicious activities.

Traditional IDS models often struggle with imbalanced datasets, where some types of attacks occur less frequently than others. This project addresses that problem by using GANs to generate synthetic attack samples, which helps improve the training of IDS models and increases detection accuracy.

The project also includes a visualization dashboard to monitor network traffic and analyze results.

Objectives

The main objectives of this project are:

Improve IDS detection accuracy using GAN-based data generation

Handle imbalanced network intrusion datasets

Detect different types of cyber attacks in network traffic

Provide visual insights through a dashboard

Evaluate model performance using metrics such as accuracy and confusion matrix

Technologies Used

Python

TensorFlow / Keras

Pandas

NumPy

Scikit-learn

Streamlit

Matplotlib

Git & GitHub

Dataset

The project uses the NSL-KDD dataset, which is a well-known dataset for network intrusion detection research.

The dataset contains multiple categories of network activities such as:

Normal traffic

Denial of Service (DoS)

Probe attacks

Remote to Local (R2L)

User to Root (U2R)

GAN models are used to generate additional attack samples to improve IDS training.

Project Structure
enhancing-ids-using-gans
│
├── dataset
│   └── KDDTrain+.txt
│
├── src
│   ├── data_preprocessing.py
│   ├── gan_model.py
│   └── train_ids.py
│
├── dashboard
│   └── app.py
│
├── requirements.txt
└── README.md
Installation
Clone the repository
git clone https://github.com/Ambika115/enhancing-ids-using-gans.git
Navigate to the project folder
cd enhancing-ids-using-gans
Create virtual environment
python -m venv venv
Activate virtual environment

Windows:

venv\Scripts\activate
Install required libraries
pip install -r requirements.txt
Running the Project
Train the IDS model
python src/train_ids.py
Run the dashboard
streamlit run dashboard/app.py

Open the dashboard in your browser:

http://localhost:8501
Results

The proposed IDS system enhanced with GANs helps:

Improve intrusion detection accuracy

Handle class imbalance in cybersecurity datasets

Provide real-time visualization of network data

Improve model training through synthetic data generation

Future Improvements

Integration with real-time network traffic monitoring

Using advanced deep learning architectures

Deployment in cloud-based security systems

Improving detection for rare attack types
