import streamlit as st
import streamlit.components.v1 as components

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(
    page_title="SkillVerse | Reaction Rush",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)
# ============================================================
# PURE GAME
# ============================================================

GAME_HTML = r"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Number Ninja</title>


    <style>

    /* =========================================================
       GLOBAL RESET
    ========================================================= */

    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    html,
    body,
    .stApp {
        width: 100% !important;
        min-width: 100% !important;
        min-height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        overflow-x: hidden !important;
    }

    body {
        font-family:
            Inter,
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            sans-serif;

        background:
            radial-gradient(
                circle at 50% 0%,
                #18264a 0%,
                #0b1020 38%,
                #050812 100%
            );

        color: white;
    }


    /* =========================================================
       STREAMLIT FULL SCREEN
    ========================================================= */

    .block-container {
        width: 100% !important;
        max-width: none !important;
        min-height: 100vh !important;

        margin: 0 !important;
        padding: 0 !important;
    }

    [data-testid="stAppViewContainer"] {
        width: 100% !important;
        min-height: 100vh !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    [data-testid="stMainBlockContainer"] {
        width: 100% !important;
        max-width: none !important;
        min-height: 100vh !important;

        padding: 0 !important;
        margin: 0 !important;
    }

    /* Hide Streamlit default UI */

    header {
        display: none !important;
    }

    footer {
        display: none !important;
    }

    #MainMenu {
        display: none !important;
    }

    [data-testid="stToolbar"] {
        display: none !important;
    }

    [data-testid="stDecoration"] {
        display: none !important;
    }


    /* =========================================================
       GAME CONTAINER
    ========================================================= */

    .game {
        width: 100vw !important;
        min-width: 100vw !important;

        height: 100vh !important;
        min-height: 100vh !important;

        max-width: none !important;

        position: relative;

        overflow: hidden;

        margin: 0 !important;
        padding: 0 !important;

        background:
            radial-gradient(
                circle at 50% 45%,
                rgba(68, 89, 180, 0.15),
                transparent 35%
            ),
            linear-gradient(
                145deg,
                #050812,
                #0a1020 50%,
                #070b16
            );
    }


    /* =========================================================
       BACKGROUND GRID
    ========================================================= */

    .grid {
        position: absolute;

        inset: 0;

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

        pointer-events: none;
    }


    /* =========================================================
       BACKGROUND GLOW
    ========================================================= */

    .glow {
        position: absolute;

        width: 500px;
        height: 500px;

        border-radius: 50%;

        background:
            rgba(76, 201, 240, 0.08);

        filter: blur(90px);

        top: 180px;
        left: 50%;

        transform: translateX(-50%);

        pointer-events: none;
    }

    .glow-two {
        position: absolute;

        width: 350px;
        height: 350px;

        border-radius: 50%;

        background:
            rgba(124, 58, 237, 0.08);

        filter: blur(80px);

        bottom: -100px;
        right: -50px;

        pointer-events: none;
    }


    /* =========================================================
       START SCREEN
    ========================================================= */

    .screen {
        position: relative;

        z-index: 5;

        width: 100%;
        min-height: 100vh;

        display: flex;

        align-items: center;
        justify-content: center;

        padding: 40px;
    }


    /* =========================================================
       START BOX
    ========================================================= */

    .start-box {
        width: min(720px, 95%);

        text-align: center;

        padding: 55px 50px;

        border-radius: 30px;

        background:
            linear-gradient(
                145deg,
                rgba(18, 28, 52, 0.96),
                rgba(8, 13, 27, 0.96)
            );

        border:
            1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 35px 100px rgba(0,0,0,0.5),
            inset 0 1px 0 rgba(255,255,255,0.05);

        backdrop-filter: blur(20px);
    }


    /* =========================================================
       LOGO
    ========================================================= */

    .logo {
        font-size: 82px;

        filter:
            drop-shadow(
                0 0 25px
                rgba(80,200,255,0.4)
            );

        margin-bottom: 5px;
    }


    /* =========================================================
       GAME TITLE
    ========================================================= */

    .game-title {
        font-size:
            clamp(42px, 7vw, 70px);

        font-weight: 900;

        letter-spacing: -3px;

        background:
            linear-gradient(
                90deg,
                #ffffff,
                #8be9ff,
                #c084fc
            );

        -webkit-background-clip: text;
        background-clip: text;

        color: transparent;
    }


    /* =========================================================
       SUBTITLE
    ========================================================= */

    .subtitle {
        color: #9ca9c7;

        font-size: 17px;

        margin-top: 10px;

        margin-bottom: 35px;
    }


    /* =========================================================
       MISSION
    ========================================================= */

    .mission {
        display: inline-flex;

        padding: 8px 15px;

        border-radius: 999px;

        background:
            rgba(76,201,240,0.08);

        border:
            1px solid rgba(76,201,240,0.18);

        color: #7ddcff;

        font-size: 12px;

        font-weight: 800;

        letter-spacing: 1.5px;

        margin-bottom: 20px;
    }


    /* =========================================================
       DIFFICULTY
    ========================================================= */

    .difficulty-title {
        color: #b5c0d8;

        font-size: 13px;

        font-weight: 800;

        text-transform: uppercase;

        letter-spacing: 1.5px;

        margin-bottom: 13px;
    }

    .difficulty {
        display: flex;

        justify-content: center;

        gap: 12px;

        margin-bottom: 28px;
    }

    .diff-btn {
        border:
            1px solid rgba(255,255,255,0.10);

        background:
            rgba(255,255,255,0.04);

        color: #aeb9d0;

        padding: 13px 25px;

        border-radius: 13px;

        cursor: pointer;

        font-weight: 800;

        transition:
            all 0.2s ease;
    }

    .diff-btn:hover {
        transform:
            translateY(-2px);

        background:
            rgba(255,255,255,0.08);

        color: white;
    }

    .diff-btn.selected {
        color: white;

        border-color: #53d7ff;

        background:
            rgba(83,215,255,0.12);

        box-shadow:
            0 0 25px
            rgba(83,215,255,0.12);
    }


    /* =========================================================
       START BUTTON
    ========================================================= */

    .start-btn {
        width: 100%;

        border: none;

        padding: 18px 25px;

        border-radius: 15px;

        cursor: pointer;

        color: #06101b;

        background:
            linear-gradient(
                90deg,
                #61dafb,
                #a78bfa
            );

        font-size: 17px;

        font-weight: 950;

        letter-spacing: 1px;

        box-shadow:
            0 15px 35px
            rgba(76,201,240,0.20);

        transition:
            all 0.2s ease;
    }

    .start-btn:hover {
        transform:
            translateY(-3px);

        box-shadow:
            0 20px 45px
            rgba(76,201,240,0.30);
    }

    .start-btn:active {
        transform:
            translateY(0);
    }


    /* =========================================================
       CONTROLS
    ========================================================= */

    .controls {
        margin-top: 22px;

        color: #66728c;

        font-size: 12px;
    }

    .key {
        display: inline-block;

        padding: 3px 7px;

        margin: 0 3px;

        border-radius: 5px;

        border:
            1px solid rgba(255,255,255,0.12);

        background:
            rgba(255,255,255,0.05);

        color: #aebbd5;

        font-weight: 800;
    }


    /* =========================================================
       GAME SCREEN
    ========================================================= */

    #playScreen {
        display: none;

        position: relative;

        width: 100%;

        min-height: 100vh;

        padding: 25px 35px;

        z-index: 5;
    }


    /* =========================================================
       TOP BAR
    ========================================================= */

    .topbar {
        width: 100%;

        display: grid;

        grid-template-columns:
            1fr
            auto
            1fr;

        align-items: center;

        gap: 20px;

        margin-bottom: 25px;
    }

    .brand {
        display: flex;

        align-items: center;

        gap: 10px;

        font-weight: 900;

        font-size: 18px;
    }

    .brand-icon {
        font-size: 28px;
    }

    .difficulty-badge {
        display: inline-flex;

        align-items: center;

        justify-content: center;

        padding: 8px 14px;

        border-radius: 999px;

        background:
            rgba(255,255,255,0.05);

        border:
            1px solid rgba(255,255,255,0.08);

        color: #9aa7c0;

        font-size: 11px;

        font-weight: 900;

        text-transform: uppercase;

        letter-spacing: 1px;
    }


    /* =========================================================
       HUD
    ========================================================= */

    .hud {
        display: flex;

        justify-content: flex-end;

        gap: 10px;
    }

    .hud-item {
        min-width: 92px;

        padding: 10px 13px;

        border-radius: 13px;

        background:
            rgba(255,255,255,0.045);

        border:
            1px solid rgba(255,255,255,0.08);

        text-align: center;
    }

    .hud-label {
        color: #6f7b93;

        font-size: 9px;

        font-weight: 900;

        text-transform: uppercase;

        letter-spacing: 1px;
    }

    .hud-value {
        color: white;

        font-size: 17px;

        font-weight: 950;

        margin-top: 2px;
    }


    /* =========================================================
       PROGRESS
    ========================================================= */

    .progress-wrap {
        width: 100%;

        height: 5px;

        background:
            rgba(255,255,255,0.07);

        border-radius: 999px;

        overflow: hidden;

        margin-bottom: 35px;
    }

    .progress {
        height: 100%;

        width: 0%;

        background:
            linear-gradient(
                90deg,
                #61dafb,
                #a78bfa
            );

        border-radius: inherit;

        transition:
            width 0.3s ease;

        box-shadow:
            0 0 15px
            rgba(97,218,251,0.4);
    }


    /* =========================================================
       ARENA
    ========================================================= */

    .arena {
        width: min(950px, 100%);

        min-height: 600px;

        margin: 0 auto;

        display: flex;

        flex-direction: column;

        align-items: center;

        justify-content: center;

        position: relative;
    }


    /* =========================================================
       ROUND
    ========================================================= */

    .round-text {
        color: #71809d;

        font-size: 12px;

        font-weight: 900;

        letter-spacing: 2px;

        text-transform: uppercase;

        margin-bottom: 25px;
    }


    /* =========================================================
       TIMER
    ========================================================= */

    .timer-ring {
        width: 95px;

        height: 95px;

        border-radius: 50%;

        display: flex;

        align-items: center;

        justify-content: center;

        position: relative;

        margin-bottom: 22px;

        background:
            conic-gradient(
                #61dafb var(--timer),
                rgba(255,255,255,0.06) 0
            );
    }

    .timer-ring::before {
        content: "";

        position: absolute;

        inset: 7px;

        border-radius: 50%;

        background: #0a1020;
    }

    .timer-number {
        position: relative;

        z-index: 2;

        font-size: 27px;

        font-weight: 950;
    }

    .timer-danger {
        background:
            conic-gradient(
                #ff5c7a var(--timer),
                rgba(255,255,255,0.06) 0
            );

        animation:
            dangerPulse
            0.5s
            infinite
            alternate;
    }

    @keyframes dangerPulse {

        from {
            transform: scale(1);
        }

        to {
            transform: scale(1.05);
        }

    }


    /* =========================================================
       QUESTION CARD
    ========================================================= */

    .question-card {
        position: relative;

        width: min(720px, 95%);

        padding: 45px 35px;

        text-align: center;

        border-radius: 28px;

        background:
            linear-gradient(
                145deg,
                rgba(18,29,54,0.96),
                rgba(8,14,29,0.96)
            );

        border:
            1px solid rgba(255,255,255,0.10);

        box-shadow:
            0 30px 70px
            rgba(0,0,0,0.35),

            inset 0 1px 0
            rgba(255,255,255,0.04);

        transition:
            transform 0.15s ease;
    }

    .question-card.correct {
        animation:
            correctFlash
            0.4s
            ease;
    }

    .question-card.wrong {
        animation:
            wrongShake
            0.4s
            ease;
    }


    /* =========================================================
       CORRECT ANIMATION
    ========================================================= */

    @keyframes correctFlash {

        0% {
            transform: scale(1);

            box-shadow:
                0 0 0
                rgba(61,255,163,0);
        }

        50% {
            transform:
                scale(1.025);

            box-shadow:
                0 0 50px
                rgba(61,255,163,0.25);
        }

        100% {
            transform: scale(1);
        }

    }


    /* =========================================================
       WRONG ANIMATION
    ========================================================= */

    @keyframes wrongShake {

        0%, 100% {
            transform:
                translateX(0);
        }

        20% {
            transform:
                translateX(-12px);
        }

        40% {
            transform:
                translateX(12px);
        }

        60% {
            transform:
                translateX(-8px);
        }

        80% {
            transform:
                translateX(8px);
        }

    }


    /* =========================================================
       QUESTION TEXT
    ========================================================= */

    .question-label {
        color: #66728b;

        font-size: 11px;

        text-transform: uppercase;

        letter-spacing: 2px;

        font-weight: 900;

        margin-bottom: 15px;
    }

    .question {
        font-size:
            clamp(45px, 8vw, 76px);

        line-height: 1;

        font-weight: 950;

        letter-spacing: -3px;

        color: white;

        text-shadow:
            0 0 35px
            rgba(97,218,251,0.12);

        user-select: none;
    }


    /* =========================================================
       ANSWER AREA
    ========================================================= */

    .answer-area {
        margin-top: 28px;

        width: min(550px, 95%);

        position: relative;
    }

    .answer-input {
        width: 100%;

        height: 68px;

        border-radius: 17px;

        border:
            1px solid
            rgba(97,218,251,0.20);

        outline: none;

        background:
            rgba(5,10,22,0.92);

        color: white;

        text-align: center;

        font-size: 27px;

        font-weight: 900;

        padding:
            0 90px 0 20px;

        transition:
            all 0.2s ease;
    }

    .answer-input::placeholder {
        color: #48536a;

        font-size: 15px;

        font-weight: 600;
    }

    .answer-input:focus {
        border-color:
            rgba(97,218,251,0.75);

        box-shadow:
            0 0 0 4px
            rgba(97,218,251,0.07),

            0 0 35px
            rgba(97,218,251,0.12);
    }


    /* =========================================================
       ATTACK BUTTON
    ========================================================= */

    .attack-btn {
        position: absolute;

        right: 7px;

        top: 7px;

        height: 54px;

        width: 80px;

        border: none;

        border-radius: 12px;

        cursor: pointer;

        background:
            linear-gradient(
                135deg,
                #61dafb,
                #818cf8
            );

        color: #06101a;

        font-size: 20px;

        font-weight: 950;

        transition:
            0.2s;
    }

    .attack-btn:hover {
        transform:
            scale(1.04);
    }

    .attack-btn:active {
        transform:
            scale(0.96);
    }


    /* =========================================================
       ENTER HINT
    ========================================================= */

    .enter-hint {
        text-align: center;

        color: #56627b;

        font-size: 11px;

        margin-top: 11px;

        font-weight: 700;
    }


    /* =========================================================
       FEEDBACK
    ========================================================= */

    .feedback {
        min-height: 40px;

        margin-top: 20px;

        text-align: center;

        font-size: 17px;

        font-weight: 950;

        opacity: 0;

        transform:
            translateY(5px);

        transition:
            all 0.2s ease;
    }

    .feedback.show {
        opacity: 1;

        transform:
            translateY(0);
    }

    .feedback.correct {
        color: #5ff0a7;

        text-shadow:
            0 0 20px
            rgba(95,240,167,0.25);
    }

    .feedback.wrong {
        color: #ff6d88;

        text-shadow:
            0 0 20px
            rgba(255,109,136,0.2);
    }


    /* =========================================================
       COMBO
    ========================================================= */

    .combo {
        position: absolute;

        right: 0;

        top: 20px;

        color: #fbbf24;

        font-size: 13px;

        font-weight: 950;

        opacity: 0;

        transition:
            0.2s;
    }

    .combo.show {
        opacity: 1;

        animation:
            comboPop
            0.35s
            ease;
    }

    @keyframes comboPop {

        0% {
            transform:
                scale(0.7);
        }

        60% {
            transform:
                scale(1.2);
        }

        100% {
            transform:
                scale(1);
        }

    }


    /* =========================================================
       END SCREEN
    ========================================================= */

    #endScreen {
        display: none;

        position: relative;

        z-index: 10;

        width: 100%;

        min-height: 100vh;

        align-items: center;

        justify-content: center;

        padding: 40px;
    }


    /* =========================================================
       RESULT BOX
    ========================================================= */

    .result-box {
        width: min(700px, 95%);

        text-align: center;

        padding: 55px 45px;

        border-radius: 30px;

        background:
            linear-gradient(
                145deg,
                rgba(18,29,54,0.97),
                rgba(7,12,25,0.97)
            );

        border:
            1px solid
            rgba(255,255,255,0.10);

        box-shadow:
            0 35px 100px
            rgba(0,0,0,0.55);
    }


    /* =========================================================
       RESULT ICON
    ========================================================= */

    .result-icon {
        font-size: 72px;

        margin-bottom: 10px;
    }

    .result-title {
        font-size: 48px;

        font-weight: 950;

        letter-spacing: -2px;
    }

    .result-subtitle {
        color: #8794ad;

        margin-top: 10px;

        margin-bottom: 30px;
    }


    /* =========================================================
       FINAL SCORE
    ========================================================= */

    .final-score {
        font-size: 72px;

        font-weight: 950;

        background:
            linear-gradient(
                90deg,
                #61dafb,
                #c084fc
            );

        -webkit-background-clip: text;
        background-clip: text;

        color: transparent;
    }

    .score-label {
        color: #65718a;

        font-size: 11px;

        font-weight: 900;

        text-transform: uppercase;

        letter-spacing: 2px;
    }


    /* =========================================================
       RESULT STATS
    ========================================================= */

    .result-stats {
        display: grid;

        grid-template-columns:
            repeat(4, 1fr);

        gap: 10px;

        margin: 30px 0;
    }

    .result-stat {
        padding: 17px 10px;

        border-radius: 14px;

        background:
            rgba(255,255,255,0.04);

        border:
            1px solid
            rgba(255,255,255,0.07);
    }

    .result-stat-number {
        font-size: 22px;

        font-weight: 950;
    }

    .result-stat-label {
        margin-top: 4px;

        font-size: 9px;

        text-transform: uppercase;

        color: #66728a;

        font-weight: 800;
    }


    /* =========================================================
       RANK
    ========================================================= */

    .rank {
        margin-bottom: 25px;

        color: #aebbd3;

        font-size: 14px;

        font-weight: 800;
    }


    /* =========================================================
       PLAY AGAIN
    ========================================================= */

    .play-again {
        width: 100%;

        padding: 17px;

        border: none;

        border-radius: 15px;

        cursor: pointer;

        background:
            linear-gradient(
                90deg,
                #61dafb,
                #a78bfa
            );

        color: #06101b;

        font-size: 16px;

        font-weight: 950;

        transition:
            0.2s;
    }

    .play-again:hover {
        transform:
            translateY(-2px);

        box-shadow:
            0 15px 35px
            rgba(97,218,251,0.2);
    }


    /* =========================================================
       FLOATING SCORE
    ========================================================= */

    .floating-score {
        position: fixed;

        pointer-events: none;

        font-weight: 950;

        font-size: 20px;

        color: #61dafb;

        animation:
            floatScore
            0.9s
            ease
            forwards;

        z-index: 100;
    }

    @keyframes floatScore {

        0% {
            opacity: 1;

            transform:
                translateY(0)
                scale(1);
        }

        100% {
            opacity: 0;

            transform:
                translateY(-70px)
                scale(1.2);
        }

    }


    /* =========================================================
       MOBILE
    ========================================================= */

    @media (max-width: 800px) {

        .screen {
            padding: 20px;
        }

        .start-box {
            padding: 40px 25px;
        }

        #playScreen {
            padding: 18px;
        }

        .topbar {
            grid-template-columns: 1fr;

            text-align: center;

            gap: 12px;
        }

        .brand {
            justify-content: center;
        }

        .hud {
            justify-content: center;

            flex-wrap: wrap;
        }

        .hud-item {
            min-width: 72px;
        }

        .arena {
            min-height: 600px;
        }

        .question-card {
            padding: 35px 18px;
        }

        .question {
            letter-spacing: -2px;
        }

        .result-stats {
            grid-template-columns:
                repeat(2, 1fr);
        }

        .difficulty {
            flex-direction: column;
        }

        .diff-btn {
            width: 100%;
        }

    }


    /* =========================================================
       SMALL MOBILE
    ========================================================= */

    @media (max-width: 500px) {

        .screen {
            padding: 12px;
        }

        .start-box {
            width: 100%;
            padding: 30px 18px;
            border-radius: 22px;
        }

        .logo {
            font-size: 62px;
        }

        .game-title {
            font-size: 42px;
            letter-spacing: -2px;
        }

        .subtitle {
            font-size: 14px;
        }

        #playScreen {
            padding: 12px;
        }

        .hud {
            gap: 6px;
        }

        .hud-item {
            min-width: 65px;
            padding: 8px;
        }

        .question-card {
            width: 100%;
            padding: 28px 12px;
            border-radius: 22px;
        }

        .question {
            font-size: 42px;
        }

        .answer-input {
            height: 60px;
            font-size: 23px;
        }

        .attack-btn {
            height: 46px;
            width: 65px;
        }

        .result-box {
            width: 100%;
            padding: 35px 20px;
        }

        .result-title {
            font-size: 36px;
        }

        .final-score {
            font-size: 58px;
        }

    }


    /* =========================================================
       EXTRA STREAMLIT SPACING REMOVAL
    ========================================================= */

    div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }

    div[data-testid="stHorizontalBlock"] {
        gap: 0 !important;
    }

    </style>
  

</head>


<body>

<div class="game">

    <div class="grid"></div>
    <div class="glow"></div>
    <div class="glow-two"></div>


    <!-- =====================================================
         START SCREEN
    ====================================================== -->

    <section id="startScreen" class="screen">

        <div class="start-box">

            <div class="mission">
                ⚔️ NINJA TRAINING PROTOCOL
            </div>

            <div class="logo">
                🥷
            </div>

            <h1 class="game-title">
                NUMBER NINJA
            </h1>

            <p class="subtitle">
                Think fast. Strike faster.
                Master the numbers.
            </p>


            <div class="difficulty-title">
                Choose your difficulty
            </div>

            <div class="difficulty">

                <button
                    class="diff-btn selected"
                    data-difficulty="Easy"
                    onclick="selectDifficulty('Easy')"
                >
                    🟢 Easy
                </button>

                <button
                    class="diff-btn"
                    data-difficulty="Medium"
                    onclick="selectDifficulty('Medium')"
                >
                    🟡 Medium
                </button>

                <button
                    class="diff-btn"
                    data-difficulty="Hard"
                    onclick="selectDifficulty('Hard')"
                >
                    🔴 Hard
                </button>

            </div>


            <button
                class="start-btn"
                onclick="startGame()"
            >
                ⚔️ START MISSION
            </button>


            <div class="controls">
                Type your answer and press
                <span class="key">ENTER</span>
                to attack
            </div>

        </div>

    </section>


    <!-- =====================================================
         GAME SCREEN
    ====================================================== -->

    <section id="playScreen">

        <div class="topbar">

            <div class="brand">
                <span class="brand-icon">🥷</span>
                <span>NUMBER NINJA</span>
            </div>


            <div class="difficulty-badge">
                <span id="difficultyText">
                    EASY
                </span>
            </div>


            <div class="hud">

                <div class="hud-item">

                    <div class="hud-label">
                        Score
                    </div>

                    <div
                        class="hud-value"
                        id="score"
                    >
                        0
                    </div>

                </div>


                <div class="hud-item">

                    <div class="hud-label">
                        Lives
                    </div>

                    <div
                        class="hud-value"
                        id="lives"
                    >
                        ❤️❤️❤️
                    </div>

                </div>


                <div class="hud-item">

                    <div class="hud-label">
                        Combo
                    </div>

                    <div
                        class="hud-value"
                        id="combo"
                    >
                        x0
                    </div>

                </div>

            </div>

        </div>


        <div class="progress-wrap">

            <div
                id="progress"
                class="progress"
            ></div>

        </div>


        <div class="arena">

            <div
                id="roundText"
                class="round-text"
            >
                ROUND 1 / 10
            </div>


            <div
                id="timerRing"
                class="timer-ring"
                style="--timer:100%"
            >

                <div
                    id="timerNumber"
                    class="timer-number"
                >
                    15
                </div>

            </div>


            <div
                id="questionCard"
                class="question-card"
            >

                <div class="question-label">
                    Solve the target
                </div>

                <div
                    id="question"
                    class="question"
                >
                    8 + 7
                </div>


                <div class="answer-area">

                    <input
                        id="answerInput"
                        class="answer-input"
                        type="number"
                        inputmode="numeric"
                        autocomplete="off"
                        placeholder="TYPE ANSWER..."
                    >

                    <button
                        class="attack-btn"
                        onclick="submitAnswer()"
                        title="Attack"
                    >
                        ⚔️
                    </button>

                    <div class="enter-hint">
                        Press ENTER to attack
                    </div>

                </div>


                <div
                    id="feedback"
                    class="feedback"
                ></div>


                <div
                    id="comboMessage"
                    class="combo"
                >
                    🔥 COMBO!
                </div>

            </div>

        </div>

    </section>


    <!-- =====================================================
         RESULT SCREEN
    ====================================================== -->

    <section id="endScreen">

        <div class="result-box">

            <div
                id="resultIcon"
                class="result-icon"
            >
                🏆
            </div>

            <h1
                id="resultTitle"
                class="result-title"
            >
                MISSION COMPLETE
            </h1>

            <p
                id="resultSubtitle"
                class="result-subtitle"
            >
                The Number Ninja has mastered the arena.
            </p>


            <div class="score-label">
                Final Score
            </div>

            <div
                id="finalScore"
                class="final-score"
            >
                0
            </div>


            <div
                id="rank"
                class="rank"
            >
                ⚡ Ninja Rank
            </div>


            <div class="result-stats">

                <div class="result-stat">

                    <div
                        id="correctStat"
                        class="result-stat-number"
                    >
                        0
                    </div>

                    <div class="result-stat-label">
                        Correct
                    </div>

                </div>


                <div class="result-stat">

                    <div
                        id="wrongStat"
                        class="result-stat-number"
                    >
                        0
                    </div>

                    <div class="result-stat-label">
                        Wrong
                    </div>

                </div>


                <div class="result-stat">

                    <div
                        id="accuracyStat"
                        class="result-stat-number"
                    >
                        0%
                    </div>

                    <div class="result-stat-label">
                        Accuracy
                    </div>

                </div>


                <div class="result-stat">

                    <div
                        id="bestComboStat"
                        class="result-stat-number"
                    >
                        x0
                    </div>

                    <div class="result-stat-label">
                        Best Combo
                    </div>

                </div>

            </div>


            <button
                class="play-again"
                onclick="restartGame()"
            >
                🥷 PLAY AGAIN
            </button>

        </div>

    </section>

</div>


<script>

/* =========================================================
   GAME CONFIG
========================================================= */

const TOTAL_ROUNDS = 10;

const DIFFICULTIES = {

    Easy: {
        time: 15,
        max: 20,
        operations: ["+", "-"]
    },

    Medium: {
        time: 10,
        max: 100,
        operations: ["+", "-", "×"]
    },

    Hard: {
        time: 7,
        max: 500,
        operations: ["+", "-", "×"]
    }

};


/* =========================================================
   GAME STATE
========================================================= */

let difficulty = "Easy";

let round = 0;

let score = 0;

let lives = 3;

let combo = 0;

let bestCombo = 0;

let correct = 0;

let wrong = 0;

let timeouts = 0;

let currentAnswer = 0;

let timer = null;

let timeLeft = 0;

let locked = false;

let gameStarted = false;


/* =========================================================
   DOM
========================================================= */

const startScreen =
    document.getElementById("startScreen");

const playScreen =
    document.getElementById("playScreen");

const endScreen =
    document.getElementById("endScreen");

const answerInput =
    document.getElementById("answerInput");

const question =
    document.getElementById("question");

const scoreEl =
    document.getElementById("score");

const livesEl =
    document.getElementById("lives");

const comboEl =
    document.getElementById("combo");

const progressEl =
    document.getElementById("progress");

const roundText =
    document.getElementById("roundText");

const timerRing =
    document.getElementById("timerRing");

const timerNumber =
    document.getElementById("timerNumber");

const feedback =
    document.getElementById("feedback");

const questionCard =
    document.getElementById("questionCard");

const comboMessage =
    document.getElementById("comboMessage");


/* =========================================================
   DIFFICULTY
========================================================= */

function selectDifficulty(level) {

    difficulty = level;

    document
        .querySelectorAll(".diff-btn")
        .forEach(btn => {

            btn.classList.remove("selected");

        });


    const selected =
        document.querySelector(
            `[data-difficulty="${level}"]`
        );

    if (selected) {
        selected.classList.add("selected");
    }

}


/* =========================================================
   RANDOM NUMBER
========================================================= */

function randomNumber(min, max) {

    return Math.floor(
        Math.random() * (max - min + 1)
    ) + min;

}


/* =========================================================
   QUESTION GENERATOR
========================================================= */

function generateQuestion() {

    const config =
        DIFFICULTIES[difficulty];

    let a;
    let b;

    let operation;

    let answer;

    operation =
        config.operations[
            Math.floor(
                Math.random() *
                config.operations.length
            )
        ];


    /* -------------------------
       ADDITION
    ------------------------- */

    if (operation === "+") {

        a = randomNumber(1, config.max);

        b = randomNumber(1, config.max);

        answer = a + b;

    }


    /* -------------------------
       SUBTRACTION
    ------------------------- */

    else if (operation === "-") {

        a = randomNumber(1, config.max);

        b = randomNumber(1, config.max);

        if (b > a) {

            const temp = a;

            a = b;

            b = temp;

        }

        answer = a - b;

    }


    /* -------------------------
       MULTIPLICATION
    ------------------------- */

    else {

        if (difficulty === "Medium") {

            a = randomNumber(2, 20);

            b = randomNumber(2, 10);

        }

        else {

            a = randomNumber(5, 30);

            b = randomNumber(5, 20);

        }

        answer = a * b;

    }


    currentAnswer = answer;

    question.textContent =
        `${a} ${operation} ${b}`;

}


/* =========================================================
   START GAME
========================================================= */

function startGame() {

    round = 0;

    score = 0;

    lives = 3;

    combo = 0;

    bestCombo = 0;

    correct = 0;

    wrong = 0;

    timeouts = 0;

    locked = false;

    gameStarted = true;


    startScreen.style.display = "none";

    endScreen.style.display = "none";

    playScreen.style.display = "block";


    document.getElementById(
        "difficultyText"
    ).textContent =
        difficulty.toUpperCase();


    updateHUD();

    nextRound();

}


/* =========================================================
   NEXT ROUND
========================================================= */

function nextRound() {

    clearInterval(timer);

    locked = false;

    round++;


    if (round > TOTAL_ROUNDS) {

        finishGame(true);

        return;

    }


    updateProgress();

    roundText.textContent =
        `ROUND ${round} / ${TOTAL_ROUNDS}`;


    generateQuestion();


    const config =
        DIFFICULTIES[difficulty];


    timeLeft = config.time;


    timerNumber.textContent =
        timeLeft;


    timerRing.style.setProperty(
        "--timer",
        "100%"
    );


    timerRing.classList.remove(
        "timer-danger"
    );


    feedback.textContent = "";

    feedback.className = "feedback";


    questionCard.classList.remove(
        "correct",
        "wrong"
    );


    answerInput.value = "";

    answerInput.focus();


    startTimer();

}


/* =========================================================
   TIMER
========================================================= */

function startTimer() {

    const config =
        DIFFICULTIES[difficulty];

    const startTime =
        Date.now();


    timer = setInterval(() => {

        if (locked) {

            clearInterval(timer);

            return;

        }


        const elapsed =
            (Date.now() - startTime) / 1000;


        timeLeft =
            Math.max(
                0,
                config.time - elapsed
            );


        const percent =
            (timeLeft / config.time) * 100;


        timerRing.style.setProperty(
            "--timer",
            `${percent}%`
        );


        timerNumber.textContent =
            Math.ceil(timeLeft);


        if (timeLeft <= 3) {

            timerRing.classList.add(
                "timer-danger"
            );

        }


        if (timeLeft <= 0) {

            clearInterval(timer);

            handleTimeout();

        }

    }, 50);

}


/* =========================================================
   SUBMIT ANSWER
========================================================= */

function submitAnswer() {

    if (!gameStarted) {
        return;
    }

    if (locked) {
        return;
    }


    const value =
        answerInput.value.trim();


    if (value === "") {

        answerInput.focus();

        return;

    }


    locked = true;

    clearInterval(timer);


    const userAnswer =
        Number(value);


    if (userAnswer === currentAnswer) {

        handleCorrect();

    }

    else {

        handleWrong();

    }

}


/* =========================================================
   CORRECT
========================================================= */

function handleCorrect() {

    correct++;

    combo++;

    if (combo > bestCombo) {

        bestCombo = combo;

    }


    const config =
        DIFFICULTIES[difficulty];


    const baseScore = 100;


    const speedBonus =
        Math.max(
            0,
            Math.floor(
                timeLeft * 10
            )
        );


    const comboBonus =
        Math.max(
            0,
            (combo - 1) * 25
        );


    const earned =
        baseScore +
        speedBonus +
        comboBonus;


    score += earned;


    updateHUD();


    feedback.textContent =
        `⚡ PERFECT! +${earned} XP`;

    feedback.className =
        "feedback show correct";


    questionCard.classList.add(
        "correct"
    );


    comboMessage.textContent =
        combo >= 2
            ? `🔥 ${combo}x COMBO`
            : "";


    comboMessage.classList.add(
        "show"
    );


    createFloatingScore(
        `+${earned}`
    );


    setTimeout(() => {

        comboMessage.classList.remove(
            "show"
        );

    }, 700);


    setTimeout(() => {

        if (round < TOTAL_ROUNDS) {

            nextRound();

        }

        else {

            finishGame(true);

        }

    }, 650);

}


/* =========================================================
   WRONG
========================================================= */

function handleWrong() {

    wrong++;

    lives--;

    combo = 0;


    updateHUD();


    feedback.textContent =
        `❌ MISS! Answer: ${currentAnswer}`;

    feedback.className =
        "feedback show wrong";


    questionCard.classList.add(
        "wrong"
    );


    if (lives <= 0) {

        setTimeout(() => {

            finishGame(false);

        }, 750);

        return;

    }


    setTimeout(() => {

        nextRound();

    }, 800);

}


/* =========================================================
   TIMEOUT
========================================================= */

function handleTimeout() {

    if (locked) {
        return;
    }


    locked = true;

    timeouts++;

    wrong++;

    lives--;

    combo = 0;


    updateHUD();


    feedback.textContent =
        `⏱️ TIME'S UP! Answer: ${currentAnswer}`;

    feedback.className =
        "feedback show wrong";


    questionCard.classList.add(
        "wrong"
    );


    if (lives <= 0) {

        setTimeout(() => {

            finishGame(false);

        }, 800);

        return;

    }


    setTimeout(() => {

        nextRound();

    }, 850);

}


/* =========================================================
   HUD
========================================================= */

function updateHUD() {

    scoreEl.textContent =
        score;


    let hearts = "";

    for (
        let i = 0;
        i < 3;
        i++
    ) {

        hearts +=
            i < lives
                ? "❤️"
                : "🖤";

    }


    livesEl.textContent =
        hearts;


    comboEl.textContent =
        `x${combo}`;

}


/* =========================================================
   PROGRESS
========================================================= */

function updateProgress() {

    const percentage =
        ((round - 1) /
        TOTAL_ROUNDS) * 100;


    progressEl.style.width =
        `${percentage}%`;

}


/* =========================================================
   FLOATING SCORE
========================================================= */

function createFloatingScore(text) {

    const element =
        document.createElement("div");


    element.className =
        "floating-score";


    element.textContent =
        text;


    const rect =
        questionCard.getBoundingClientRect();


    element.style.left =
        `${rect.left + rect.width / 2}px`;


    element.style.top =
        `${rect.top + 100}px`;


    document.body.appendChild(
        element
    );


    setTimeout(() => {

        element.remove();

    }, 1000);

}


/* =========================================================
   FINISH GAME
========================================================= */

function finishGame(victory) {

    clearInterval(timer);

    gameStarted = false;

    playScreen.style.display =
        "none";

    endScreen.style.display =
        "flex";


    progressEl.style.width =
        "100%";


    const totalAnswered =
        correct + wrong;


    const accuracy =
        totalAnswered > 0
            ? Math.round(
                (correct /
                totalAnswered) * 100
              )
            : 0;


    document.getElementById(
        "finalScore"
    ).textContent =
        score;


    document.getElementById(
        "correctStat"
    ).textContent =
        correct;


    document.getElementById(
        "wrongStat"
    ).textContent =
        wrong;


    document.getElementById(
        "accuracyStat"
    ).textContent =
        `${accuracy}%`;


    document.getElementById(
        "bestComboStat"
    ).textContent =
        `x${bestCombo}`;


    const resultIcon =
        document.getElementById(
            "resultIcon"
        );


    const resultTitle =
        document.getElementById(
            "resultTitle"
        );


    const resultSubtitle =
        document.getElementById(
            "resultSubtitle"
        );


    const rank =
        document.getElementById(
            "rank"
        );


    if (victory) {

        resultIcon.textContent =
            "🏆";

        resultTitle.textContent =
            "MISSION COMPLETE";

        resultSubtitle.textContent =
            "You survived the Number Ninja arena.";

    }

    else {

        resultIcon.textContent =
            "💀";

        resultTitle.textContent =
            "GAME OVER";

        resultSubtitle.textContent =
            "The arena defeated you this time.";

    }


    let ninjaRank;


    if (accuracy >= 95 && score >= 1300) {

        ninjaRank =
            "👑 LEGENDARY NINJA";

    }

    else if (accuracy >= 85) {

        ninjaRank =
            "⚡ MASTER NINJA";

    }

    else if (accuracy >= 70) {

        ninjaRank =
            "🔥 ELITE NINJA";

    }

    else if (accuracy >= 50) {

        ninjaRank =
            "🥷 SHADOW NINJA";

    }

    else {

        ninjaRank =
            "🌱 ROOKIE NINJA";

    }


    rank.textContent =
        ninjaRank;

}


/* =========================================================
   RESTART
========================================================= */

function restartGame() {

    endScreen.style.display =
        "none";

    startScreen.style.display =
        "flex";

    gameStarted = false;

}


/* =========================================================
   ENTER KEY
========================================================= */

answerInput.addEventListener(
    "keydown",
    function(event) {

        if (
            event.key === "Enter"
        ) {

            event.preventDefault();

            submitAnswer();

        }

    }
);


/* =========================================================
   GLOBAL KEYBOARD SHORTCUT
========================================================= */

document.addEventListener(
    "keydown",
    function(event) {

        if (
            gameStarted &&
            event.key === "Enter" &&
            document.activeElement !== answerInput
        ) {

            answerInput.focus();

            submitAnswer();

        }

    }
);


/* =========================================================
   AUTO FOCUS
========================================================= */

window.addEventListener(
    "load",
    function() {

        setTimeout(() => {

            const firstButton =
                document.querySelector(
                    ".diff-btn"
                );

            if (firstButton) {
                firstButton.focus();
            }

        }, 200);

    }
);

</script>

</body>

</html>
"""


# ============================================================
# RENDER GAME
# ============================================================

components.html(
    GAME_HTML,
    height=900,
    scrolling=False
)