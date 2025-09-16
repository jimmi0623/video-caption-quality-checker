# 📽 Video Captioning Quality Checker

## 📝 Description
The **Video Captioning Quality Checker** is a Python-based tool that validates video caption files (e.g., `.srt`).  
It checks grammar, punctuation, and timing alignment to ensure captions are accurate, readable, and follow accessibility standards.
---

## ✨ Features
- Grammar and spelling validation using `language-tool-python`.
- Timing checks for overlapping or out-of-order captions.
- Context checks to ensure captions are descriptive and concise.
- Command-line interface for quick validation.
- *(Optional)* Streamlit or Gradio dashboard for visualizing flagged issues.

---

## 🛠 Requirements
- Python 3.9+
- `language-tool-python`
- `pysrt`
- `argparse` (built-in)
- *(Optional)* `streamlit` or `gradio` for interactive dashboard

Install dependencies:
```bash
pip install language-tool-python pysrt streamlit gradio
```

---

## ▶ Usage
1. Clone the repository:
```bash
git clone https://github.com/your-username/video-caption-quality-checker.git
cd video-caption-quality-checker
```
2. Run the checker on a caption file:
```bash
python checker.py --file sample.srt
```
3. *(Optional)* Launch the dashboard:
```bash
streamlit run dashboard.py
```

---

## 📊 Example Output
```
[OK] Caption 1: Timing and grammar valid
[GRAMMAR] Caption 3: Grammar issue – “They is running” → “They are running”
[TIMING] Overlap: Caption 5 ends after Caption 6 starts
```

---

## 📚 Skills Demonstrated
- **Data Quality Assurance**: Checking accuracy and consistency of captions.
- **Natural Language Processing**: Grammar and context validation.
- **Python Scripting**: Automating QA workflows.
- **Version Control**: Managing project updates with Git.
- **Optional Web App Development**: Using Streamlit or Gradio for a simple UI.

---

## 📄 License
This project is open-source and available under the MIT License.
