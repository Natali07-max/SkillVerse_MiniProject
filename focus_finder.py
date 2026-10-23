import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="SkillVerse - Focus Finder",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# GAME HTML
# ============================================================

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

    color: #ffffff;

    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(124,58,237,0.24),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 90%,
            rgba(6,182,212,0.18),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #070712 0%,
            #0b0b18 50%,
            #090914 100%
        );

    overflow-x: hidden;
}

body::before {
    content: "";

    position: fixed;
    inset: 0;

    pointer-events: none;

    background-image:
        linear-gradient(
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        );

    background-size: 45px 45px;

    mask-image:
        linear-gradient(
            to bottom,
            black,
            transparent
        );
}

button {
    font-family: inherit;
}

.app {
    min-height: 900px;
    width: 100%;
    position: relative;
}

.glow {
    position: fixed;

    border-radius: 50%;

    filter: blur(100px);

    pointer-events: none;

    opacity: 0.24;
}

.glow.one {
    width: 270px;
    height: 270px;

    background: #7c3aed;

    top: 5%;
    left: 5%;
}

.glow.two {
    width: 250px;
    height: 250px;

    background: #06b6d4;

    right: 5%;
    bottom: 5%;
}

/* ============================================================
   SCREEN
   ============================================================ */

.screen {
    display: none;

    width: 100%;

    min-height: 900px;
}

.screen.active {
    display: flex;
}

/* ============================================================
   START SCREEN
   ============================================================ */

#startScreen {
    justify-content: center;
    align-items: center;

    padding: 30px;
}

.start-card {
    width: min(650px, 95%);

    padding: 55px 45px;

    text-align: center;

    background:
        rgba(15,15,30,0.91);

    border:
        1px solid rgba(139,92,246,0.30);

    border-radius: 28px;

    box-shadow:
        0 30px 100px rgba(0,0,0,0.55),
        0 0 80px rgba(124,58,237,0.12);

    backdrop-filter: blur(20px);
}

.mission {
    display: inline-flex;

    align-items: center;

    gap: 8px;

    padding: 8px 15px;

    border-radius: 999px;

    background:
        rgba(124,58,237,0.12);

    border:
        1px solid rgba(139,92,246,0.30);

    color: #c4b5fd;

    font-size: 13px;

    font-weight: 800;

    letter-spacing: 0.5px;
}

.logo {
    font-size: 72px;

    margin:
        25px 0 10px;

    filter:
        drop-shadow(
            0 0 20px
            rgba(124,58,237,0.65)
        );
}

.title {
    margin: 0;

    font-size:
        clamp(40px, 7vw, 68px);

    font-weight: 900;

    letter-spacing: -2px;

    background:
        linear-gradient(
            90deg,
            #a78bfa,
            #22d3ee,
            #c084fc
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.subtitle {
    color: #9ca3af;

    font-size: 17px;

    margin:
        14px auto 35px;

    max-width: 500px;

    line-height: 1.6;
}

.difficulty-label {
    text-align: left;

    margin-bottom: 10px;

    color: #d1d5db;

    font-size: 13px;

    font-weight: 800;
}

.difficulty {
    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 10px;

    margin-bottom: 25px;
}

.diff-btn {
    border:
        1px solid
        rgba(255,255,255,0.10);

    background:
        rgba(255,255,255,0.035);

    color: #a1a1aa;

    padding: 14px;

    border-radius: 14px;

    cursor: pointer;

    font-weight: 800;

    transition: 0.2s ease;
}

.diff-btn:hover {
    transform:
        translateY(-2px);

    border-color:
        rgba(124,58,237,0.5);
}

.diff-btn.selected {
    color: white;

    border-color:
        #8b5cf6;

    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,0.25),
            rgba(6,182,212,0.10)
        );

    box-shadow:
        0 0 25px
        rgba(124,58,237,0.18);
}

.start-btn {
    width: 100%;

    border: none;

    padding: 17px 25px;

    border-radius: 16px;

    color: white;

    font-size: 16px;

    font-weight: 900;

    cursor: pointer;

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #06b6d4
        );

    box-shadow:
        0 12px 35px
        rgba(124,58,237,0.30);

    transition: 0.2s ease;
}

.start-btn:hover {
    transform:
        translateY(-3px);

    box-shadow:
        0 18px 45px
        rgba(124,58,237,0.42);
}

.keyboard-hint {
    margin-top: 18px;

    color: #71717a;

    font-size: 12px;
}

/* ============================================================
   GAME SCREEN
   ============================================================ */

#gameScreen {
    justify-content: center;
    align-items: center;

    padding: 25px;
}

.game-content {
    width: min(900px,100%);

    margin: auto;
}

/* ============================================================
   TOP BAR
   ============================================================ */

.topbar {
    width: 100%;

    display: flex;

    justify-content:
        space-between;

    align-items: center;

    margin-bottom: 15px;
}

.brand {
    display: flex;

    align-items: center;

    gap: 10px;

    font-weight: 900;

    font-size: 18px;
}

.brand-icon {
    width: 38px;
    height: 38px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 12px;

    background:
        linear-gradient(
            135deg,
            rgba(124,58,237,0.35),
            rgba(6,182,212,0.25)
        );

    border:
        1px solid
        rgba(139,92,246,0.35);
}

.diff-badge {
    padding: 8px 13px;

    border-radius: 999px;

    background:
        rgba(255,255,255,0.05);

    border:
        1px solid
        rgba(255,255,255,0.08);

    color: #c4b5fd;

    font-size: 12px;

    font-weight: 800;
}

/* ============================================================
   HUD
   ============================================================ */

.hud {
    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 12px;

    margin-bottom: 15px;
}

.stat {
    padding: 14px 16px;

    background:
        rgba(18,18,35,0.80);

    border:
        1px solid
        rgba(255,255,255,0.07);

    border-radius: 16px;

    box-shadow:
        0 10px 35px
        rgba(0,0,0,0.18);
}

.stat-label {
    color: #71717a;

    font-size: 11px;

    text-transform: uppercase;

    letter-spacing: 1px;

    font-weight: 800;
}

.stat-value {
    margin-top: 4px;

    font-size: 22px;

    font-weight: 900;
}

.lives {
    color: #fb7185;
}

.combo {
    color: #fbbf24;
}

/* ============================================================
   PROGRESS
   ============================================================ */

.progress-container {
    width: 100%;

    height: 5px;

    background:
        rgba(255,255,255,0.06);

    border-radius: 999px;

    overflow: hidden;

    margin-bottom: 20px;
}

.progress {
    height: 100%;

    width: 0%;

    background:
        linear-gradient(
            90deg,
            #7c3aed,
            #06b6d4
        );

    border-radius: inherit;

    transition:
        width 0.3s ease;
}

/* ============================================================
   ROUND
   ============================================================ */

.round-info {
    text-align: center;

    color: #71717a;

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 8px;
}

/* ============================================================
   TIMER
   ============================================================ */

.timer-wrap {
    display: flex;

    justify-content: center;

    margin-bottom: 14px;
}

.timer {
    width: 64px;
    height: 64px;

    border-radius: 50%;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 19px;

    font-weight: 900;

    background:
        radial-gradient(
            circle,
            rgba(124,58,237,0.20),
            rgba(10,10,20,0.95)
        );

    border:
        2px solid
        rgba(139,92,246,0.45);

    box-shadow:
        0 0 30px
        rgba(124,58,237,0.15);
}

.timer.warning {
    border-color: #f59e0b;

    color: #fbbf24;
}

.timer.danger {
    border-color: #ef4444;

    color: #fb7185;

    animation:
        pulse 0.6s infinite;
}

@keyframes pulse {

    50% {
        transform: scale(1.07);
    }

}

/* ============================================================
   FOCUS CARD
   ============================================================ */

.focus-card {
    width: 100%;

    padding: 28px 25px 30px;

    text-align: center;

    background:
        linear-gradient(
            145deg,
            rgba(22,22,42,0.94),
            rgba(13,13,27,0.94)
        );

    border:
        1px solid
        rgba(139,92,246,0.18);

    border-radius: 25px;

    box-shadow:
        0 30px 80px
        rgba(0,0,0,0.30);
}

.focus-label {
    color: #8b5cf6;

    font-size: 12px;

    text-transform: uppercase;

    font-weight: 900;

    letter-spacing: 2px;

    margin-bottom: 7px;
}

.focus-instruction {
    color: #a1a1aa;

    font-size: 14px;

    margin-bottom: 20px;
}

/* ============================================================
   GRID
   ============================================================ */

.grid {
    width: min(650px,100%);

    margin: auto;

    display: grid;

    gap: 9px;

    padding: 10px;
}

.tile {
    aspect-ratio: 1 / 1;

    min-width: 0;

    border-radius: 13px;

    border:
        1px solid
        rgba(255,255,255,0.08);

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,0.065),
            rgba(255,255,255,0.025)
        );

    color: #ddd6fe;

    cursor: pointer;

    display: flex;

    align-items: center;

    justify-content: center;

    font-weight: 900;

    transition:
        transform 0.12s ease,
        border-color 0.15s ease,
        background 0.15s ease;

    box-shadow:
        inset 0 0 18px
        rgba(255,255,255,0.012);
}

.tile:hover {
    transform: scale(1.04);

    border-color:
        rgba(139,92,246,0.55);

    background:
        rgba(124,58,237,0.12);
}

.tile.different {
    background:
        linear-gradient(
            145deg,
            rgba(6,182,212,0.16),
            rgba(124,58,237,0.14)
        );

    border-color:
        rgba(34,211,238,0.20);
}

.tile.correct {
    border-color:
        #22c55e !important;

    background:
        rgba(34,197,94,0.20) !important;

    box-shadow:
        0 0 35px
        rgba(34,197,94,0.25);
}

.tile.wrong {
    border-color:
        #ef4444 !important;

    background:
        rgba(239,68,68,0.18) !important;

    box-shadow:
        0 0 35px
        rgba(239,68,68,0.20);
}

.tile.disabled {
    pointer-events: none;
}

/* ============================================================
   FEEDBACK
   ============================================================ */

.feedback {
    min-height: 28px;

    margin-top: 12px;

    font-size: 14px;

    font-weight: 900;
}

.feedback.correct {
    color: #4ade80;
}

.feedback.wrong {
    color: #fb7185;
}

.combo-message {
    height: 22px;

    color: #fbbf24;

    font-size: 13px;

    font-weight: 900;
}

/* ============================================================
   ANIMATIONS
   ============================================================ */

.correct-flash {
    animation:
        correctFlash 0.45s ease;
}

@keyframes correctFlash {

    50% {
        box-shadow:
            0 0 65px
            rgba(34,197,94,0.30);
    }

}

.shake {
    animation:
        shake 0.4s ease;
}

@keyframes shake {

    20% {
        transform:
            translateX(-8px);
    }

    40% {
        transform:
            translateX(8px);
    }

    60% {
        transform:
            translateX(-6px);
    }

    80% {
        transform:
            translateX(6px);
    }

}

/* ============================================================
   RESULT
   ============================================================ */

#resultScreen {
    justify-content: center;

    align-items: center;

    padding: 30px;
}

.result-card {
    width: min(700px,95%);

    padding: 45px 35px;

    text-align: center;

    background:
        linear-gradient(
            145deg,
            rgba(20,20,40,0.96),
            rgba(10,10,22,0.96)
        );

    border:
        1px solid
        rgba(139,92,246,0.25);

    border-radius: 28px;

    box-shadow:
        0 35px 100px
        rgba(0,0,0,0.55);
}

.result-icon {
    font-size: 65px;

    filter:
        drop-shadow(
            0 0 20px
            rgba(124,58,237,0.55)
        );
}

.result-title {
    margin:
        15px 0 5px;

    font-size: 38px;

    font-weight: 900;

    background:
        linear-gradient(
            90deg,
            #a78bfa,
            #22d3ee
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}

.result-subtitle {
    color: #9ca3af;

    margin-bottom: 30px;
}

.final-score {
    margin-bottom: 28px;
}

.score-number {
    font-size: 60px;

    font-weight: 900;

    color: white;

    text-shadow:
        0 0 30px
        rgba(124,58,237,0.45);
}

.score-label {
    color: #71717a;

    font-size: 12px;

    text-transform: uppercase;

    letter-spacing: 2px;

    font-weight: 800;
}

.rank {
    display: inline-block;

    padding: 9px 17px;

    border-radius: 999px;

    background:
        rgba(124,58,237,0.14);

    border:
        1px solid
        rgba(139,92,246,0.3);

    color: #c4b5fd;

    font-size: 13px;

    font-weight: 900;

    margin-bottom: 28px;
}

.result-stats {
    display: grid;

    grid-template-columns:
        repeat(3,1fr);

    gap: 12px;

    margin-bottom: 25px;
}

.result-stat {
    padding: 17px 10px;

    background:
        rgba(255,255,255,0.035);

    border:
        1px solid
        rgba(255,255,255,0.06);

    border-radius: 15px;
}

.result-stat-value {
    font-size: 21px;

    font-weight: 900;
}

.result-stat-label {
    margin-top: 4px;

    color: #71717a;

    font-size: 10px;

    text-transform: uppercase;

    letter-spacing: 0.8px;
}

.play-again {
    width: 100%;

    border: none;

    padding: 16px;

    border-radius: 15px;

    color: white;

    background:
        linear-gradient(
            135deg,
            #7c3aed,
            #06b6d4
        );

    font-size: 15px;

    font-weight: 900;

    cursor: pointer;

    transition: 0.2s ease;
}

.play-again:hover {
    transform:
        translateY(-2px);

    box-shadow:
        0 15px 40px
        rgba(124,58,237,0.3);
}

/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 650px) {

    .start-card {
        padding: 40px 22px;
    }

    .logo {
        font-size: 60px;
    }

    .difficulty {
        grid-template-columns: 1fr;
    }

    .hud {
        gap: 7px;
    }

    .stat {
        padding: 11px;
    }

    .stat-value {
        font-size: 18px;
    }

    .focus-card {
        padding:
            23px 10px 25px;
    }

    .grid {
        gap: 6px;

        padding: 5px;
    }

    .tile {
        border-radius: 9px;
    }

    .result-card {
        padding:
            35px 20px;
    }

    .result-stats {
        grid-template-columns:
            repeat(2,1fr);
    }

    .result-title {
        font-size: 31px;
    }

}

</style>
</head>

<body>

<div class="app">

<div class="glow one"></div>
<div class="glow two"></div>


<!-- ========================================================
     START SCREEN
     ======================================================== -->

<div id="startScreen" class="screen active">

<div class="start-card">

<div class="mission">
🎯 FOCUS & ATTENTION CHALLENGE
</div>

<div class="logo">
🎯
</div>

<h1 class="title">
Focus Finder
</h1>

<p class="subtitle">
Train your visual attention by finding the one
tile that is different from all the others.
</p>

<div class="difficulty-label">
SELECT DIFFICULTY
</div>

<div class="difficulty">

<button
class="diff-btn selected"
id="easyBtn"
onclick="selectDifficulty('easy')">
🟢 Easy
</button>

<button
class="diff-btn"
id="mediumBtn"
onclick="selectDifficulty('medium')">
🟡 Medium
</button>

<button
class="diff-btn"
id="hardBtn"
onclick="selectDifficulty('hard')">
🔴 Hard
</button>

</div>

<button
class="start-btn"
onclick="startGame()">
🚀 START FOCUS TEST
</button>

<div class="keyboard-hint">
Find the different tile as quickly as possible
</div>

</div>

</div>


<!-- ========================================================
     GAME SCREEN
     ======================================================== -->

<div id="gameScreen" class="screen">

<div class="game-content">

<div class="topbar">

<div class="brand">

<div class="brand-icon">
🎯
</div>

SkillVerse

</div>

<div
class="diff-badge"
id="difficultyBadge">
EASY
</div>

</div>


<div class="hud">

<div class="stat">

<div class="stat-label">
Score
</div>

<div
class="stat-value"
id="score">
0
</div>

</div>


<div class="stat">

<div class="stat-label">
Lives
</div>

<div
class="stat-value lives"
id="lives">
❤️❤️❤️
</div>

</div>


<div class="stat">

<div class="stat-label">
Combo
</div>

<div
class="stat-value combo"
id="combo">
×0
</div>

</div>

</div>


<div class="progress-container">

<div
class="progress"
id="progress">
</div>

</div>


<div
class="round-info"
id="roundInfo">
ROUND 1 / 10
</div>


<div class="timer-wrap">

<div
class="timer"
id="timer">
5
</div>

</div>


<div
class="focus-card"
id="focusCard">

<div class="focus-label">
FIND THE DIFFERENT TILE
</div>

<div class="focus-instruction">
One tile is different. Tap it!
</div>


<div
class="grid"
id="grid">
</div>


<div
class="feedback"
id="feedback">
</div>


<div
class="combo-message"
id="comboMessage">
</div>

</div>

</div>

</div>


<!-- ========================================================
     RESULT SCREEN
     ======================================================== -->

<div id="resultScreen" class="screen">

<div class="result-card">

<div
class="result-icon"
id="resultIcon">
🏆
</div>

<div
class="result-title"
id="resultTitle">
Focus Master
</div>

<div
class="result-subtitle"
id="resultSubtitle">
Your visual attention is excellent!
</div>


<div class="final-score">

<div
class="score-number"
id="finalScore">
0
</div>

<div class="score-label">
FINAL SCORE
</div>

</div>


<div
class="rank"
id="rank">
Focus Rookie
</div>


<div class="result-stats">

<div class="result-stat">

<div
class="result-stat-value"
id="correctStat">
0
</div>

<div class="result-stat-label">
Correct
</div>

</div>


<div class="result-stat">

<div
class="result-stat-value"
id="wrongStat">
0
</div>

<div class="result-stat-label">
Wrong
</div>

</div>


<div class="result-stat">

<div
class="result-stat-value"
id="accuracyStat">
0%
</div>

<div class="result-stat-label">
Accuracy
</div>

</div>


<div class="result-stat">

<div
class="result-stat-value"
id="bestComboStat">
×0
</div>

<div class="result-stat-label">
Best Combo
</div>

</div>


<div class="result-stat">

<div
class="result-stat-value"
id="bestTimeStat">
0ms
</div>

<div class="result-stat-label">
Best Reaction
</div>

</div>


<div class="result-stat">

<div
class="result-stat-value"
id="avgTimeStat">
0ms
</div>

<div class="result-stat-label">
Avg Reaction
</div>

</div>

</div>


<button
class="play-again"
onclick="restartGame()">
🔄 PLAY AGAIN
</button>

</div>

</div>

</div>


<script>

/* ============================================================
   CONFIG
   ============================================================ */

const CONFIG = {

    easy: {
        rounds: 10,
        time: 5.0,
        startGrid: 3,
        maxGrid: 5,
        multiplier: 1
    },

    medium: {
        rounds: 12,
        time: 4.0,
        startGrid: 4,
        maxGrid: 6,
        multiplier: 1.5
    },

    hard: {
        rounds: 15,
        time: 3.0,
        startGrid: 5,
        maxGrid: 7,
        multiplier: 2
    }

};


/* ============================================================
   GAME STATE
   ============================================================ */

let difficulty = "easy";

let currentRound = 0;

let score = 0;

let lives = 3;

let combo = 0;

let bestCombo = 0;

let correct = 0;

let wrong = 0;

let acceptingAnswer = false;

let timerInterval = null;

let timeLeft = 0;

let roundStartTime = 0;

let reactionTimes = [];

let bestTime = Infinity;

let currentDifferentIndex = -1;


/* ============================================================
   DIFFICULTY
   ============================================================ */

function selectDifficulty(level) {

    difficulty = level;

    document
        .querySelectorAll(".diff-btn")
        .forEach(btn => {
            btn.classList.remove("selected");
        });

    document
        .getElementById(level + "Btn")
        .classList.add("selected");

}


/* ============================================================
   START
   ============================================================ */

function startGame() {

    clearInterval(timerInterval);

    currentRound = 0;

    score = 0;

    lives = 3;

    combo = 0;

    bestCombo = 0;

    correct = 0;

    wrong = 0;

    reactionTimes = [];

    bestTime = Infinity;

    acceptingAnswer = false;

    document
        .getElementById("startScreen")
        .classList.remove("active");

    document
        .getElementById("resultScreen")
        .classList.remove("active");

    document
        .getElementById("gameScreen")
        .classList.add("active");

    document
        .getElementById("difficultyBadge")
        .textContent =
        difficulty.toUpperCase();

    updateHUD();

    nextRound();

}


/* ============================================================
   GRID SIZE
   ============================================================ */

function getGridSize() {

    const config =
        CONFIG[difficulty];

    let increase =
        Math.floor(
            (currentRound - 1) / 3
        );

    let size =
        config.startGrid + increase;

    return Math.min(
        size,
        config.maxGrid
    );

}


/* ============================================================
   CREATE ROUND
   ============================================================ */

function nextRound() {

    if (
        lives <= 0 ||
        currentRound >=
        CONFIG[difficulty].rounds
    ) {

        endGame();

        return;

    }

    currentRound++;

    acceptingAnswer = true;

    renderGrid();

    startTimer();

    updateHUD();

}


/* ============================================================
   GRID RENDER
   ============================================================ */

function renderGrid() {

    const grid =
        document.getElementById("grid");

    grid.innerHTML = "";

    const size =
        getGridSize();

    const total =
        size * size;

    currentDifferentIndex =
        Math.floor(
            Math.random() * total
        );

    grid.style.gridTemplateColumns =
        `repeat(${size}, 1fr)`;


    /*
       Use subtle visual differences.
       Normal tiles and different tile
       look very similar.
    */

    const baseBrightness =
        1;

    const difference =
        difficulty === "easy"
            ? 0.22
            : difficulty === "medium"
                ? 0.15
                : 0.09;


    for (
        let i = 0;
        i < total;
        i++
    ) {

        const tile =
            document.createElement("button");

        tile.className =
            "tile";


        if (
            i ===
            currentDifferentIndex
        ) {

            tile.classList.add(
                "different"
            );

            tile.style.filter =
                `brightness(${1 + difference})`;

        }

        else {

            tile.style.filter =
                `brightness(${baseBrightness})`;

        }


        tile.onclick =
            () => chooseTile(
                i,
                tile
            );


        grid.appendChild(tile);

    }


    document
        .getElementById("feedback")
        .textContent = "";

    document
        .getElementById("feedback")
        .className =
        "feedback";

    document
        .getElementById("comboMessage")
        .textContent = "";


    document
        .getElementById("roundInfo")
        .textContent =
        `ROUND ${currentRound} / ${CONFIG[difficulty].rounds}`;


    document
        .getElementById("progress")
        .style.width =
        `${((currentRound - 1) /
            CONFIG[difficulty].rounds) * 100}%`;

}


/* ============================================================
   TIMER
   ============================================================ */

function startTimer() {

    clearInterval(timerInterval);

    timeLeft =
        CONFIG[difficulty].time;

    updateTimer();

    roundStartTime =
        performance.now();

    timerInterval =
        setInterval(() => {

            timeLeft -= 0.05;

            if (timeLeft <= 0) {

                timeLeft = 0;

                updateTimer();

                clearInterval(
                    timerInterval
                );

                handleTimeout();

                return;

            }

            updateTimer();

        }, 50);

}


function updateTimer() {

    const timer =
        document.getElementById("timer");

    timer.textContent =
        timeLeft.toFixed(1);

    timer.classList.remove(
        "warning",
        "danger"
    );


    if (
        timeLeft <=
        CONFIG[difficulty].time * 0.40
    ) {

        timer.classList.add(
            "warning"
        );

    }


    if (timeLeft <= 1.2) {

        timer.classList.remove(
            "warning"
        );

        timer.classList.add(
            "danger"
        );

    }

}


/* ============================================================
   TILE SELECTION
   ============================================================ */

function chooseTile(
    index,
    tile
) {

    if (!acceptingAnswer) {
        return;
    }

    acceptingAnswer = false;

    clearInterval(timerInterval);


    const reaction =
        Math.round(
            performance.now() -
            roundStartTime
        );


    if (
        index ===
        currentDifferentIndex
    ) {

        tile.classList.add(
            "correct"
        );

        correct++;

        combo++;

        if (
            combo >
            bestCombo
        ) {

            bestCombo =
                combo;

        }

        reactionTimes.push(
            reaction
        );

        if (
            reaction <
            bestTime
        ) {

            bestTime =
                reaction;

        }


        /*
           SCORE
        */

        const config =
            CONFIG[difficulty];


        const base =
            100 *
            config.multiplier;


        const speedBonus =
            Math.max(
                0,
                Math.floor(
                    (config.time * 1000 -
                    reaction) / 15
                )
            ) *
            config.multiplier;


        const comboBonus =
            Math.max(
                0,
                (combo - 1) * 30
            );


        const earned =
            Math.round(
                base +
                speedBonus +
                comboBonus
            );


        score += earned;


        document
            .getElementById("feedback")
            .textContent =
            `✓ Excellent! +${earned} points`;


        document
            .getElementById("feedback")
            .className =
            "feedback correct";


        document
            .getElementById("focusCard")
            .classList.add(
                "correct-flash"
            );


        if (combo >= 2) {

            document
                .getElementById("comboMessage")
                .textContent =
                `🔥 ${combo}× FOCUS COMBO`;

        }


        updateHUD();


        setTimeout(() => {

            document
                .getElementById("focusCard")
                .classList.remove(
                    "correct-flash"
                );

            nextRound();

        }, 700);

    }

    else {

        tile.classList.add(
            "wrong"
        );

        wrong++;

        lives--;

        combo = 0;


        const tiles =
            document.querySelectorAll(
                ".tile"
            );


        if (
            tiles[
                currentDifferentIndex
            ]
        ) {

            tiles[
                currentDifferentIndex
            ].classList.add(
                "correct"
            );

        }


        tiles.forEach(
            t => {
                t.classList.add(
                    "disabled"
                );
            }
        );


        document
            .getElementById("feedback")
            .textContent =
            "✕ Wrong tile! Focus harder.";


        document
            .getElementById("feedback")
            .className =
            "feedback wrong";


        document
            .getElementById("focusCard")
            .classList.add(
                "shake"
            );


        updateHUD();


        setTimeout(() => {

            document
                .getElementById("focusCard")
                .classList.remove(
                    "shake"
                );


            if (
                lives <= 0
            ) {

                endGame();

            }

            else {

                nextRound();

            }

        }, 950);

    }

}


/* ============================================================
   TIMEOUT
   ============================================================ */

function handleTimeout() {

    if (!acceptingAnswer) {
        return;
    }

    acceptingAnswer = false;

    wrong++;

    lives--;

    combo = 0;


    const tiles =
        document.querySelectorAll(
            ".tile"
        );


    tiles.forEach(
        t => {
            t.classList.add(
                "disabled"
            );
        }
    );


    if (
        tiles[
            currentDifferentIndex
        ]
    ) {

        tiles[
            currentDifferentIndex
        ].classList.add(
            "correct"
        );

    }


    document
        .getElementById("feedback")
        .textContent =
        "⏱ Time's up! Find it faster.";


    document
        .getElementById("feedback")
        .className =
        "feedback wrong";


    document
        .getElementById("focusCard")
        .classList.add(
            "shake"
        );


    updateHUD();


    setTimeout(() => {

        document
            .getElementById("focusCard")
            .classList.remove(
                "shake"
            );


        if (
            lives <= 0
        ) {

            endGame();

        }

        else {

            nextRound();

        }

    }, 950);

}


/* ============================================================
   HUD
   ============================================================ */

function updateHUD() {

    document
        .getElementById("score")
        .textContent =
        score;


    document
        .getElementById("combo")
        .textContent =
        `×${combo}`;


    document
        .getElementById("lives")
        .textContent =
        "❤️".repeat(lives) +
        "🖤".repeat(3 - lives);

}


/* ============================================================
   END GAME
   ============================================================ */

function endGame() {

    clearInterval(
        timerInterval
    );

    acceptingAnswer = false;


    const total =
        correct + wrong;


    const accuracy =
        total > 0
            ? Math.round(
                correct / total * 100
            )
            : 0;


    const average =
        reactionTimes.length > 0
            ? Math.round(
                reactionTimes.reduce(
                    (a,b) => a + b,
                    0
                ) /
                reactionTimes.length
            )
            : 0;


    let rank;

    if (
        accuracy >= 90 &&
        bestTime <= 700
    ) {

        rank =
            "Ultimate Focus Master";

    }

    else if (
        accuracy >= 80
    ) {

        rank =
            "Focus Master";

    }

    else if (
        accuracy >= 65
    ) {

        rank =
            "Attention Expert";

    }

    else if (
        accuracy >= 45
    ) {

        rank =
            "Focus Learner";

    }

    else {

        rank =
            "Focus Rookie";

    }


    let icon = "🎯";

    let title =
        "Keep Training!";

    let subtitle =
        "Your attention improves with every challenge.";


    if (accuracy >= 80) {

        icon = "🏆";

        title =
            "Incredible Focus!";

        subtitle =
            "Your visual attention is seriously sharp.";

    }

    else if (accuracy >= 60) {

        icon = "🔥";

        title =
            "Great Focus!";

        subtitle =
            "You're getting faster at spotting differences.";

    }


    document
        .getElementById("resultIcon")
        .textContent =
        icon;


    document
        .getElementById("resultTitle")
        .textContent =
        title;


    document
        .getElementById("resultSubtitle")
        .textContent =
        subtitle;


    document
        .getElementById("finalScore")
        .textContent =
        score;


    document
        .getElementById("rank")
        .textContent =
        rank;


    document
        .getElementById("correctStat")
        .textContent =
        correct;


    document
        .getElementById("wrongStat")
        .textContent =
        wrong;


    document
        .getElementById("accuracyStat")
        .textContent =
        `${accuracy}%`;


    document
        .getElementById("bestComboStat")
        .textContent =
        `×${bestCombo}`;


    document
        .getElementById("bestTimeStat")
        .textContent =
        bestTime === Infinity
            ? "--"
            : `${bestTime}ms`;


    document
        .getElementById("avgTimeStat")
        .textContent =
        average > 0
            ? `${average}ms`
            : "--";


    document
        .getElementById("progress")
        .style.width =
        "100%";


    document
        .getElementById("gameScreen")
        .classList.remove(
            "active"
        );


    document
        .getElementById("resultScreen")
        .classList.add(
            "active"
        );

}


/* ============================================================
   RESTART
   ============================================================ */

function restartGame() {

    document
        .getElementById("resultScreen")
        .classList.remove(
            "active"
        );

    document
        .getElementById("startScreen")
        .classList.add(
            "active"
        );

}

</script>

</body>
</html>
"""


# ============================================================
# RENDER
# ============================================================

components.html(
    GAME_HTML,
    height=950,
    scrolling=False
)