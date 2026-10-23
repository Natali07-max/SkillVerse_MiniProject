import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SkillVerse | Memory Match",
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
    padding: 30px 18px;
}

.screen {
    width: min(1050px, 100%);
}

/* =========================
   START
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
    padding: 9px 15px;
    border-radius: 999px;
    background: rgba(0,229,255,.08);
    border: 1px solid rgba(0,229,255,.25);
    color: #67e8f9;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 1.5px;
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
    box-shadow: 0 20px 45px rgba(99,102,241,.4);
}

.keyboard {
    margin-top: 18px;
    color: #475569;
    font-size: 12px;
}

/* =========================
   GAME
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
}

/* HUD */

.hud {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 12px;
}

.stat {
    padding: 15px;
    border-radius: 16px;
    background: rgba(12,16,28,.8);
    border: 1px solid rgba(255,255,255,.08);
}

.stat-label {
    color: #64748b;
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.2px;
}

.stat-value {
    margin-top: 5px;
    font-size: 23px;
    font-weight: 900;
}

#score {
    color: #67e8f9;
}

#moves {
    color: #c084fc;
}

#lives {
    color: #fb7185;
}

#combo {
    color: #fbbf24;
}

/* PROGRESS */

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

/* ARENA */

.arena {
    position: relative;
    min-height: 600px;
    padding: 80px 30px 30px;
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
    min-width: 58px;
    height: 48px;
    padding: 0 12px;
    border-radius: 15px;
    border: 1px solid rgba(34,211,238,.25);
    display: flex;
    justify-content: center;
    align-items: center;
    color: #67e8f9;
    font-size: 15px;
    font-weight: 900;
}

/* =========================
   CARDS
========================= */

.card-grid {
    width: min(680px, 100%);
    margin: auto;
    display: grid;
    gap: 13px;
    justify-content: center;
}

.card {
    aspect-ratio: 1 / 1;
    min-width: 0;
    cursor: pointer;
    perspective: 900px;
}

.card-inner {
    width: 100%;
    height: 100%;
    position: relative;
    transition: transform .45s;
    transform-style: preserve-3d;
}

.card.flipped .card-inner,
.card.matched .card-inner {
    transform: rotateY(180deg);
}

.card-front,
.card-back {
    position: absolute;
    inset: 0;
    backface-visibility: hidden;
    border-radius: 16px;
}

.card-front {
    display: flex;
    justify-content: center;
    align-items: center;
    background:
        linear-gradient(
            135deg,
            rgba(34,211,238,.10),
            rgba(168,85,247,.10)
        );
    border: 1px solid rgba(168,85,247,.3);
    box-shadow:
        0 8px 25px rgba(0,0,0,.25);
}

.card-front::before {
    content: "?";
    color: #475569;
    font-size: 27px;
    font-weight: 900;
}

.card-back {
    display: flex;
    justify-content: center;
    align-items: center;
    transform: rotateY(180deg);
    background:
        radial-gradient(
            circle at 30% 25%,
            rgba(255,255,255,.15),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            rgba(6,182,212,.22),
            rgba(99,102,241,.22),
            rgba(168,85,247,.22)
        );
    border: 1px solid rgba(103,232,249,.4);
    box-shadow:
        0 0 25px rgba(34,211,238,.10);
    font-size: 35px;
}

.card.matched .card-back {
    border-color: rgba(74,222,128,.65);
    box-shadow:
        0 0 30px rgba(74,222,128,.16);
}

.card:hover .card-front {
    border-color: rgba(34,211,238,.5);
    transform: translateY(-2px);
}

.card.disabled {
    pointer-events: none;
}

/* FEEDBACK */

.feedback {
    position: absolute;
    left: 50%;
    bottom: 15px;
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

.good-flash {
    animation: goodFlash .4s;
}

.bad-shake {
    animation: badShake .35s;
}

@keyframes goodFlash {
    50% {
        box-shadow:
            inset 0 0 100px rgba(74,222,128,.14);
    }
}

@keyframes badShake {
    25% {
        transform: translateX(-7px);
    }

    75% {
        transform: translateX(7px);
    }
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

/* RESPONSIVE */

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
        min-height: 530px;
        padding: 75px 12px 25px;
    }

    .card-grid {
        gap: 8px;
    }

    .card-back {
        font-size: 25px;
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

<div id="startScreen">

    <div class="start-card">

        <div class="badge">
            🧠 SKILLVERSE GAME
        </div>

        <div class="logo">
            🧠
        </div>

        <h1>
            Memory Match
        </h1>

        <div class="subtitle">
            Flip the cards, remember their positions,
            and match every pair using the fewest
            moves possible.
        </div>

        <div class="difficulty-title">
            Select Difficulty
        </div>

        <div class="difficulty">

            <button
                class="diff-btn active"
                onclick="setDifficulty('easy', this)">
                Easy
            </button>

            <button
                class="diff-btn"
                onclick="setDifficulty('medium', this)">
                Medium
            </button>

            <button
                class="diff-btn"
                onclick="setDifficulty('hard', this)">
                Hard
            </button>

        </div>

        <button
            class="start-btn"
            onclick="startGame()">
            START GAME 🧠
        </button>

        <div class="keyboard">
            🃏 Flip → Remember → Match
        </div>

    </div>

</div>


<!-- =========================
     GAME SCREEN
========================= -->

<div
    class="game-screen"
    id="gameScreen">

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
                Moves
            </div>

            <div
                class="stat-value"
                id="moves">
                0
            </div>

        </div>


        <div class="stat">

            <div class="stat-label">
                Lives
            </div>

            <div
                class="stat-value"
                id="lives">
                ❤️❤️❤️
            </div>

        </div>


        <div class="stat">

            <div class="stat-label">
                Combo
            </div>

            <div
                class="stat-value"
                id="combo">
                0x
            </div>

        </div>

    </div>


    <div class="progress-wrap">

        <div
            class="progress"
            id="progress">
        </div>

    </div>


    <div
        class="arena"
        id="arena">

        <div
            class="round-info"
            id="roundInfo">
            MATCH 0 / 8
        </div>

        <div
            class="timer"
            id="timer">
            00:00
        </div>


        <div
            class="card-grid"
            id="cardGrid">
        </div>


        <div
            class="feedback"
            id="feedback">
        </div>

    </div>

</div>


<!-- =========================
     RESULT SCREEN
========================= -->

<div
    class="result-screen"
    id="resultScreen">

    <div class="result-card">

        <div
            class="result-icon"
            id="resultIcon">
            🏆
        </div>

        <div
            class="result-title"
            id="resultTitle">
            Memory Master!
        </div>

        <div class="result-sub">
            Your memory challenge is complete.
        </div>

        <div
            class="final-score"
            id="finalScore">
            0
        </div>

        <div
            class="rank"
            id="rank">
            MEMORY ROOKIE
        </div>


        <div class="result-stats">

            <div class="result-stat">

                <div
                    class="result-stat-value"
                    id="matchedPairs">
                    0
                </div>

                <div class="result-stat-label">
                    Pairs
                </div>

            </div>


            <div class="result-stat">

                <div
                    class="result-stat-value"
                    id="totalMoves">
                    0
                </div>

                <div class="result-stat-label">
                    Moves
                </div>

            </div>


            <div class="result-stat">

                <div
                    class="result-stat-value"
                    id="accuracy">
                    0%
                </div>

                <div class="result-stat-label">
                    Accuracy
                </div>

            </div>


            <div class="result-stat">

                <div
                    class="result-stat-value"
                    id="bestCombo">
                    0x
                </div>

                <div class="result-stat-label">
                    Best Combo
                </div>

            </div>


            <div class="result-stat">

                <div
                    class="result-stat-value"
                    id="timeTaken">
                    0s
                </div>

                <div class="result-stat-label">
                    Time
                </div>

            </div>


            <div class="result-stat">

                <div
                    class="result-stat-value"
                    id="mistakes">
                    0
                </div>

                <div class="result-stat-label">
                    Mistakes
                </div>

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
   SETTINGS
========================================= */

let difficulty = "easy";

const settings = {

    easy: {
        pairs: 6,
        gridColumns: 4,
        multiplier: 1
    },

    medium: {
        pairs: 8,
        gridColumns: 4,
        multiplier: 1.5
    },

    hard: {
        pairs: 10,
        gridColumns: 5,
        multiplier: 2
    }

};


/* =========================================
   SYMBOLS
========================================= */

const symbols = [
    "🚀",
    "🌟",
    "🎯",
    "⚡",
    "🔥",
    "💎",
    "🦊",
    "🐼",
    "🍕",
    "🎮",
    "🌈",
    "👑"
];


/* =========================================
   VARIABLES
========================================= */

let cards = [];

let flippedCards = [];

let matchedPairs = 0;

let moves = 0;

let mistakes = 0;

let score = 0;

let lives = 3;

let combo = 0;

let bestCombo = 0;

let gameActive = false;

let lockBoard = false;

let startTime = 0;

let timerInterval = null;


/* =========================================
   DIFFICULTY
========================================= */

function setDifficulty(level, button) {

    difficulty = level;

    document
        .querySelectorAll(".diff-btn")
        .forEach(btn => {
            btn.classList.remove("active");
        });

    button.classList.add("active");
}


/* =========================================
   START
========================================= */

function startGame() {

    clearInterval(timerInterval);

    const config =
        settings[difficulty];

    cards = [];

    flippedCards = [];

    matchedPairs = 0;

    moves = 0;

    mistakes = 0;

    score = 0;

    lives = 3;

    combo = 0;

    bestCombo = 0;

    lockBoard = false;

    gameActive = true;

    startTime = Date.now();

    document
        .getElementById("startScreen")
        .style.display = "none";

    document
        .getElementById("resultScreen")
        .style.display = "none";

    document
        .getElementById("gameScreen")
        .style.display = "block";

    document
        .getElementById("difficultyLabel")
        .textContent =
        difficulty.toUpperCase();

    createDeck();

    updateHUD();

    updateProgress();

    startClock();
}


/* =========================================
   CREATE DECK
========================================= */

function createDeck() {

    const pairSymbols =
        symbols.slice(
            0,
            settings[difficulty].pairs
        );

    cards = [
        ...pairSymbols,
        ...pairSymbols
    ];

    shuffle(cards);

    const grid =
        document.getElementById(
            "cardGrid"
        );

    grid.innerHTML = "";

    grid.style.gridTemplateColumns =
        `repeat(
            ${settings[difficulty].gridColumns},
            minmax(0, 1fr)
        )`;

    cards.forEach(
        (symbol, index) => {

            const card =
                document.createElement(
                    "div"
                );

            card.className = "card";

            card.dataset.symbol =
                symbol;

            card.dataset.index =
                index;

            card.innerHTML = `
                <div class="card-inner">

                    <div class="card-front"></div>

                    <div class="card-back">
                        ${symbol}
                    </div>

                </div>
            `;

            card.addEventListener(
                "click",
                () => flipCard(card)
            );

            grid.appendChild(card);
        }
    );

    document
        .getElementById("roundInfo")
        .textContent =
        "MATCH 0 / " +
        settings[difficulty].pairs;
}


/* =========================================
   SHUFFLE
========================================= */

function shuffle(array) {

    for (
        let i = array.length - 1;
        i > 0;
        i--
    ) {

        const j =
            Math.floor(
                Math.random() * (i + 1)
            );

        [
            array[i],
            array[j]
        ] = [
            array[j],
            array[i]
        ];
    }

    return array;
}


/* =========================================
   FLIP CARD
========================================= */

function flipCard(card) {

    if (
        !gameActive ||
        lockBoard ||
        card.classList.contains("flipped") ||
        card.classList.contains("matched")
    ) {
        return;
    }

    card.classList.add("flipped");

    flippedCards.push(card);

    if (flippedCards.length === 2) {

        moves++;

        checkMatch();
    }
}


/* =========================================
   CHECK MATCH
========================================= */

function checkMatch() {

    const first =
        flippedCards[0];

    const second =
        flippedCards[1];

    const match =
        first.dataset.symbol ===
        second.dataset.symbol;

    if (match) {

        handleMatch(
            first,
            second
        );

    } else {

        handleMismatch(
            first,
            second
        );
    }
}


/* =========================================
   MATCH
========================================= */

function handleMatch(
    first,
    second
) {

    first.classList.add("matched");

    second.classList.add("matched");

    matchedPairs++;

    combo++;

    if (combo > bestCombo) {
        bestCombo = combo;
    }

    const base =
        100 *
        settings[difficulty].multiplier;

    const comboBonus =
        (combo - 1) * 35;

    const moveBonus =
        Math.max(
            0,
            40 - moves
        );

    const points =
        Math.round(
            base +
            comboBonus +
            moveBonus
        );

    score += points;

    showFeedback(
        "✓ MATCH! +" + points,
        true
    );

    flashArena(true);

    flippedCards = [];

    updateHUD();

    updateProgress();

    document
        .getElementById("roundInfo")
        .textContent =
        "MATCH " +
        matchedPairs +
        " / " +
        settings[difficulty].pairs;

    if (
        matchedPairs ===
        settings[difficulty].pairs
    ) {

        setTimeout(
            endGame,
            700
        );
    }
}


/* =========================================
   MISMATCH
========================================= */

function handleMismatch(
    first,
    second
) {

    mistakes++;

    lives--;

    combo = 0;

    lockBoard = true;

    showFeedback(
        "✕ NO MATCH  ❤️ -1",
        false
    );

    flashArena(false);

    updateHUD();

    setTimeout(() => {

        first.classList.remove(
            "flipped"
        );

        second.classList.remove(
            "flipped"
        );

        flippedCards = [];

        lockBoard = false;

        if (lives <= 0) {

            setTimeout(
                endGame,
                300
            );
        }

    }, 850);
}


/* =========================================
   HUD
========================================= */

function updateHUD() {

    document
        .getElementById("score")
        .textContent =
        score.toLocaleString();

    document
        .getElementById("moves")
        .textContent =
        moves;

    document
        .getElementById("lives")
        .textContent =
        "❤️".repeat(
            Math.max(0, lives)
        ) +
        "🖤".repeat(
            Math.max(0, 3 - lives)
        );

    document
        .getElementById("combo")
        .textContent =
        combo + "x";
}


/* =========================================
   PROGRESS
========================================= */

function updateProgress() {

    const total =
        settings[difficulty].pairs;

    const percent =
        (matchedPairs / total) * 100;

    document
        .getElementById("progress")
        .style.width =
        percent + "%";
}


/* =========================================
   TIMER
========================================= */

function startClock() {

    timerInterval =
        setInterval(() => {

            if (!gameActive) return;

            const elapsed =
                Math.floor(
                    (Date.now() - startTime) /
                    1000
                );

            const minutes =
                Math.floor(
                    elapsed / 60
                );

            const seconds =
                elapsed % 60;

            document
                .getElementById("timer")
                .textContent =
                String(minutes).padStart(
                    2,
                    "0"
                ) +
                ":" +
                String(seconds).padStart(
                    2,
                    "0"
                );

        }, 250);
}


/* =========================================
   FEEDBACK
========================================= */

function showFeedback(
    text,
    good
) {

    const element =
        document.getElementById(
            "feedback"
        );

    element.textContent = text;

    element.className =
        "feedback show " +
        (
            good
                ? "good"
                : "bad"
        );

    setTimeout(() => {

        element.classList.remove(
            "show"
        );

    }, 550);
}


/* =========================================
   ARENA EFFECT
========================================= */

function flashArena(good) {

    const arena =
        document.getElementById(
            "arena"
        );

    arena.classList.remove(
        "good-flash",
        "bad-shake"
    );

    void arena.offsetWidth;

    arena.classList.add(
        good
            ? "good-flash"
            : "bad-shake"
    );
}


/* =========================================
   END GAME
========================================= */

function endGame() {

    if (!gameActive) return;

    gameActive = false;

    clearInterval(timerInterval);

    const totalAttempts =
        matchedPairs + mistakes;

    const accuracy =
        totalAttempts > 0
            ? Math.round(
                (
                    matchedPairs /
                    totalAttempts
                ) * 100
              )
            : 0;

    const time =
        Math.floor(
            (Date.now() - startTime) /
            1000
        );

    document
        .getElementById("gameScreen")
        .style.display =
        "none";

    document
        .getElementById("resultScreen")
        .style.display =
        "block";

    document
        .getElementById("finalScore")
        .textContent =
        score.toLocaleString();

    document
        .getElementById("matchedPairs")
        .textContent =
        matchedPairs;

    document
        .getElementById("totalMoves")
        .textContent =
        moves;

    document
        .getElementById("accuracy")
        .textContent =
        accuracy + "%";

    document
        .getElementById("bestCombo")
        .textContent =
        bestCombo + "x";

    document
        .getElementById("timeTaken")
        .textContent =
        time + "s";

    document
        .getElementById("mistakes")
        .textContent =
        mistakes;


    let title;
    let rank;
    let icon;


    if (
        matchedPairs ===
        settings[difficulty].pairs &&
        accuracy >= 90
    ) {

        title =
            "Memory Master!";

        rank =
            "👑 MEMORY LEGEND";

        icon =
            "👑";

    } else if (
        matchedPairs >=
        settings[difficulty].pairs * .75 &&
        accuracy >= 70
    ) {

        title =
            "Excellent Memory!";

        rank =
            "🔥 MEMORY EXPERT";

        icon =
            "🔥";

    } else if (
        matchedPairs >=
        settings[difficulty].pairs * .5
    ) {

        title =
            "Great Work!";

        rank =
            "🎯 MEMORY PRO";

        icon =
            "🎯";

    } else {

        title =
            "Keep Practicing!";

        rank =
            "💪 MEMORY ROOKIE";

        icon =
            "💪";
    }


    document
        .getElementById("resultTitle")
        .textContent =
        title;

    document
        .getElementById("rank")
        .textContent =
        rank;

    document
        .getElementById("resultIcon")
        .textContent =
        icon;
}


/* =========================================
   ENTER = START
========================================= */

document.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter" &&
            document
                .getElementById("startScreen")
                .style.display !== "none"
        ) {

            startGame();

        }

    }
);

</script>

</body>
</html>
"""

components.html(
    GAME_HTML,
    height=930,
    scrolling=False
)