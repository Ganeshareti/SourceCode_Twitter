# Twitter Spam Detection System

A Flask-based web application that uses a **Convolutional Neural Network (CNN)** with **GloVe word embeddings** to detect spam tweets in real time. The system provides a user-friendly interface for tweet classification, user authentication, and a deep-learning evaluation dashboard.

---

## 📑 Table of Contents

1. [Overview](#-overview)
2. [Features](#-features)
3. [Project Structure](#-project-structure)
4. [Tech Stack](#-tech-stack)
5. [Prerequisites](#-prerequisites)
6. [Installation & Setup](#-installation--setup)
7. [Database Setup](#-database-setup)
8. [Running the Application](#-running-the-application)
9. [Application Routes / Usage](#-application-routes--usage)
10. [Model Details](#-model-details)
11. [Dataset](#-dataset)
12. [Evaluation Metrics](#-evaluation-metrics)
13. [Default Credentials](#-default-credentials)
14. [Sample Test Tweets](#-sample-test-tweets)
15. [Screenshots / Output](#-screenshots--output)
16. [Troubleshooting](#-troubleshooting)
17. [Future Enhancements](#-future-enhancements)
18. [Contributing](#-contributing)
19. [License](#-license)
20. [Author](#-author)

---

## 🔎 Overview

The **Twitter Spam Detection System** is a web-based deep-learning project that classifies tweets as **ham (legitimate)** or **spam (unsolicited/advertising)**. The CNN model is trained on a labeled Twitter dataset using pre-trained GloVe embeddings (100-dimensional) to capture the semantic context of words. A Flask front-end provides a clean UI for user registration, login, tweet submission, and live prediction, along with an admin dashboard to view model performance.

---

## ✨ Features

- **User Registration & Login** – Secure user authentication using MySQL.
- **Admin Login** – Default admin account for accessing the dashboard.
- **Real-time Tweet Classification** – Enter any tweet and get instant `ham` or `spam` prediction.
- **CNN-based Deep Learning Model** – 1D Convolutional Neural Network trained on a Twitter dataset.
- **GloVe Word Embeddings** – Pre-trained 100-D embeddings for better semantic understanding.
- **Evaluation Dashboard** – Displays Accuracy, Precision, Recall, and F1-Score with a bar chart.
- **Tokenization Pipeline** – Re-uses the trained tokenizer for consistent preprocessing at inference.
- **Static & Template-based UI** – Clean HTML/CSS frontend served via Flask.

---

## 📁 Project Structure

```
SourceCode_Twitter/
│
├── .venv/                          # Python virtual environment (excluded via .gitignore)
├── .claude/                         # Claude Code settings
├── DB/
│   └── db.sql                       # MySQL schema dump (twitter_spam database)
│
├── Detection/
│   ├── cnn_model.h5                 # Trained CNN model (Keras)
│   ├── DBConfig.py                  # MySQL connection & DB/table auto-creation
│   ├── index.py                     # Flask application (main entry point)
│   ├── Train_CNN.py                 # Model training & evaluation script
│   ├── tokenizer.pickle             # Saved Keras tokenizer
│   ├── samples.txt                  # Sample tweets for quick testing
│   │
│   ├── data/
│   │   └── glove.6B.100d.txt        # Pre-trained GloVe embeddings (~347 MB)
│   │
│   ├── dataset/
│   │   └── twitter_dataset.csv      # Labeled training dataset
│   │
│   ├── static/                      # Static assets
│   │   ├── accuracy.png             # Generated evaluation bar chart
│   │   ├── css/                     # Stylesheets
│   │   ├── fonts/                   # Web fonts
│   │   └── images/                  # UI images
│   │
│   └── templates/                   # Jinja2 HTML templates
│       ├── index.html               # Landing page
│       ├── admin_login.html         # Admin login
│       ├── admin_home.html          # Admin home
│       ├── user_login.html          # User login
│       ├── user_register.html       # User registration
│       ├── user_home.html           # User dashboard
│       ├── detection.html           # Tweet input form
│       ├── detection_result.html    # Prediction result
│       ├── dl_evaluations.html      # Metrics dashboard
│       ├── header.html              # Common header
│       ├── aheader.html             # Admin header
│       ├── uheader.html             # User header
│       └── footer.html              # Common footer
│
├── requirements.txt                 # Python dependencies
├── .gitignore                       # Ignored files/folders
└── README.md                        # Project documentation
```

---

## 🛠 Tech Stack

| Layer            | Technology                                       |
|------------------|--------------------------------------------------|
| **Language**     | Python 3.x                                       |
| **Web Framework**| Flask 3.1.3                                      |
| **Deep Learning**| TensorFlow 2.21.0, Keras 3.15.0                  |
| **Embeddings**   | GloVe 6B (100-D)                                 |
| **Database**     | MySQL (via `mysql-connector-python` 9.7.0)       |
| **Frontend**     | HTML5, CSS3, Jinja2 templates                    |
| **Data / ML**    | pandas, NumPy, scikit-learn, matplotlib          |
| **Serialization**| pickle (Keras tokenizer)                         |

---

## ✅ Prerequisites

Make sure the following are installed on your system:

1. **Python 3.9 or higher**
2. **pip** (Python package manager)
3. **MySQL Server** (5.5+ or 8.x)
4. **Git** (optional, for cloning)
5. At least **2 GB free disk space** (GloVe file is ~347 MB)

Verify installations:

```bash
python --version
pip --version
mysql --version
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd SourceCode_Twitter
```

### 2. Create & Activate a Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

**Linux / macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If you have trouble installing TensorFlow, ensure your Python version is compatible with TensorFlow 2.21.0.

---

## 🗄 Database Setup

The app **automatically creates** the database (`twitter_spam`) and the `register` table on first run via `DBConfig.py`. However, you can also import the schema manually:

### Option A — Automatic (recommended)

Just start the app; it will create everything if MySQL credentials are correct.

### Option B — Manual Import

```bash
mysql -u root -p < DB/db.sql
```

### MySQL Credentials

Default values are hard-coded in `Detection/DBConfig.py`:

| Parameter | Value     |
|-----------|-----------|
| Host      | localhost |
| User      | root      |
| Password  | root      |
| Database  | twitter_spam |
| Table     | register  |

> ⚠️ **Important:** Edit `Detection/DBConfig.py` and update the credentials if your local MySQL setup differs.

### `register` Table Schema

| Column     | Type           | Description           |
|------------|----------------|-----------------------|
| name       | VARCHAR(100)   | User's full name      |
| username   | VARCHAR(100)   | Unique login ID       |
| passwrd    | VARCHAR(100)   | Password (plain text) |
| email      | VARCHAR(100)   | Email address         |
| mno        | VARCHAR(100)   | Mobile number         |

---

## ▶️ Running the Application

1. **Make sure MySQL is running** on `localhost:3306`.
2. **Activate your virtual environment** (see step 2 above).
3. **Navigate to the project root** and run:

```bash
python Detection/index.py
```

4. Open your browser and go to:

```
http://localhost:4683/
```

The Flask development server runs on **`localhost:4683`** with `debug=True`.

---

## 🌐 Application Routes / Usage

| Route                  | Method   | Description                                      |
|------------------------|----------|--------------------------------------------------|
| `/`                    | GET      | Landing / home page                              |
| `/admin`               | GET      | Admin login page                                 |
| `/adminlogin_check`    | POST     | Validate admin credentials                       |
| `/admin_home`          | GET      | Admin dashboard                                  |
| `/user_home`           | GET      | User dashboard (post-login)                      |
| `/user_login`          | GET      | User login form                                  |
| `/newuser`             | GET      | New user registration form                       |
| `/user_register`       | POST     | Register a new user                              |
| `/userlogin_check`     | POST     | Validate user credentials                        |
| `/detection`           | GET      | Tweet submission form                            |
| `/prediction`          | POST     | Run model inference & return result              |
| `/dl_evaluations`      | GET      | Run evaluation & display metrics + bar chart     |

### Typical User Flow

1. Register a new account at `/newuser`.
2. Login with your credentials at `/user_login`.
3. Click **Detection** → enter a tweet → submit.
4. View the result: **`ham`** or **`spam`**.
5. (Optional) Admin can visit `/dl_evaluations` to see model metrics.

---

## 🧠 Model Details

- **Architecture:** Sequential CNN
  - `Embedding` layer (vocab size × 100, weights = GloVe, `trainable=False`)
  - `Conv1D(128, kernel_size=5, activation='relu')`
  - `GlobalMaxPooling1D()`
  - `Dense(2, activation='softmax')` — 2 output classes
- **Loss Function:** `categorical_crossentropy`
- **Optimizer:** `adam`
- **Batch Size:** 64
- **Epochs:** 5 (in `Train_CNN.py`; `index.py` shows 10 for original config)
- **Sequence Length:** 100 tokens
- **Embedding Size:** 100-D (GloVe 6B)
- **Train/Test Split:** 75 / 25 (`random_state=7`)
- **Inference:** Tokenize → pad to 100 → `model.predict()` → `argmax` → `ham`/`spam`

The trained model is saved as `Detection/cnn_model.h5`, and the tokenizer as `Detection/tokenizer.pickle`.

---

## 📊 Dataset

- **File:** `Detection/dataset/twitter_dataset.csv`
- **Columns used:** `tweet` (text), `label` (`ham` / `spam`)
- **Encoding:** `latin-1`
- **Format:** CSV
- **Purpose:** Training & evaluation of the CNN classifier

> The dataset is loaded only when `Train_CNN.py` is executed (training) or when `/dl_evaluations` is hit.

---

## 📈 Evaluation Metrics

When the **DL Evaluations** page is opened, the system:

1. Re-loads the dataset.
2. Re-trains (or evaluates) the CNN on the train/test split.
3. Computes:
   - **Accuracy**
   - **Precision** (macro)
   - **Recall** (macro)
   - **F1-Score** (macro)
4. Renders a bar chart at `static/accuracy.png`.

Metrics are displayed in a table on the `dl_evaluations.html` page.

---

## 🔐 Default Credentials

| Role  | Username | Password |
|-------|----------|----------|
| Admin | `admin`  | `admin`  |
| User  | _(self-registered)_ | _(self-set)_ |

> ⚠️ Change the admin password in `Detection/index.py` (`adminlogin()` function) for production use. The user passwords are currently stored as plain text in MySQL — also a security concern addressed in [Future Enhancements](#-future-enhancements).

---

## 🧪 Sample Test Tweets

The file `Detection/samples.txt` includes the following examples you can paste into the detection form:

```
You have won a free mobile. call back.

Don't miss out! Subscribe to our newsletter for exclusive deals and discounts.

You've been selected for a special discount! Click here to redeem your exclusive offer.

Need a loan? We offer quick and easy approval. Apply now for cash in minutes!.
```

The first line is a typical spam message; the others are promotional-style spam examples. A genuine tweet about your day, a friend, or an opinion should be classified as `ham`.

---

## 🖼 Screenshots / Output

*(Add your own screenshots here)*

- **Landing Page** — `Detection/templates/index.html`
- **Login Page** — `Detection/templates/user_login.html`
- **Detection Result Page** — `Detection/templates/detection_result.html`
- **DL Evaluations Chart** — `Detection/static/accuracy.png`

> Example bar chart is generated automatically at `static/accuracy.png` after running `/dl_evaluations`.

---

## 🛟 Troubleshooting

| Issue | Possible Cause | Fix |
|-------|----------------|-----|
| `Access denied for user 'root'@'localhost'` | Wrong MySQL password | Update credentials in `Detection/DBConfig.py` |
| `ModuleNotFoundError: No module named 'flask'` | Dependencies not installed | Run `pip install -r requirements.txt` |
| `OSError: Unable to open file cnn_model.h5` | Wrong working directory or missing model | Ensure you run from the project root, and `Detection/cnn_model.h5` exists |
| `Port 4683 already in use` | Another process is using the port | Change `port=4683` in `Detection/index.py` to e.g. `5000` |
| TensorFlow installation fails | Python version incompatible | Use Python 3.9–3.11 for best TF 2.21 compatibility |
| App loads but `/prediction` errors | Tokenizer not found | Make sure `Detection/tokenizer.pickle` is present (regenerate by running `Train_CNN.py`) |

---

## 🚀 Future Enhancements

- **Password Hashing** — Use `bcrypt` / `werkzeug.security` to hash user passwords.
- **SQL Injection Protection** — Use parameterized queries (currently uses string concatenation).
- **Better Model** — Try LSTM, BiLSTM, or Transformer-based models (e.g., BERT) for higher accuracy.
- **Real-time Twitter API** — Fetch live tweets via the Twitter API v2 for classification.
- **Email Verification** — Verify email at registration.
- **Pagination & History** — Let users see their past predictions.
- **Deployment** — Containerize with Docker and deploy to AWS/GCP/Azure.
- **CI/CD** — Add GitHub Actions for linting & testing.

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Open a Pull Request.

Please open an issue first to discuss major changes.

---

## 📄 License

This project is provided for **educational purposes**. You are free to use, modify, and distribute it. If you plan to publish or commercialize it, please add an explicit license (e.g., MIT, Apache 2.0).

---

## 👤 Author

**Ganesh Areti**

- GitHub: `ganesh-0809`
- Project: `SourceCode_Twitter`

---

### 🙏 Acknowledgements

- **GloVe** — Pre-trained word embeddings by Stanford NLP.
- **TensorFlow / Keras** — Deep learning framework.
- **Flask** — Lightweight web framework.
- **scikit-learn** — ML utilities for evaluation metrics.
