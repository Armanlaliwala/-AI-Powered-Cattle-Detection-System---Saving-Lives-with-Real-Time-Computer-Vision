# 🐄 AI-Powered Cattle Detection System  
**Saving Lives with Real-Time Computer Vision**

Thousands of road accidents in India occur due to stray cattle. Manual livestock tracking is still common among farmers. This project is a **lightweight, real-time AI system** that detects cows using any basic camera feed — enabling both highway safety and smart farming.

---

## 🚀 Features

- ✅ **Low-Cost**: Runs on basic hardware like webcams or Raspberry Pi  
- ✅ **Real-Time**: Instant detection and alerting system  
- ✅ **Edge Compatible**: Can work offline in rural areas  
- ✅ **Highway Safety**: Detects cattle before accidents occur  
- ✅ **Smart Farming**: Helps farmers track and monitor livestock  

---

## 📸 Demo

🎥 [Watch the Video on linkedin](https://www.linkedin.com/feed/update/urn:li:activity:7342404724932947968/)

---

## 💡 Use Cases

- 🚧 **Road & Highway Safety**: Alerts officials when cattle are detected near roads  
- 🧑‍🌾 **Smart Farming**: Monitors livestock in real-time and prevents cattle loss  
- 🌐 **Edge AI**: Runs in low-bandwidth areas using edge devices  

---

## 🧠 Tech Stack

- Python
- YOLOv5 (You Only Look Once v5)
- OpenCV
- TensorFlow Lite / ONNX (for model optimization)
- Streamlit (optional UI for live monitoring)

---

## 🛠️ Installation & Setup

```bash
# Clone the repo
git clone https://github.com/armanlaliwala/cattle-detection-ai.git
cd cattle-detection-ai

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run detection
python detect.py --source your_video.mp4  # or use --source 0 for webcam
