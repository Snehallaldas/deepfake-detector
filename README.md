# Deepfake Detector

A comprehensive application for detecting deepfakes using machine learning. This project combines a FastAPI backend with an advanced image classification model and an intuitive frontend web interface.

## Overview

Deepfake Detector is designed to identify manipulated or artificially generated media content using state-of-the-art deep learning techniques. The application provides:

- **FastAPI Backend**: High-performance REST API for deepfake detection
- **Image Classification Model**: Advanced neural network trained to detect deepfakes
- **Frontend Web Interface**: User-friendly interface for uploading and analyzing images

## Features

- 🎯 Accurate deepfake detection using deep learning
- 🚀 Fast inference with FastAPI backend
- 🖼️ Support for image upload and analysis
- 📊 Confidence scores and detailed detection results
- 💻 Responsive web interface
- 🔒 Secure API endpoints

## Project Structure

```
deepfake-detector/
├── backend/
│   ├── app.py              # FastAPI application
│   ├── models/             # ML model files
│   ├── requirements.txt     # Python dependencies
│   └── utils/              # Utility functions
├── frontend/
│   ├── index.html          # Main web interface
│   ├── css/                # Styling
│   ├── js/                 # Frontend logic
│   └── assets/             # Images and static files
├── README.md               # Project documentation
└── .gitignore              # Git ignore rules
```

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js (for frontend development)
- pip (Python package manager)

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:
```bash
uvicorn app:app --reload
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Open `index.html` in your web browser or serve it using a local web server:
```bash
python -m http.server 8080
```

The frontend will be available at `http://localhost:8080`

## API Endpoints

### Detection Endpoint

**POST** `/api/detect`

Upload an image for deepfake detection.

**Request:**
```
Content-Type: multipart/form-data
Body: image file
```

**Response:**
```json
{
  "is_deepfake": boolean,
  "confidence": float,
  "message": "string"
}
```

## Usage

1. Open the frontend interface in your browser
2. Upload an image file (JPG, PNG, etc.)
3. Click "Analyze" to run detection
4. View results including:
   - Detection status (Real or Deepfake)
   - Confidence percentage
   - Analysis details

## Model Information

The detection model is trained on a comprehensive dataset of both authentic and deepfake images, utilizing:
- Convolutional Neural Networks (CNN)
- Transfer learning from pre-trained models
- Advanced image preprocessing techniques

## Performance

- **Accuracy**: Optimized for both precision and recall
- **Latency**: Sub-second inference times
- **Throughput**: Handles multiple concurrent requests

## Technologies Used

- **Backend**: FastAPI, Python, PyTorch/TensorFlow
- **Frontend**: HTML5, CSS3, JavaScript
- **ML Framework**: PyTorch/TensorFlow
- **API**: RESTful API with FastAPI

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Snehallaldas**

## Acknowledgments

- Thanks to the open-source community for the ML frameworks and libraries
- Dataset contributors for providing training data
- All contributors who have helped with code improvements

## Contact & Support

For questions, issues, or suggestions, please open an issue on the GitHub repository.

---

**Note**: This tool is intended for research and educational purposes. Always verify detection results and consult with domain experts for critical applications.
