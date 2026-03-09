# Enhancing Intrusion Detection System using GANs

## Project Description
This project focuses on enhancing an Intrusion Detection System (IDS) using Generative Adversarial Networks (GANs) to improve the detection of cyber attacks in network traffic. Traditional IDS models often struggle with imbalanced datasets where normal traffic is much larger than attack traffic. To address this problem, GANs are used to generate synthetic attack samples which help improve the performance of machine learning models.

The system analyzes network traffic data and classifies connections as either normal or malicious. A real-time visualization dashboard is also developed using Streamlit to monitor network activity and analyze attack patterns.

## Dataset
This project uses the **NSL-KDD dataset**, a widely used dataset for intrusion detection research. It contains labeled network traffic records with different connection features.

Example dataset record:

duration  protocol_type  service  flag  src_bytes  dst_bytes  label  
5         tcp            http     SF    181        5450       normal  

Meaning:
- A computer connected to a server
- Using TCP protocol
- Accessing HTTP service
- Connection status is SF (successful connection)
- Data transferred between source and destination
- Classified as normal traffic

## Attack Types Detected
The system detects multiple cyber attacks including:
- DoS (Denial of Service)
- Probe attacks
- U2R (User to Root)
- R2L (Remote to Local)

## Technologies Used
- Python
- TensorFlow / Keras
- Pandas
- NumPy
- Matplotlib
- Streamlit

## Project Screenshots

### IDS Dashboard
![Dashboard](screenshots/dashboard.png)

### Attack Distribution
![Attack Distribution](screenshots/attack_distribution.png)

### Confusion Matrix
![Confusion Matrix](screenshots/confusion_matrix.png)

## Project Objective
The main objective of this project is to improve cyber attack detection by using GANs to generate synthetic attack data and enhance the training process of the intrusion detection model. The project also provides a visualization dashboard to analyze network traffic and attack patterns effectively.

## Author
Ambika Korala  
Computer Science and Engineering (Cybersecurity)  
Malla Reddy Engineering College for Women
