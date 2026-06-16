# 🩺 MediScan — Symptom to Disease Predictor

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ExtraTrees-orange?style=for-the-badge&logo=scikit-learn)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-yellow?style=for-the-badge&logo=html5)
![Vercel](https://img.shields.io/badge/Deploy-Vercel-black?style=for-the-badge&logo=vercel)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered web app that predicts diseases from symptoms using a trained Extra Trees Classifier.**
The entire model runs **100% in your browser** — no server, no Python, no installation needed.

[🚀 Live Demo](#) &nbsp;·&nbsp; [📂 GitHub Repo]() &nbsp;·&nbsp; 

</div>

---

## 📸 Preview

> Dark mode and Light mode supported — toggle with the 🌙 / ☀️ button in the header.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🧠 AI Prediction | Extra Trees Classifier trained on augmented medical dataset |
| 🔍 123 Symptoms | Search and filter from a comprehensive symptom list |
| 🏆 Top-3 Results | Ranked disease predictions with confidence percentages |
| 📊 Full Breakdown | Probability chart across all 41 diseases |
| 🌙 Theme Toggle | Dark mode and Light mode with localStorage persistence |
| ⚡ Browser-Only | Model embedded in HTML — works offline, no backend needed |
| 📱 Responsive | Works on desktop and mobile |

---

## 🧠 Model Details

| Property | Value |
|---|---|
| Algorithm | Extra Trees Classifier |
| Training Samples | ~8,700 (original + augmented subsets) |
| Diseases Covered | 41 |
| Symptoms (Features) | 123 |
| Accuracy | 93%+ on diverse test cases |
| Inference | Client-side JavaScript (no API call) |

### Diseases Covered
`Fungal Infection` · `Allergy` · `GERD` · `Chronic Cholestasis` · `Drug Reaction` · `Peptic Ulcer` · `AIDS` · `Diabetes` · `Gastroenteritis` · `Bronchial Asthma` · `Hypertension` · `Migraine` · `Cervical Spondylosis` · `Paralysis` · `Jaundice` · `Malaria` · `Chicken Pox` · `Dengue` · `Typhoid` · `Hepatitis A/B/C/D/E` · `Tuberculosis` · `Common Cold` · `Pneumonia` · `Dimorphic Haemorrhoids` · `Heart Attack` · `Varicella` · `Hypothyroidism` · `Hyperthyroidism` · `Hypoglycemia` · `Osteoarthritis` · `Arthritis` · `Vertigo` · `Acne` · `Urinary Tract Infection` · `Psoriasis` · `Impetigo` and more.

---

## 🗂️ Project Structure

```
mediscan/
├── public/
│   └── index.html          ← Complete standalone app (open this to run!)
├── api/
│   └── predict.py          ← FastAPI backend (used for Vercel serverless)
├── vercel.json             ← Vercel deployment config
├── requirements.txt        ← Python dependencies
├── README.md
├── DEPLOY.md               ← Step-by-step Vercel deploy guide
└── .gitignore
```

---

## ▶️ Run Locally (Zero Setup)

No installation needed whatsoever.

```
1. Download and unzip the project
2. Open the  mediscan/  folder
3. Double-click  public/index.html
4. It opens in your browser and works instantly ✅
```

> The entire ML model is embedded inside `index.html` and runs as JavaScript. No Python required.

---

## ☁️ Deploy to Vercel

### Step 1 — Push to GitHub

```bash
# Navigate into the project folder
cd mediscan

# Initialize git
git init
git add .
git commit -m "Initial commit: MediScan Symptom Disease Predictor"

# Create a new repo on github.com, then connect it:
git remote add origin https://github.com/YOUR_USERNAME/mediscan.git
git branch -M main
git push -u origin main
```

### Step 2 — Deploy on Vercel

1. Go to **[vercel.com](https://vercel.com)** and sign in with GitHub
2. Click **"Add New Project"**
3. Select your `mediscan` repository
4. Leave all settings as default — Vercel auto-reads `vercel.json`
5. Click **"Deploy"**

Your live URL will be:
```
https://mediscan-YOUR_USERNAME.vercel.app
```

> Since the app is a single static HTML file, deployment completes in under 30 seconds.

---

## 🛠️ Tech Stack

**Frontend**
- Pure HTML, CSS, JavaScript — no frameworks
- Google Fonts (Inter, Sora)
- CSS custom properties for theming

**ML / Backend**
- Python 3.9+
- scikit-learn (Extra Trees Classifier)
- Augmented training with random symptom subsets
- FastAPI (for optional server deployment)

---

## ⚠️ Medical Disclaimer

> This tool is built for **educational and academic purposes only**.
> It does **not** provide medical advice, diagnosis, or treatment.
> Always consult a qualified and licensed healthcare professional for any medical concerns.

---

