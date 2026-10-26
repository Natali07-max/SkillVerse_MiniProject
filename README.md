# SkillVerse 
### Think Better. Play Better. Grow Better.

SkillVerse AI is an AI-powered, gamified learning platform designed to help students and professionals strengthen cognitive skills through interactive games and engaging challenges. The platform focuses on improving memory, concentration, logical reasoning, pattern recognition, numerical ability, and reaction speed.

## Features

- **Login Interface:** A React-based login page with email and password fields.
- **Game Hub:** A Streamlit dashboard that provides access to all available cognitive games.
- **Focus Finder:** Improves attention and concentration through visual identification challenges.
- **Memory Match:** Strengthens visual memory by matching hidden pairs.
- **Number Ninja:** Develops numerical ability and mental calculation speed.
- **Pattern Master:** Encourages pattern recognition and logical reasoning.
- **Reaction Rush:** Challenges reaction speed and decision-making.
- **Sequence Solver:** Develops logical thinking through number-sequence puzzles.
- **Difficulty Levels:** Games can offer different difficulty settings.
- **Interactive Interface:** A modern interface with game cards, progress indicators, and feedback.

## Technology Stack

| Component | Technologies |
|---|---|
| Frontend and login interface | React.js, JavaScript, CSS |
| Game dashboard | Streamlit |
| Backend and game logic | Python |
| Navigation | React Router, Streamlit page navigation |
| Icons | Lucide React |
| Version control | Git and GitHub |

## Project Structure

```text
SkillVerse/
├── frontend/
│   └── src/
│       ├── Login.jsx
│       ├── App.jsx
│       └── ...
├── game_hub.py
├── pages/
│   ├── focus_finder.py
│   ├── memory_match.py
│   ├── number_ninja.py
│   ├── pattern_master.py
│   ├── reaction_rush.py
│   └── sequence_solver.py
├── requirements.txt
└── README.md
```

*Note: Adjust the folder structure above to match your actual repository.*

## Installation and Setup

### Prerequisites

- Python 3.10 or later
- Node.js and npm
- Git
- Visual Studio Code or another code editor

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd SkillVerse
```

Replace the placeholder with your actual GitHub repository URL.

### 2. Install Python Dependencies

Create and activate a virtual environment.

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

Install Streamlit:

```bash
pip install streamlit
```

If a `requirements.txt` file exists, install all project dependencies using:

```bash
pip install -r requirements.txt
```

### 3. Start the Streamlit Game Hub

From the directory containing `game_hub.py`, run:

```bash
streamlit run game_hub.py --server.port 8501
```

Open the displayed local URL, usually:

```text
http://localhost:8501
```

### 4. Start the React Frontend

Open a separate terminal and navigate to the React application's directory.

Install the dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Open the local URL displayed in the terminal.

### 5. Connect Login to the Game Hub

The React login page redirects to the Streamlit Game Hub at:

```text
http://localhost:8501
```

Ensure both applications are running before testing the redirect.

**Authentication note:** The current demo login implementation checks whether the fields are filled in but does not verify credentials against a database. Production deployment requires secure, server-side authentication.

## How to Use

1. Start the React frontend and Streamlit Game Hub.
2. Open the login page.
3. Enter your email and password.
4. Continue to the SkillVerse Game Hub.
5. Select any available game using the **Play Now** button.
6. Follow the instructions and complete the challenge.
7. Return to the Game Hub to explore other games.

## Project Objectives

- Make cognitive-skill development interactive and engaging.
- Encourage consistent practice through gamification.
- Provide a centralized platform for multiple brain-training games.
- Offer a user-friendly and visually consistent experience.
- Establish a foundation for future personalization and learning analytics.

## Future Enhancements

- Secure registration and login with database integration.
- Persistent user profiles and game history.
- XP points, levels, achievements, and leaderboards.
- Personalized game recommendations.
- Performance dashboards and progress tracking.
- AI-based analysis of gameplay performance.
- Adaptive difficulty based on user performance.
- Mobile-responsive improvements and deployment.

## Scope

SkillVerse AI can be extended for use by students, educators, professionals, and organizations seeking interactive cognitive exercises. Future versions may incorporate analytics and personalization to help users understand their performance over time.

## Contributors

Developed as an academic software project focused on gamified learning and cognitive skill development.

**Project:** SkillVerse AI  
**Domain:** Artificial Intelligence, Gamification, and Cognitive Learning

## License

This project is intended for educational and research purposes. Add a suitable open-source license, such as the MIT License, if you intend to distribute the project under those terms.
