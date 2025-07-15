# Emotion-Detector

## Description

Emotion-Detector is a Python web application that detects emotions from text input using IBM Watson NLP. The app provides a simple web interface for users to submit text and view detected emotions. It includes robust error handling, unit tests, and static code analysis support.

## Features

- Detects emotions from user input text
- Web interface built with Flask
- Output formatting for easy interpretation
- Error handling for invalid input and server issues
- Unit tests for core functionality
- Static code analysis support

## Setup

### Technologies Used

- Python
- Flask
- ibm-watson
- ibm-cloud-sdk-core

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/brendanbadhe/Emotion-Detector.git
cd Emotion-Detector
pip install flask ibm-watson ibm-cloud-sdk-core pylint
```

Configure your IBM Watson API credentials:

Open `EmotionDetection/emotion_detection.py` and replace `API_KEY` and `INSTANCE` in the file with your own IBM Cloud credentials.

## Usage

Start the Flask server:

```bash
python server.py
```

Open your browser and go to `http://localhost:5000` to use the web interface.

## Testing

Run unit tests:

```bash
python test_emotion_detection.py
```

## Static Code Analysis

Run static analysis using pylint on the main files:

```bash
pylint EmotionDetection/emotion_detection.py
pylint server.py
```

## Screenshots

See the [`Images/` folder](./Images/) for screenshots and diagrams illustrating the application and its output.
