import os


def set_page_config(st):
    st.set_page_config(
        page_title="Aditya Vyas Pet Projects",
        page_icon="https://cdn.myportfolio.com/96740d58-7273-4585-ab3a-195b3a5456f4/4952e841-36a4-48f2-809c-2e27c8d85fab_carw_1x1x32.png?h=546faff1ec83eb12955dc4d58e3b0e5f",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            'Get Help': 'https://adityavyas.co.in/contact',
            'Report a bug': "https://adityavyas.co.in/contact",
            'About': "[Click here to know more about me](https://adityavyas.co.in/about-me)"
        }
    )

    if "shared" not in st.session_state:
        st.session_state["shared"] = True


def set_env_vars():
    env = os.environ.get('ENVIRONMENT', 'Not Set')
    if env == "Not Set":
        print("Setting env variables")
        os.environ["ENVIRONMENT"] = 'local'  # 'dev' 'test' 'prod'

    env = os.environ.get('ENVIRONMENT', 'Not Set')
    if env == "Not Set":
        raise "Enviornment not set"
    elif env == 'local':
        os.environ["base_path"] = "http://localhost:8501"
        os.environ["backend"] = "http://localhost:8000/api/"
    else:
        os.environ["base_path"] = "http://work.adityavyas.co.in"
        os.environ["backend"] = "http://fastapi:8000/api/"
