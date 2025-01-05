import  streamlit as st

def footer():
    st.markdown(
        """
        <style>
        footer {
            visibility: hidden;
        }
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #eeece8;
            text-align: center;
            padding: 10px;
            font-size: 12px;
        }
        </style>
        <div class="footer">
            © 2024 ShowProject | Créé par Pouwédéo TCHAZINON|Sorbonne Data Analytics
        </div>
        """,
        unsafe_allow_html=True
    )