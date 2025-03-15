# 🎵 Music Genre Classifier  
*A Deep Learning & Machine Learning-powered genre prediction system.*  

![Genre Classifier](https://user-images.githubusercontent.com/674621/71187872-fb6de800-2269-11ea-9009-72c8164dfd57.png)  
(*Example spectrogram image – replace with your own!*)

---

## 📌 Overview  
This project classifies music genres using **Machine Learning (Random Forest)** and **Deep Learning (VGG16 CNN)**.  
It processes audio files, extracts features, and predicts the genre based on trained models.

**Key Features:**  
✅ Upload an audio file and get its predicted genre.  
✅ Uses **Librosa** for feature extraction (MFCCs, Chroma, ZCR, Spectral Contrast).  
✅ Supports both **ML (Random Forest)** and **DL (VGG16 CNN)** for predictions.  
✅ Built with **Streamlit** for an interactive web app.  

---

## 🚀 Demo  
🎬 **Live Demo:** *(Yet to delpoy)*  
🔗 **GitHub Repository:** [Music-Genre-Classifier](https://github.com/gg-hgew/Music-Genre-Classifier)  

---

## 📂 Project Structure  
```plaintext
📦 Music-Genre-Classifier
 ┣ 📂 gtzan_dataset           # The dataset (if stored locally)
 ┣ 📂 spectrogram_dataset      # Spectrogram images for CNN
 ┣ 📂 models                  # Trained models (optional)
 ┣ 📜 app.py                  # Streamlit Web App
 ┣ 📜 main.py                 # Main script for running classification
 ┣ 📜 predict.py               # Functions for predicting genre
 ┣ 📜 requirements.txt         # Required libraries
 ┣ 📜 README.md                # Project Overview
 ┗ 📜 .gitignore               # Ignored files (e.g., dataset, cache)
```

---

## 📦 Installation & Setup  
1️⃣ **Clone the repository**  
```bash
git clone https://github.com/gg-hgew/Music-Genre-Classifier.git
cd Music-Genre-Classifier
```

2️⃣ **Download the dataset from Kaggle**  
🔗 **GTZAN Dataset Link:** [Click Here](https://www.kaggle.com/datasets/andradaolteanu/gtzan-dataset-music-genre-classification)  
- Extract the dataset inside the project folder as:  
  ```
  Music-Genre-Classifier/gtzan_dataset/
  ```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run the Streamlit Web App**  
```bash
streamlit run app.py
```
🎶 **Now you can upload audio files and get genre predictions!**  

---

## 🛠️ How It Works  
1️⃣ **Feature Extraction:**  
   - Uses **Librosa** to extract **MFCCs, Chroma, Spectral Contrast, and Zero-Crossing Rate (ZCR)**.  
2️⃣ **Model Selection:**  
   - **Random Forest** for classical ML classification.  
   - **VGG16-based CNN** trained on spectrogram images.  
3️⃣ **Prediction:**  
   - Takes an audio file, extracts features, and predicts its genre.  

---

## 📊 Model Performance  
| Model            | Accuracy |
|-----------------|----------|
| Random Forest   | 94.7%    |
| CNN (VGG16)     | 92.4%    |

---

## ✨ Example Prediction  
```bash
🎵 Uploading: classical.00004.wav
✅ Predicted Genre: Classical
```

---

## 🛠 Tech Stack  
🔹 **Machine Learning**: Scikit-Learn, RandomForest  
🔹 **Deep Learning**: TensorFlow, VGG16  
🔹 **Audio Processing**: Librosa  
🔹 **Web App**: Streamlit  
🔹 **Dataset**: GTZAN  

---

## 📜 License  
This project is licensed under the **MIT License**.  

---

## 🤝 Contributions & Issues  
🙌 Feel free to **contribute** to the project!  
📌 If you find any **bugs** or have **feature requests**, open an **issue** in GitHub.  

---

### 🌟 **Star this repository if you found it useful!** ⭐  
🚀 **Now go ahead and make music classification awesome!** 🎶🔥  
