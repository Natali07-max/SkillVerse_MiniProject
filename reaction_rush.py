
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="SkillVerse | Sequence Solver",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="collapsed"
)

GAME_HTML = r"""
<!DOCTYPE html>
<html lang="en">
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
    z-index: 0;
}

button {
    font: inherit;
}

.game-wrapper {
    width: 100%;
    min-height: 100vh;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    padding: 35px 20px;
    position: relative;
    z-index: 1;
}

.screen {
    width: min(1050px, 100%);
    position: relative;
}

/* START SCREEN */

.start-screen {
    display: block;
}

.start-card {
    max-width: 700px;
    margin: 20px auto;
    padding: 45px;
    text-align: center;
    border-radius: 30px;
    background: rgba(12,16,28,.90);
    border: 1px solid rgba(255,255,255,.10);
    box-shadow: 0 30px 100px rgba(0,0,0,.55);
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
    font-size: 68px;
    margin: 22px 0 10px;
    filter: drop-shadow(0 0 25px rgba(0,229,255,.35));
}

h1 {
    margin: 0;
    font-size: clamp(38px, 6vw, 66px);
    line-height: 1.05;
    font-weight: 900;
    letter-spacing: -2px;
    background: linear-gradient(90deg,#67e8f9,#60a5fa,#c084fc,#f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    margin: 18px auto 30px;
    max-width: 500px;
    color: #94a3b8;
    font-size: 15px;
    line-height: 1.8;
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
    border-color: #22d3ee;
    color: white;
}

.diff-btn.active {
    background: linear-gradient(
        135deg,
        rgba(0,229,255,.18),
        rgba(168,85,247,.18)
    );
    border-color: #22d3ee;
    color: white;
    box-shadow: 0 0 25px rgba(34,211,238,.12);
}

.start-btn {
    width: 100%;
    border: none;
    padding: 17px;
    border-radius: 15px;
    color: white;
    font-size: 15px;
    font-weight: 900;
    cursor: pointer;
    background: linear-gradient(135deg,#06b6d4,#6366f1,#a855f7);
    box-shadow: 0 15px 35px rgba(99,102,241,.28);
    transition: .2s;
}

.start-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 20px 45px rgba(99,102,241,.40);
}

.keyboard {
    margin-top: 18px;
    color: #64748b;
    font-size: 12px;
}

/* GAME */

.game-screen {
    display: none;
}

.topbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 15px;
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
    grid-template-columns: repeat(3,1fr);
    gap: 12px;
}

.stat {
    padding: 16px;
    border-radius: 16px;
    background: rgba(12,16,28,.85);
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

#combo {
    color: #c084fc;
}

#lives {
    color: #fb7185;
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
    background: linear-gradient(90deg,#22d3ee,#818cf8,#c084fc);
    transition: width .3s;
}

/* PUZZLE AREA */

.arena {
    position: relative;
    min-height: 470px;
    padding: 30px;
    border-radius: 26px;
    border: 1px solid rgba(255,255,255,.09);
    background:
        radial-gradient(circle at center,rgba(30,41,59,.25),transparent 65%),
        rgba(5,8,15,.88);
    box-shadow: inset 0 0 70px rgba(0,0,0,.35);
}

.round-info {
    color: #64748b;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.puzzle-heading {
    margin-top: 30px;
    text-align: center;
    color: #94a3b8;
    font-size: 13px;
}

.question {
    margin: 14px auto 8px;
    text-align: center;
    color: #f8fafc;
    font-size: clamp(27px,4vw,43px);
    font-weight: 900;
    letter-spacing: 1px;
    overflow-wrap: anywhere;
    line-height: 1.5;
}

.question .missing {
    color: #67e8f9;
    text-shadow: 0 0 22px rgba(34,211,238,.45);
}

.hint {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin: 12px 0 28px;
}

.options {
    display: grid;
    grid-template-columns: repeat(2,minmax(0,1fr));
    gap: 13px;
    max-width: 620px;
    margin: 0 auto;
}

.option-btn {
    min-height: 66px;
    padding: 16px;
    border-radius: 15px;
    border: 1px solid rgba(255,255,255,.10);
    background: rgba(255,255,255,.035);
    color: #e2e8f0;
    font-size: 21px;
    font-weight: 800;
    cursor: pointer;
    transition: .18s;
}

.option-btn:hover:not(:disabled) {
    border-color: #22d3ee;
    background: rgba(34,211,238,.09);
    transform: translateY(-2px);
}

.option-btn:disabled {
    cursor: default;
    opacity: .85;
}

.option-btn.correct {
    border-color: #4ade80;
    background: rgba(74,222,128,.14);
    color: #4ade80;
}

.option-btn.wrong {
    border-color: #fb7185;
    background: rgba(251,113,133,.12);
    color: #fb7185;
}

.feedback {
    min-height: 28px;
    margin-top: 22px;
    text-align: center;
    font-size: 14px;
    font-weight: 800;
}

.feedback.good {
    color: #4ade80;
}

.feedback.bad {
    color: #fb7185;
}

.next-btn {
    display: none;
    max-width: 300px;
    margin: 12px auto 0;
    border: 1px solid rgba(34,211,238,.3);
    border-radius: 12px;
    padding: 13px 20px;
    background: rgba(34,211,238,.10);
    color: #67e8f9;
    font-weight: 800;
    cursor: pointer;
}

.next-btn:hover {
    background: rgba(34,211,238,.2);
}

.tip {
    margin-top: 18px;
    text-align: center;
    color: #475569;
    font-size: 11px;
}

/* RESULT */

.result-screen {
    display: none;
    max-width: 760px;
    margin: 20px auto;
}

.result-card {
    padding: 40px;
    text-align: center;
    border-radius: 30px;
    background: rgba(12,16,28,.92);
    border: 1px solid rgba(255,255,255,.09);
    box-shadow: 0 30px 100px rgba(0,0,0,.5);
}

.result-icon {
    font-size: 65px;
}

.result-title {
    font-size: clamp(30px,5vw,40px);
    font-weight: 900;
    margin-top: 10px;
}

.result-sub {
    color: #64748b;
    margin: 10px 0 25px;
}

.final-score {
    font-size: 65px;
    font-weight: 900;
    background: linear-gradient(90deg,#22d3ee,#818cf8,#c084fc);
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
    grid-template-columns: repeat(3,minmax(0,1fr));
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
        padding: 15px 10px;
    }

    .start-card,
    .result-card {
        padding: 28px 18px;
    }

    .logo {
        font-size: 55px;
    }

    .difficulty {
        flex-wrap: wrap;
    }

    .diff-btn {
        flex: 1;
        min-width: 80px;
        padding: 12px;
    }

    .arena {
        padding: 20px 14px;
        min-height: 440px;
    }

    .question {
        margin-top: 22px;
    }

    .options {
        gap: 9px;
    }

    .option-btn {
        min-height: 58px;
        padding: 12px 6px;
        font-size: 18px;
    }

    .result-stats {
        grid-template-columns: repeat(2,minmax(0,1fr));
    }

    .hud {
        gap: 7px;
    }

    .stat {
        padding: 12px 9px;
    }

    .stat-value {
        font-size: 21px;
    }
}

@media(prefers-reduced-motion:reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
</head>

<body>
<div class="game-wrapper">
<div class="screen">

<!-- START SCREEN -->

<div class="start-screen" id="startScreen">
    <div class="start-card">

        <div class="badge">🧩 SKILLVERSE GAME</div>
        <div class="logo">🧩</div>
        <h1>Sequence Solver</h1>

        <div class="subtitle">
            Train your brain to recognize patterns.
            Analyze the sequence, discover the hidden rule,
            and choose the correct answer.
        </div>

        <div class="difficulty-title">Select Difficulty</div>

        <div class="difficulty">
            <button class="diff-btn active"
                onclick="setDifficulty('easy',this)">Easy</button>

            <button class="diff-btn"
                onclick="setDifficulty('medium',this)">Medium</button>

            <button class="diff-btn"
                onclick="setDifficulty('hard',this)">Hard</button>
        </div>

        <button class="start-btn" onclick="startGame()">
            START GAME →
        </button>

        <div class="keyboard">
            🔍 Find the pattern • Think logically • Solve the sequence
        </div>
    </div>
</div>

<!-- GAME SCREEN -->

<div class="game-screen" id="gameScreen">

    <div class="topbar">
        <div class="brand">SKILL<span>VERSE</span> 🧩</div>
        <div class="game-diff" id="difficultyLabel">EASY</div>
    </div>

    <div class="hud">
        <div class="stat">
            <div class="stat-label">Score</div>
            <div class="stat-value" id="score">0</div>
        </div>

        <div class="stat">
            <div class="stat-label">Lives</div>
            <div class="stat-value" id="lives">❤️❤️❤️</div>
        </div>

        <div class="stat">
            <div class="stat-label">Combo</div>
            <div class="stat-value" id="combo">0x</div>
        </div>
    </div>

    <div class="progress-wrap">
        <div class="progress" id="progress"></div>
    </div>

    <div class="arena">

        <div class="round-info" id="roundInfo">ROUND 1 / 10</div>

        <div class="puzzle-heading">
            STUDY THE SEQUENCE
        </div>

        <div class="question" id="question"></div>

        <div class="hint" id="hint">
            What number comes next?
        </div>

        <div class="options" id="options"></div>

        <div class="feedback" id="feedback" aria-live="polite"></div>

        <button class="next-btn" id="nextBtn" onclick="nextRound()">
            NEXT QUESTION →
        </button>

        <div class="tip">
            Correct answer = points • Wrong answer = one life lost
        </div>
    </div>
</div>

<!-- RESULT SCREEN -->

<div class="result-screen" id="resultScreen">
    <div class="result-card">

        <div class="result-icon" id="resultIcon">🏆</div>
        <div class="result-title" id="resultTitle">Well Played!</div>

        <div class="result-sub">
            Your sequence-solving session is complete.
        </div>

        <div class="final-score" id="finalScore">0</div>
        <div class="rank" id="rank">PATTERN BEGINNER</div>

        <div class="result-stats">
            <div class="result-stat">
                <div class="result-stat-value" id="correctCount">0</div>
                <div class="result-stat-label">Correct</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="wrongCount">0</div>
                <div class="result-stat-label">Incorrect</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="accuracy">0%</div>
                <div class="result-stat-label">Accuracy</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="bestCombo">0x</div>
                <div class="result-stat-label">Best Combo</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="questionsDone">0</div>
                <div class="result-stat-label">Questions</div>
            </div>

            <div class="result-stat">
                <div class="result-stat-value" id="completion">0%</div>
                <div class="result-stat-label">Completed</div>
            </div>
        </div>

        <button class="start-btn" onclick="startGame()">
            PLAY AGAIN ↻
        </button>
    </div>
</div>

</div>
</div>

<script>
"use strict";

/* GAME CONFIGURATION */

let difficulty = "easy";

const settings = {
    easy: {
        rounds: 10,
        multiplier: 1,
        points: 100
    },
    medium: {
        rounds: 12,
        multiplier: 1.5,
        points: 150
    },
    hard: {
        rounds: 15,
        multiplier: 2,
        points: 200
    }
};

/*
 Each question contains:
 sequence, answer, choices, and a pattern explanation.
 Choices are validated against the answer.
*/

const questions = {

easy: [
    {
        sequence: [2, 4, 6, 8, 10],
        answer: "12",
        choices: ["11", "12", "14", "16"],
        explanation: "Add 2 each time."
    },
    {
        sequence: [5, 10, 15, 20, 25],
        answer: "30",
        choices: ["28", "30", "35", "40"],
        explanation: "Add 5 each time."
    },
    {
        sequence: [1, 2, 4, 8, 16],
        answer: "32",
        choices: ["24", "30", "32", "36"],
        explanation: "Multiply each number by 2."
    },
    {
        sequence: [3, 6, 9, 12, 15],
        answer: "18",
        choices: ["16", "18", "20", "21"],
        explanation: "Add 3 each time."
    },
    {
        sequence: [20, 18, 16, 14, 12],
        answer: "10",
        choices: ["8", "9", "10", "11"],
        explanation: "Subtract 2 each time."
    },
    {
        sequence: [1, 4, 9, 16, 25],
        answer: "36",
        choices: ["30", "32", "36", "49"],
        explanation: "These are consecutive square numbers."
    },
    {
        sequence: [2, 3, 4, 5, 6],
        answer: "7",
        choices: ["7", "8", "9", "10"],
        explanation: "Add 1 each time."
    },
    {
        sequence: [10, 20, 30, 40, 50],
        answer: "60",
        choices: ["55", "60", "65", "70"],
        explanation: "Add 10 each time."
    },
    {
        sequence: [1, 3, 5, 7, 9],
        answer: "11",
        choices: ["10", "11", "12", "13"],
        explanation: "The sequence contains consecutive odd numbers."
    },
    {
        sequence: [64, 32, 16, 8, 4],
        answer: "2",
        choices: ["1", "2", "3", "4"],
        explanation: "Divide by 2 each time."
    },
    {
        sequence: [4, 8, 12, 16, 20],
        answer: "24",
        choices: ["22", "24", "26", "28"],
        explanation: "Add 4 each time."
    },
    {
        sequence: [1, 1, 2, 3, 5],
        answer: "8",
        choices: ["6", "7", "8", "10"],
        explanation: "Add the previous two terms."
    }
],

medium: [
    {
        sequence: [2, 6, 12, 20, 30],
        answer: "42",
        choices: ["40", "42", "44", "46"],
        explanation: "The differences are 4, 6, 8, 10, then 12."
    },
    {
        sequence: [3, 7, 15, 31, 63],
        answer: "127",
        choices: ["95", "125", "127", "129"],
        explanation: "Multiply by 2 and add 1."
    },
    {
        sequence: [81, 27, 9, 3],
        answer: "1",
        choices: ["0", "1", "2", "3"],
        explanation: "Divide by 3 each time."
    },
    {
        sequence: [1, 4, 10, 19, 31],
        answer: "46",
        choices: ["43", "45", "46", "48"],
        explanation: "Add 3, 6, 9, 12, then 15."
    },
    {
        sequence: [2, 5, 11, 23, 47],
        answer: "95",
        choices: ["91", "93", "95", "97"],
        explanation: "Multiply by 2 and add 1."
    },
    {
        sequence: [1, 8, 27, 64],
        answer: "125",
        choices: ["100", "121", "125", "144"],
        explanation: "These are consecutive cube numbers."
    },
    {
        sequence: [50, 45, 37, 26, 12],
        answer: "-5",
        choices: ["-2", "-3", "-5", "0"],
        explanation: "Subtract 5, 8, 11, 14, then 17."
    },
    {
        sequence: [2, 3, 5, 8, 12],
        answer: "17",
        choices: ["15", "16", "17", "18"],
        explanation: "Add 1, 2, 3, 4, then 5."
    },
    {
        sequence: [1, 2, 6, 24, 120],
        answer: "720",
        choices: ["600", "620", "720", "840"],
        explanation: "Multiply successively by 2, 3, 4, 5, then 6."
    },
    {
        sequence: [7, 14, 12, 24, 22, 44],
        answer: "42",
        choices: ["40", "42", "46", "48"],
        explanation: "Alternate between multiplying by 2 and subtracting 2."
    },
    {
        sequence: [4, 9, 19, 39, 79],
        answer: "159",
        choices: ["149", "157", "159", "161"],
        explanation: "Multiply by 2 and add 1."
    },
    {
        sequence: [1, 5, 14, 30, 55],
        answer: "91",
        choices: ["81", "84", "91", "96"],
        explanation: "Add 4, 9, 16, 25, then 36."
    }
],

hard: [
    {
        sequence: [2, 5, 11, 23, 47],
        answer: "95",
        choices: ["93", "95", "97", "99"],
        explanation: "Each term is twice the previous term plus 1."
    },
    {
        sequence: [3, 4, 7, 12, 19, 28],
        answer: "39",
        choices: ["37", "38", "39", "41"],
        explanation: "Add consecutive odd numbers: 1, 3, 5, 7, 9, then 11."
    },
    {
        sequence: [2, 6, 18, 54],
        answer: "162",
        choices: ["108", "144", "162", "216"],
        explanation: "Multiply by 3 each time."
    },
    {
        sequence: [1, 4, 13, 40, 121],
        answer: "364",
        choices: ["360", "362", "364", "366"],
        explanation: "Multiply by 3 and add 1."
    },
    {
        sequence: [100, 96, 88, 76, 60],
        answer: "40",
        choices: ["36", "38", "40", "42"],
        explanation: "Subtract 4, 8, 12, 16, then 20."
    },
    {
        sequence: [2, 3, 5, 9, 17, 33],
        answer: "65",
        choices: ["63", "64", "65", "67"],
        explanation: "Multiply by 2 and subtract 1."
    },
    {
        sequence: [1, 2, 5, 14, 41],
        answer: "122",
        choices: ["120", "121", "122", "124"],
        explanation: "Multiply by 3 and subtract 1."
    },
    {
        sequence: [6, 11, 21, 36, 56],
        answer: "81",
        choices: ["76", "79", "81", "86"],
        explanation: "Add 5, 10, 15, 20, then 25."
    },
    {
        sequence: [2, 10, 30, 68, 130],
        answer: "222",
        choices: ["210", "216", "222", "230"],
        explanation: "The terms follow n cubed plus n, for n = 1, 2, 3, 4, 5, 6."
    },
    {
        sequence: [3, 8, 18, 38, 78],
        answer: "158",
        choices: ["148", "156", "158", "160"],
        explanation: "Multiply by 2 and add 2."
    },
    {
        sequence: [1, 3, 12, 60, 360],
        answer: "2520",
        choices: ["2160", "2400", "2520", "2880"],
        explanation: "Multiply by 3, 4, 5, 6, then 7."
    },
    {
        sequence: [5, 7, 11, 19, 35, 67],
        answer: "131",
        choices: ["127", "129", "131", "135"],
        explanation: "Add 2, 4, 8, 16, 32, then 64."
    },
    {
        sequence: [2, 12, 36, 80, 150],
        answer: "252",
        choices: ["240", "250", "252", "256"],
        explanation: "Terms follow n squared times (n + 1), for n = 1, 2, 3, 4, 5, 6."
    },
    {
        sequence: [7, 14, 28, 56, 112],
        answer: "224",
        choices: ["196", "210", "224", "238"],
        explanation: "Multiply by 2 each time."
    },
    {
        sequence: [1, 4, 9, 16, 25, 36],
        answer: "49",
        choices: ["42", "45", "49", "64"],
        explanation: "These are consecutive square numbers."
    }
]};

/* STATE */

let score = 0;
let lives = 3;
let combo = 0;
let bestCombo = 0;
let round = 0;
let correct = 0;
let wrong = 0;
let gameActive = false;
let questionLocked = false;
let currentQuestions = [];
let currentQuestion = null;
let answeredCount = 0;

/* HELPERS */

function shuffle(array) {
    const result = [...array];

    for (let i = result.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [result[i], result[j]] = [result[j], result[i]];
    }

    return result;
}

function setDifficulty(level, button) {
    difficulty = level;

    document.querySelectorAll(".diff-btn").forEach(btn => {
        btn.classList.remove("active");
    });

    button.classList.add("active");
}

/* START GAME */

function startGame() {
    score = 0;
    lives = 3;
    combo = 0;
    bestCombo = 0;
    round = 0;
    correct = 0;
    wrong = 0;
    answeredCount = 0;
    questionLocked = false;
    gameActive = true;

    currentQuestions = shuffle(questions[difficulty])
        .slice(0, settings[difficulty].rounds);

    document.getElementById("startScreen").style.display = "none";
    document.getElementById("resultScreen").style.display = "none";
    document.getElementById("gameScreen").style.display = "block";

    document.getElementById("difficultyLabel").textContent =
        difficulty.toUpperCase();

    updateHUD();
    nextRound();
}

/* LOAD QUESTION */

function nextRound() {
    if (!gameActive) return;

    if (
        round >= currentQuestions.length ||
        lives <= 0
    ) {
        endGame();
        return;
    }

    round++;
    questionLocked = false;
    currentQuestion = currentQuestions[round - 1];

    document.getElementById("roundInfo").textContent =
        "ROUND " + round + " / " + currentQuestions.length;

    document.getElementById("progress").style.width =
        ((round - 1) / currentQuestions.length * 100) + "%";

    document.getElementById("question").innerHTML =
        currentQuestion.sequence.join(
            '<span style="color:#475569"> → </span>'
        ) +
        '<span class="missing"> → ?</span>';

    document.getElementById("hint").textContent =
        "Which number completes the pattern?";

    document.getElementById("feedback").textContent = "";
    document.getElementById("feedback").className = "feedback";

    document.getElementById("nextBtn").style.display = "none";

    const optionsContainer = document.getElementById("options");
    optionsContainer.innerHTML = "";

    const choices = shuffle(currentQuestion.choices);

    choices.forEach(choice => {
        const button = document.createElement("button");

        button.className = "option-btn";
        button.textContent = choice;
        button.type = "button";

        button.addEventListener("click", () => {
            selectAnswer(choice, button);
        });

        optionsContainer.appendChild(button);
    });

    updateHUD();
}

/* ANSWER */

function selectAnswer(choice, selectedButton) {
    if (!gameActive || questionLocked) return;

    questionLocked = true;
    answeredCount++;

    const buttons = document.querySelectorAll(".option-btn");

    buttons.forEach(button => {
        button.disabled = true;

        if (button.textContent === currentQuestion.answer) {
            button.classList.add("correct");
        }
    });

    const feedback = document.getElementById("feedback");

    if (choice === currentQuestion.answer) {
        correct++;
        combo++;
        bestCombo = Math.max(bestCombo, combo);

        const points = Math.round(
            (settings[difficulty].points + (combo - 1) * 25)
            * settings[difficulty].multiplier
        );

        score += points;

        feedback.textContent =
            "✓ Correct! +" + points + " points. " +
            currentQuestion.explanation;

        feedback.className = "feedback good";

    } else {
        wrong++;
        lives--;
        combo = 0;

        selectedButton.classList.add("wrong");

        feedback.textContent =
            "✕ Not quite. " + currentQuestion.explanation;

        feedback.className = "feedback bad";
    }

    document.getElementById("progress").style.width =
        (round / currentQuestions.length * 100) + "%";

    updateHUD();

    document.getElementById("nextBtn").style.display = "block";

    document.getElementById("nextBtn").textContent =
        (round >= currentQuestions.length || lives <= 0)
        ? "VIEW RESULTS →"
        : "NEXT QUESTION →";
}

/* HUD */

function updateHUD() {
    document.getElementById("score").textContent =
        score.toLocaleString();

    document.getElementById("lives").textContent =
        "❤️".repeat(Math.max(0, lives)) +
        "🖤".repeat(Math.max(0, 3 - lives));

    document.getElementById("combo").textContent =
        combo + "x";
}

/* RESULTS */

function endGame() {
    gameActive = false;
    questionLocked = true;

    document.getElementById("gameScreen").style.display = "none";
    document.getElementById("resultScreen").style.display = "block";

    document.getElementById("finalScore").textContent =
        score.toLocaleString();

    const accuracy = answeredCount > 0
        ? Math.round(correct / answeredCount * 100)
        : 0;

    const completion = Math.round(
        answeredCount / currentQuestions.length * 100
    );

    document.getElementById("correctCount").textContent = correct;
    document.getElementById("wrongCount").textContent = wrong;
    document.getElementById("accuracy").textContent = accuracy + "%";
    document.getElementById("bestCombo").textContent = bestCombo + "x";
    document.getElementById("questionsDone").textContent = answeredCount;
    document.getElementById("completion").textContent = completion + "%";

    let title;
    let rank;
    let icon;

    if (accuracy >= 90) {
        title = "Pattern Genius!";
        rank = "🧠 SEQUENCE MASTER";
        icon = "🏆";
    } else if (accuracy >= 75) {
        title = "Excellent Thinking!";
        rank = "⚡ LOGIC EXPERT";
        icon = "⚡";
    } else if (accuracy >= 50) {
        title = "Great Progress!";
        rank = "🎯 PATTERN SOLVER";
        icon = "🎯";
    } else {
        title = "Keep Practicing!";
        rank = "💪 PATTERN BEGINNER";
        icon = "🧩";
    }

    document.getElementById("resultTitle").textContent = title;
    document.getElementById("rank").textContent = rank;
    document.getElementById("resultIcon").textContent = icon;

    document.getElementById("progress").style.width =
        completion + "%";
}

/* KEYBOARD SUPPORT */

document.addEventListener("keydown", event => {
    if (
        event.key === "Enter" &&
        document.getElementById("startScreen").style.display !== "none"
    ) {
        startGame();
    } else if (
        event.key === "Enter" &&
        gameActive &&
        questionLocked
    ) {
        nextRound();
    }
});
</script>
</body>
</html>
"""

components.html(
    GAME_HTML,
    height=1100,
    scrolling=True
)
