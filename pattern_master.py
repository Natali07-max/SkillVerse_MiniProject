import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SkillVerse | Pattern Master",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GAME_HTML = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
    font-family: Inter, Arial, sans-serif;
    background: #05070d;
    color: #fff;
    overflow-x: hidden;
}

body {
    background:
        radial-gradient(circle at 15% 15%, rgba(0,229,255,.10), transparent 28%),
        radial-gradient(circle at 85% 20%, rgba(168,85,247,.12), transparent 30%),
        radial-gradient(circle at 50% 100%, rgba(236,72,153,.08), transparent 35%),
        #05070d;
}

body::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    opacity: .22;
    background-image:
        linear-gradient(rgba(255,255,255,.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.035) 1px, transparent 1px);
    background-size: 42px 42px;
}

.stApp {
    background: transparent !important;
}

header,
footer,
[data-testid="stToolbar"] {
    display: none !important;
}

.game-wrapper {
    width: 100%;
    min-height: 870px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 35px 20px;
    position: relative;
}

.screen {
    width: min(1050px, 100%);
    position: relative;
}

/* =========================
   START SCREEN
========================= */

.start-card {
    max-width: 680px;
    margin: auto;
    padding: 48px 45px;
    text-align: center;
    border-radius: 30px;
    background: rgba(12,16,28,.88);
    border: 1px solid rgba(255,255,255,.10);
    box-shadow:
        0 30px 100px rgba(0,0,0,.55),
        0 0 70px rgba(0,229,255,.05);
    backdrop-filter: blur(20px);
}

.badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 15px;
    border-radius: 999px;
    background: rgba(0,229,255,.08);
    border: 1px solid rgba(0,229,255,.25);
    color: #67e8f9;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.logo {
    font-size: 72px;
    margin: 25px 0 8px;
    filter: drop-shadow(0 0 25px rgba(168,85,247,.4));
}

h1 {
    margin: 0;
    font-size: clamp(42px, 7vw, 70px);
    line-height: 1;
    font-weight: 900;
    letter-spacing: -3px;
    background: linear-gradient(
        90deg,
        #67e8f9,
        #60a5fa,
        #c084fc,
        #f472b6
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    margin: 18px auto 30px;
    max-width: 500px;
    color: #94a3b8;
    font-size: 16px;
    line-height: 1.7;
}

.difficulty-title {
    color: #64748b;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.difficulty {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 28px;
}

.diff-btn {
    border: 1px solid rgba(255,255,255,.10);
    background: rgba(255,255,255,.035);
    color: #94a3b8;
    padding: 12px 22px;
    border-radius: 12px;
    cursor: pointer;
    font-weight: 700;
    transition: .2s;
}

.diff-btn:hover {
    border-color: rgba(168,85,247,.45);
    color: white;
}

.diff-btn.active {
    background:
        linear-gradient(
            135deg,
            rgba(0,229,255,.18),
            rgba(168,85,247,.18)
        );
    border-color: #a855f7;
    color: white;
    box-shadow: 0 0 25px rgba(168,85,247,.12);
}

.start-btn {
    width: 100%;
    border: none;
    padding: 17px;
    border-radius: 15px;
    color: white;
    font-size: 16px;
    font-weight: 900;
    cursor: pointer;
    background:
        linear-gradient(
            135deg,
            #06b6d4,
            #6366f1,
            #a855f7
        );
    box-shadow: 0 15px 35px rgba(99,102,241,.28);
    transition: .2s;
}

.start-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 20px 45px rgba(99,102,241,.40);
}

.keyboard {
    margin-top: 18px;
    color: #475569;
    font-size: 12px;
}

/* =========================
   GAME SCREEN
========================= */

.game-screen {
    display: none;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 18px;
}

.brand {
    font-size: 17px;
    font-weight: 900;
    letter-spacing: .5px;
}

.brand span {
    color: #22d3ee;
}

.game-diff {
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(168,85,247,.10);
    border: 1px solid rgba(168,85,247,.3);
    color: #c084fc;
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
}

.hud {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 12px;
}

.stat {
    padding: 16px;
    border-radius: 16px;
    background: rgba(12,16,28,.8);
    border: 1px solid rgba(255,255,255,.08);
}

.stat-label {
    color: #64748b;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.2px;
    text-transform: uppercase;
}

.stat-value {
    margin-top: 5px;
    font-size: 25px;
    font-weight: 900;
}

#score {
    color: #67e8f9;
}

#level {
    color: #c084fc;
}

#lives {
    color: #fb7185;
}

#streak {
    color: #fbbf24;
}

.progress-wrap {
    height: 4px;
    margin: 18px 0;
    border-radius: 10px;
    overflow: hidden;
    background: rgba(255,255,255,.06);
}

.progress {
    height: 100%;
    width: 0%;
    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #818cf8,
            #c084fc
        );
    transition: width .3s;
}

/* =========================
   ARENA
========================= */

.arena {
    height: 560px;
    position: relative;
    overflow: hidden;
    border-radius: 26px;
    border: 1px solid rgba(255,255,255,.09);
    background:
        radial-gradient(
            circle at center,
            rgba(30,41,59,.22),
            transparent 60%
        ),
        rgba(5,8,15,.88);
    box-shadow: inset 0 0 70px rgba(0,0,0,.35);
}

.round-info {
    position: absolute;
    top: 22px;
    left: 25px;
    color: #64748b;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1px;
}

.timer {
    position: absolute;
    top: 18px;
    right: 22px;
    width: 55px;
    height: 55px;
    border-radius: 50%;
    border: 2px solid rgba(168,85,247,.30);
    display: flex;
    justify-content: center;
    align-items: center;
    color: #c084fc;
    font-size: 15px;
    font-weight: 900;
    box-shadow: 0 0 25px rgba(168,85,247,.08);
}

.instruction {
    position: absolute;
    top: 90px;
    left: 0;
    right: 0;
    text-align: center;
    color: #64748b;
    font-size: 13px;
}

/* =========================
   PATTERN
========================= */

.pattern-display {
    position: absolute;
    top: 135px;
    left: 50%;
    transform: translateX(-50%);
    width: 92%;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    min-height: 75px;
}

.pattern-item {
    width: 52px;
    height: 52px;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    font-weight: 900;
    font-family: "Courier New", monospace;
    color: #e0f2fe;
    background:
        linear-gradient(
            135deg,
            rgba(34,211,238,.16),
            rgba(168,85,247,.16)
        );
    border: 1px solid rgba(168,85,247,.35);
    box-shadow: 0 0 20px rgba(168,85,247,.08);
    animation: patternAppear .35s ease both;
}

@keyframes patternAppear {
    from {
        opacity: 0;
        transform: translateY(10px) scale(.8);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

/* =========================
   MEMORY MASK
========================= */

.memory-message {
    position: absolute;
    top: 235px;
    left: 0;
    right: 0;
    text-align: center;
}

.memory-icon {
    font-size: 40px;
    margin-bottom: 8px;
}

.memory-title {
    font-size: 21px;
    font-weight: 900;
}

.memory-sub {
    margin-top: 6px;
    color: #64748b;
    font-size: 13px;
}

/* =========================
   INPUT
========================= */

.input-area {
    display: none;
    position: absolute;
    left: 50%;
    bottom: 65px;
    transform: translateX(-50%);
    width: min(650px, 90%);
    text-align: center;
}

.input-label {
    color: #94a3b8;
    font-size: 13px;
    margin-bottom: 12px;
}

.pattern-input {
    width: 100%;
    padding: 17px 20px;
    border-radius: 15px;
    border: 1px solid rgba(168,85,247,.35);
    outline: none;
    background: rgba(255,255,255,.045);
    color: white;
    text-align: center;
    font-size: 18px;
    font-weight: 800;
    font-family: "Courier New", monospace;
    letter-spacing: 7px;
    transition: .2s;
}

.pattern-input:focus {
    border-color: #22d3ee;
    box-shadow: 0 0 25px rgba(34,211,238,.10);
}

.submit-btn {
    width: 100%;
    margin-top: 12px;
    border: none;
    padding: 15px;
    border-radius: 13px;
    color: white;
    font-weight: 900;
    cursor: pointer;
    background: linear-gradient(
        135deg,
        #06b6d4,
        #6366f1,
        #a855f7
    );
}

/* =========================
   FEEDBACK
========================= */

.feedback {
    position: absolute;
    left: 50%;
    bottom: 20px;
    transform: translateX(-50%);
    font-size: 16px;
    font-weight: 900;
    opacity: 0;
    transition: .2s;
    white-space: nowrap;
}

.feedback.show {
    opacity: 1;
}

.feedback.good {
    color: #4ade80;
    text-shadow: 0 0 18px rgba(74,222,128,.45);
}

.feedback.bad {
    color: #fb7185;
    text-shadow: 0 0 18px rgba(251,113,133,.45);
}

/* =========================
   RESULT
========================= */

.result-screen {
    display: none;
    max-width: 720px;
    margin: auto;
}

.result-card {
    padding: 45px;
    text-align: center;
    border-radius: 30px;
    background: rgba(12,16,28,.9);
    border: 1px solid rgba(255,255,255,.09);
    box-shadow: 0 30px 100px rgba(0,0,0,.5);
}

.result-icon {
    font-size: 65px;
}

.result-title {
    font-size: 40px;
    font-weight: 900;
    margin-top: 10px;
}

.result-sub {
    color: #64748b;
    margin: 10px 0 28px;
}

.final-score {
    font-size: 65px;
    font-weight: 900;
    background:
        linear-gradient(
            90deg,
            #22d3ee,
            #818cf8,
            #c084fc
        );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.rank {
    display: inline-block;
    margin: 5px 0 28px;
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(168,85,247,.12);
    border: 1px solid rgba(168,85,247,.25);
    color: #c084fc;
    font-weight: 900;
}

.result-stats {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 12px;
    margin-bottom: 25px;
}

.result-stat {
    padding: 18px 10px;
    border-radius: 15px;
    background: rgba(255,255,255,.035);
    border: 1px solid rgba(255,255,255,.06);
}

.result-stat-value {
    font-size: 24px;
    font-weight: 900;
}

.result-stat-label {
    margin-top: 5px;
    color: #64748b;
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1px;
}

/* =========================
   ANIMATIONS
========================= */

.correct-flash {
    animation: correctFlash .45s;
}

.wrong-shake {
    animation: wrongShake .35s;
}

@keyframes correctFlash {
    0%,100% {
        box-shadow: inset 0 0 0 rgba(74,222,128,0);
    }

    50% {
        box-shadow:
            inset 0 0 100px rgba(74,222,128,.15);
    }
}

@keyframes wrongShake {
    0%,100% {
        transform: translateX(0);
    }

    25% {
        transform: translateX(-8px);
    }

    75% {
        transform: translateX(8px);
    }
}

/* =========================
   RESPONSIVE
========================= */

@media(max-width:700px) {

    .game-wrapper {
        padding: 18px 10px;
    }

    .start-card,
    .result-card {
        padding: 30px 20px;
    }

    .logo {
        font-size: 58px;
    }

    .difficulty {
        flex-wrap: wrap;
    }

    .diff-btn {
        flex: 1;
        min-width: 90px;
    }

    .hud {
        grid-template-columns: repeat(2,1fr);
    }

    .arena {
        height: 520px;
    }

    .pattern-display {
        flex-wrap: wrap;
        padding: 0 15px;
    }

    .pattern-item {
        width: 44px;
        height: 44px;
        font-size: 21px;
    }

    .result-stats {
        grid-template-columns: 1fr 1fr;
    }
}
</style>
</head>

<body>

<div class="game-wrapper">

<div class="screen">

<!-- =========================
     START SCREEN
========================= -->

<div class="start-screen" id="startScreen">

    <div class="start-card">

        <div class="badge">
            🧠 SKILLVERSE GAME
        </div>

        <div class="logo">
            🧠
        </div>

        <h1>
            Pattern Master
        </h1>

        <div class="subtitle">
            Watch the pattern carefully.
            Memorize every letter and number and reproduce
            them in exactly the right order.
        </div>

        <div class="difficulty-title">
            Select Difficulty
        </div>

        <div class="difficulty">

            <button
                class="diff-btn active"
                onclick="setDifficulty('easy',this)">
                Easy
            </button>

            <button
                class="diff-btn"
                onclick="setDifficulty('medium',this)">
                Medium
            </button>

            <button
                class="diff-btn"
                onclick="setDifficulty('hard',this)">
                Hard
            </button>

        </div>

        <button
            class="start-btn"
            onclick="startGame()">
            START GAME 🧠
        </button>

        <div class="keyboard">
            👁️ Memorize → Type the pattern → Submit
        </div>

    </div>

</div>


<!-- =========================
     GAME SCREEN
========================= -->

<div class="game-screen" id="gameScreen">

    <div class="topbar">

        <div class="brand">
            SKILL<span>VERSE</span> 🧠
        </div>

        <div
            class="game-diff"
            id="difficultyLabel">
            EASY
        </div>

    </div>


    <div class="hud">

        <div class="stat">
            <div class="stat-label">Score</div>
            <div class="stat-value" id="score">0</div>
        </div>

        <div class="stat">
            <div class="stat-label">Level</div>
            <div class="stat-value" id="level">1</div>
        </div>

        <div class="stat">
            <div class="stat-label">Lives</div>
            <div class="stat-value" id="lives">❤️❤️❤️</div>
        </div>

        <div class="stat">
            <div class="stat-label">Streak</div>
            <div class="stat-value" id="streak">0x</div>
        </div>

    </div>


    <div class="progress-wrap">
        <div class="progress" id="progress"></div>
    </div>


    <div class="arena" id="arena">

        <div class="round-info" id="roundInfo">
            LEVEL 1
        </div>

        <div class="timer" id="timer">
            0
        </div>

        <div class="instruction">
            MEMORIZE THE PATTERN
        </div>

        <div class="pattern-display" id="patternDisplay"></div>

        <div class="memory-message" id="memoryMessage">

            <div class="memory-icon">👀</div>

            <div class="memory-title">Memorize...</div>

            <div class="memory-sub">
                The pattern will disappear soon
            </div>

        </div>

        <div class="input-area" id="inputArea">

            <div class="input-label">
                Enter the letters and numbers in the exact order
            </div>

            <input
                id="patternInput"
                class="pattern-input"
                maxlength="20"
                autocomplete="off"
                placeholder="TYPE HERE"
            >

            <button
                class="submit-btn"
                onclick="submitPattern()">
                SUBMIT PATTERN ✓
            </button>

        </div>

        <div class="feedback" id="feedback"></div>

    </div>

</div>


<!-- =========================
     RESULT SCREEN
========================= -->

<div class="result-screen" id="resultScreen">

    <div class="result-card">

        <div class="result-icon" id="resultIcon">🏆</div>

        <div class="result-title" id="resultTitle">
            Pattern Master!
        </div>

        <div class="result-sub">
            Your memory challenge is complete.
        </div>

        <div class="final-score" id="finalScore">0</div>

        <div class="rank" id="rank">MEMORY ROOKIE</div>

        <div class="result-stats">

            <div class="result-stat">
                <div class="result-stat-value" id="completed">0</div>
                <div class="result-stat-label">Levels</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="accuracy">0%</div>
                <div class="result-stat-label">Accuracy</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="longest">0</div>
                <div class="result-stat-label">Best Pattern</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="correct">0</div>
                <div class="result-stat-label">Correct</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="wrong">0</div>
                <div class="result-stat-label">Wrong</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="bestStreak">0x</div>
                <div class="result-stat-label">Best Streak</div>
            </div>

        </div>

        <button
            class="start-btn"
            onclick="startGame()">
            PLAY AGAIN 🧠
        </button>

    </div>

</div>

</div>
</div>


<script>

/* =========================================
   GAME SETTINGS
========================================= */

let difficulty = "easy";

const settings = {

    easy: {
        startLength: 3,
        maxLevels: 10,
        displayTime: 1700,
        multiplier: 1
    },

    medium: {
        startLength: 4,
        maxLevels: 12,
        displayTime: 1400,
        multiplier: 1.5
    },

    hard: {
        startLength: 5,
        maxLevels: 15,
        displayTime: 1050,
        multiplier: 2
    }

};


/* =========================================
   SYMBOL SET (letters + numbers)
   Look-alikes O, I, Q, 0, 1 are left out
========================================= */

const symbols = [
    "A","B","C","D","E","F","G","H","J","K",
    "L","M","N","P","R","S","T","U","W","X",
    "Y","Z","2","3","4","5","6","7","8","9"
];


/* =========================================
   VARIABLES
========================================= */

let score = 0;
let lives = 3;
let level = 0;
let streak = 0;
let bestStreak = 0;
let correct = 0;
let wrong = 0;
let longestPattern = 0;
let currentPattern = [];
let gameActive = false;
let inputEnabled = false;
let timerInterval = null;


/* =========================================
   DIFFICULTY
========================================= */

function setDifficulty(levelName, button) {

    difficulty = levelName;

    document
        .querySelectorAll(".diff-btn")
        .forEach(btn => {
            btn.classList.remove("active");
        });

    button.classList.add("active");
}


/* =========================================
   START GAME
========================================= */

function startGame() {

    clearInterval(timerInterval);

    score = 0;
    lives = 3;
    level = 0;
    streak = 0;
    bestStreak = 0;
    correct = 0;
    wrong = 0;
    longestPattern = 0;
    currentPattern = [];
    gameActive = true;
    inputEnabled = false;

    document.getElementById("startScreen").style.display = "none";
    document.getElementById("resultScreen").style.display = "none";
    document.getElementById("gameScreen").style.display = "block";

    document.getElementById("difficultyLabel").textContent =
        difficulty.toUpperCase();

    updateHUD();

    nextLevel();
}


/* =========================================
   MEMORIZE MESSAGE
========================================= */

function setMemoryMessage(icon, title, sub) {

    const box = document.getElementById("memoryMessage");

    box.innerHTML = `
        <div class="memory-icon">${icon}</div>
        <div class="memory-title">${title}</div>
        <div class="memory-sub">${sub}</div>
    `;

    box.style.display = "block";
}


/* =========================================
   NEXT LEVEL
========================================= */

function nextLevel() {

    if (!gameActive) return;

    if (
        level >= settings[difficulty].maxLevels ||
        lives <= 0
    ) {
        endGame();
        return;
    }

    level++;

    inputEnabled = false;

    document.getElementById("inputArea").style.display = "none";

    setMemoryMessage(
        "👀",
        "Memorize...",
        "The pattern will disappear soon"
    );

    document.getElementById("patternDisplay").innerHTML = "";

    document.getElementById("roundInfo").textContent =
        "LEVEL " + level + " / " + settings[difficulty].maxLevels;

    updateProgress();

    generatePattern();

    showPattern();
}


/* =========================================
   GENERATE PATTERN
========================================= */

function generatePattern() {

    const length =
        settings[difficulty].startLength + level - 1;

    currentPattern = [];

    for (let i = 0; i < length; i++) {

        const randomIndex =
            Math.floor(Math.random() * symbols.length);

        currentPattern.push(symbols[randomIndex]);
    }

    if (currentPattern.length > longestPattern) {
        longestPattern = currentPattern.length;
    }
}


/* =========================================
   SHOW PATTERN
========================================= */

function showPattern() {

    const display = document.getElementById("patternDisplay");

    display.innerHTML = "";

    currentPattern.forEach((symbol, index) => {

        const item = document.createElement("div");

        item.className = "pattern-item";

        item.textContent = symbol;

        item.style.animationDelay = (index * 0.08) + "s";

        display.appendChild(item);
    });

    startMemoryTimer();
}


/* =========================================
   MEMORY TIMER
========================================= */

function startMemoryTimer() {

    clearInterval(timerInterval);

    let remaining = settings[difficulty].displayTime;

    updateTimer(remaining);

    timerInterval = setInterval(() => {

        remaining -= 50;

        updateTimer(remaining);

        if (remaining <= 0) {

            clearInterval(timerInterval);

            hidePattern();
        }

    }, 50);
}


/* =========================================
   TIMER DISPLAY
========================================= */

function updateTimer(milliseconds) {

    const seconds = Math.max(0, milliseconds / 1000);

    document.getElementById("timer").textContent =
        seconds.toFixed(1);
}


/* =========================================
   HIDE PATTERN
========================================= */

function hidePattern() {

    document.getElementById("patternDisplay").innerHTML = "";

    setMemoryMessage(
        "🧠",
        "Your turn!",
        "Enter the letters and numbers exactly as shown"
    );

    document.getElementById("inputArea").style.display = "block";

    document.getElementById("timer").textContent = "GO";

    inputEnabled = true;

    const input = document.getElementById("patternInput");

    input.value = "";

    input.focus();
}


/* =========================================
   SUBMIT
========================================= */

function submitPattern() {

    if (!gameActive || !inputEnabled) {
        return;
    }

    const input =
        document
            .getElementById("patternInput")
            .value
            .trim()
            .toUpperCase();

    if (!input) {
        return;
    }

    inputEnabled = false;

    const expected = currentPattern.join("").toUpperCase();

    if (input === expected) {
        handleCorrect();
    } else {
        handleWrong(input);
    }
}


/* =========================================
   CORRECT
========================================= */

function handleCorrect() {

    correct++;

    streak++;

    if (streak > bestStreak) {
        bestStreak = streak;
    }

    const basePoints = 100 * settings[difficulty].multiplier;

    const levelBonus = level * 25;

    const streakBonus = (streak - 1) * 40;

    const points = Math.round(basePoints + levelBonus + streakBonus);

    score += points;

    showFeedback("✓ PERFECT! +" + points, true);

    flashArena(true);

    updateHUD();

    setTimeout(nextLevel, 700);
}


/* =========================================
   WRONG
========================================= */

function handleWrong(input) {

    wrong++;

    lives--;

    streak = 0;

    showFeedback("✕ WRONG PATTERN  ❤️ -1", false);

    flashArena(false);

    updateHUD();

    if (lives <= 0) {

        setTimeout(endGame, 750);

        return;
    }

    setTimeout(() => {

        /* Repeat the same level after a mistake. */

        inputEnabled = false;

        document.getElementById("inputArea").style.display = "none";

        setMemoryMessage(
            "🔄",
            "Try Again",
            "Watch the pattern carefully"
        );

        showPattern();

    }, 850);
}


/* =========================================
   HUD
========================================= */

function updateHUD() {

    document.getElementById("score").textContent =
        score.toLocaleString();

    document.getElementById("level").textContent = level;

    document.getElementById("lives").textContent =
        "❤️".repeat(Math.max(0, lives)) +
        "🖤".repeat(Math.max(0, 3 - lives));

    document.getElementById("streak").textContent = streak + "x";
}


/* =========================================
   PROGRESS
========================================= */

function updateProgress() {

    const total = settings[difficulty].maxLevels;

    const percent = ((level - 1) / total) * 100;

    document.getElementById("progress").style.width =
        percent + "%";
}


/* =========================================
   FEEDBACK
========================================= */

function showFeedback(text, good) {

    const element = document.getElementById("feedback");

    element.textContent = text;

    element.className = "feedback show " + (good ? "good" : "bad");

    setTimeout(() => {
        element.classList.remove("show");
    }, 600);
}


/* =========================================
   ARENA EFFECT
========================================= */

function flashArena(good) {

    const arena = document.getElementById("arena");

    arena.classList.remove("correct-flash", "wrong-shake");

    void arena.offsetWidth;

    arena.classList.add(good ? "correct-flash" : "wrong-shake");
}


/* =========================================
   END GAME
========================================= */

function endGame() {

    gameActive = false;

    inputEnabled = false;

    clearInterval(timerInterval);

    document.getElementById("gameScreen").style.display = "none";

    document.getElementById("resultScreen").style.display = "block";

    document.getElementById("finalScore").textContent =
        score.toLocaleString();

    const attempts = correct + wrong;

    const accuracy =
        attempts > 0
            ? Math.round((correct / attempts) * 100)
            : 0;

    document.getElementById("completed").textContent = correct;
    document.getElementById("accuracy").textContent = accuracy + "%";
    document.getElementById("longest").textContent = longestPattern;
    document.getElementById("correct").textContent = correct;
    document.getElementById("wrong").textContent = wrong;
    document.getElementById("bestStreak").textContent = bestStreak + "x";

    let title;
    let rank;
    let icon;

    if (correct >= 10 && accuracy >= 90) {

        title = "Your Memory Is Elite!";
        rank = "🧠 PATTERN MASTER";
        icon = "👑";

    } else if (correct >= 7 && accuracy >= 75) {

        title = "Amazing Memory!";
        rank = "🔥 MEMORY EXPERT";
        icon = "🔥";

    } else if (correct >= 4 && accuracy >= 60) {

        title = "Great Job!";
        rank = "🎯 PATTERN PRO";
        icon = "🎯";

    } else {

        title = "Keep Training!";
        rank = "💪 MEMORY ROOKIE";
        icon = "💪";
    }

    document.getElementById("resultTitle").textContent = title;
    document.getElementById("rank").textContent = rank;
    document.getElementById("resultIcon").textContent = icon;
}


/* =========================================
   ENTER KEY
========================================= */

document.addEventListener("keydown", function(event) {

    if (event.key === "Enter" && inputEnabled) {
        submitPattern();
    }

});


/* =========================================
   ONLY LETTERS AND NUMBERS IN INPUT
========================================= */

document
    .getElementById("patternInput")
    .addEventListener("input", function() {

        this.value =
            this.value
                .replace(/[^a-zA-Z0-9]/g, "")
                .toUpperCase();

    });

</script>

</body>
</html>
"""

components.html(
    GAME_HTML,
    height=920,
    scrolling=False
)