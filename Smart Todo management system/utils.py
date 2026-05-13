import streamlit as st


def load_css():

    st.markdown(
        """
        <style>

        /* =========================
           Main App Background
        ========================== */

        .stApp {

            background: linear-gradient(
                135deg,
                #0f172a,
                #111827,
                #020617
            );

            color: white;
        }


        /* =========================
           Sidebar
        ========================== */

        section[data-testid="stSidebar"] {

            background: linear-gradient(
                180deg,
                rgba(15,23,42,0.95),
                rgba(2,6,23,0.95)
            );

            border-right: 1px solid rgba(255,255,255,0.08);
        }


        /* Sidebar Text */

        section[data-testid="stSidebar"] * {

            color: #f8fafc !important;
        }


        /* =========================
           Radio Buttons
        ========================== */

        div[role="radiogroup"] label {

            color: white !important;

            font-weight: 500;
        }


        /* =========================
           Labels
        ========================== */

        label {

            color: #f8fafc !important;

            font-weight: 500;
        }


        /* =========================
           Glassmorphism Task Cards
        ========================== */

        .task-card {

            background: rgba(255, 255, 255, 0.05);

            backdrop-filter: blur(12px);

            border-radius: 20px;

            padding: 22px;

            margin-bottom: 20px;

            border: 1px solid rgba(255,255,255,0.08);

            box-shadow:
                0 8px 32px rgba(0,0,0,0.35);

            transition: 0.3s ease;
        }


        /* Hover Animation */

        .task-card:hover {

            transform: translateY(-5px);

            box-shadow:
                0 0 20px rgba(0,255,255,0.18),
                0 0 40px rgba(0,255,255,0.10);
        }


        /* =========================
           Priority Borders
        ========================== */

        .high-border {

            border-left: 6px solid #ff4d6d;
        }

        .medium-border {

            border-left: 6px solid #ffd166;
        }

        .low-border {

            border-left: 6px solid #80ed99;
        }


        /* =========================
           Task Title
        ========================== */

        .title {

            font-size: 24px;

            font-weight: 700;

            margin-bottom: 10px;
        }


        .completed {

            color: #80ed99;

            text-decoration: line-through;
        }


        .pending {

            color: #f8fafc;
        }


        /* =========================
           Task Information
        ========================== */

        .task-info {

            color: #cbd5e1;

            font-size: 15px;

            margin-top: 8px;

            color: white;
        }


        /* =========================
           Priority Colors
        ========================== */

        .high {

            color: #ff4d6d;

            font-weight: bold;
        }


        .medium {

            color: #ffd166;

            font-weight: bold;
        }


        .low {

            color: #80ed99;

            font-weight: bold;
        }


        /* =========================
           Buttons
        ========================== */

        .stButton > button {

            width: 100%;

            border-radius: 12px;

            border: none;

            padding: 10px;

            font-weight: bold;

            background: linear-gradient(
                135deg,
                #06b6d4,
                #3b82f6
            );

            color: white;

            transition: 0.3s ease;
        }


        .stButton > button:hover {

            transform: scale(1.03);

            box-shadow:
                0 0 15px rgba(59,130,246,0.5);
        }


        /* =========================
           Inputs
        ========================== */

        .stSelectbox div[data-baseweb="select"] {

        background-color: white !important;

        color: black !important;

        border-radius: 12px;
    }


        /* =========================
    Dashboard Metrics
    ========================== */

    [data-testid="metric-container"] {

        background: rgba(255,255,255,0.05);

        border-radius: 18px;

        padding: 20px;

        border: 1px solid rgba(255,255,255,0.08);

        backdrop-filter: blur(12px);

        text-align: center;
    }


    /* Metric Labels */

    [data-testid="metric-container"] label {

        color: #cbd5e1 !important;

        font-size: 18px !important;

        font-weight: bold;
    }


    /* Metric Numbers */

    [data-testid="stMetricValue"] {

        color: white !important;

        font-size: 36px !important;

        font-weight: bold;
    }

         /* =========================
              Headers
        ========================== */

        h1, h2, h3 {

            color: #f8fafc;
        }


        /* =========================
           Smooth Animation
        ========================== */

        * {

            transition: all 0.2s ease;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
