from src.infrastructure.socialLinks import st_button, load_css
from PIL import Image


def create_social_links(st, image_location="assets/Adi-1.jpg"):
    load_css()

    col1, col2 = st.columns(2)
    col1.image(Image.open(image_location))

    with col2:
        st.header('Aditya Vyas, M.B.A., M.S., B.E.')

        st.info('Machine Learning Engineer with high ' +
                'interest in data science and building large scale systems')
        icon_size = 20
        st_button('website',
                  'https://adityavyas.co.in',
                  'Portfolio', icon_size)
        st_button('api',
                  'https://work.adityavyas.co.in/docs',
                  'Backend API docs', icon_size)
        st_button('github',
                  'https://github.com/adityavyasbme/X',
                  'Check code for this website', icon_size)
        st_button('medium', 'https://medium.com/@CrazyStupidTraveller',
                  'Read my Blogs', icon_size)
        # st_button('twitter', 'https://twitter.com/adityavyasbme/',
        #           'Follow me on Twitter', icon_size)
        st_button('linkedin', 'https://www.linkedin.com/in/adityavyasbme/',
                  'Follow me on LinkedIn', icon_size)
        st_button('newsletter', 'https://medium.com/@CrazyStupidTraveller/subscribe',
                  'Sign up for my Newsletter', icon_size)
        st_button('youtube', 'https://www.youtube.com/@CrazyStupidTraveller/videos',
                  'My Travel channel', icon_size)
        st_button('cup', 'https://www.buymeacoffee.com/crazystupidtraveller',
                  'Buy me a Coffee', icon_size)
