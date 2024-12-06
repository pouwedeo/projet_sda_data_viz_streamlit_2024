import  streamlit as st

def custom_metric(
    label: str,
    value: str,
    delta: str = None,
    data_testid: str = "default-id",
    background_color: str = "#f9f9f9",
    border_radius_px: int = 5,
    text_color: str = "#333",
    delta_color: str = "#008000",
) -> None:

    st.markdown(
        f"""
        <div data-testid="{data_testid}" 
             style="
                 background-color: {background_color}; 
                 border-radius: {border_radius_px}px; 
                 padding: 15px; 
                 text-align: center; 
                 margin-bottom: 10px;
                 box-shadow: 5px 5px 5px 5px rgb(68 63 63 / 17%);
             ">
            <div style="color: {text_color}; font-size: 16px; font-weight: bold;">{label}</div>
            <div style="color: {text_color}; font-size: 24px; font-weight: bold;">{value}</div>
            {'<div style="color: '+delta_color+'; font-size: 14px;">'+delta+'</div>' if delta else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )

