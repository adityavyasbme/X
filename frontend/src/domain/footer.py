def hide_footer(st):
    hide_menu = """
    <style>
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility:hidden;
    }
    </style>
    """
    st.markdown(hide_menu, unsafe_allow_html=True)
