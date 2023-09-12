import requests


def health_check(backend_url):
    r = requests.get(backend_url+'healthcheck')
    return r


def add_health_check_button(st, backend_url):
    if st.button("Backend Health Check"):
        res = health_check(backend_url).content
        if b'true' in res:
            data = "Healthcheck Success"
        else:
            data = "Healthcheck Failed"
        st.write(data)
