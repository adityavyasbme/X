"""
This code is taken from https://github.com/streamlit/links
"""
import streamlit as st


def load_css():
    css = """
    .css-12oz5g7.egzxvld2 {
    padding-top: 0px;
    }

    .css-1v0mbdj.etr89bj1 {
        display: block;
        margin-left: auto;
        margin-right: auto;
        min-width: 180px;
        max-width: 40%;
    }

    .css-10trblm.e16nr0p30 {
        font-weight: bold;
        text-align: center;
    }
    """

    st.markdown('<style>{}</style>'.format(css),
                unsafe_allow_html=True)
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)


def st_button(icon, url, label, iconsize):
    if icon == 'youtube':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-youtube" viewBox="0 0 16 16">
                    <path d="M8.051 1.999h.089c.822.003 4.987.033 6.11.335a2.01 2.01 0 0 1 1.415 1.42c.101.38.172.883.22 1.402l.01.104.022.26.008.104c.065.914.073 1.77.074 1.957v.075c-.001.194-.01 1.108-.082 2.06l-.008.105-.009.104c-.05.572-.124 1.14-.235 1.558a2.007 2.007 0 0 1-1.415 1.42c-1.16.312-5.569.334-6.18.335h-.142c-.309 0-1.587-.006-2.927-.052l-.17-.006-.087-.004-.171-.007-.171-.007c-1.11-.049-2.167-.128-2.654-.26a2.007 2.007 0 0 1-1.415-1.419c-.111-.417-.185-.986-.235-1.558L.09 9.82l-.008-.104A31.4 31.4 0 0 1 0 7.68v-.123c.002-.215.01-.958.064-1.778l.007-.103.003-.052.008-.104.022-.26.01-.104c.048-.519.119-1.023.22-1.402a2.007 2.007 0 0 1 1.415-1.42c.487-.13 1.544-.21 2.654-.26l.17-.007.172-.006.086-.003.171-.007A99.788 99.788 0 0 1 7.858 2h.193zM6.4 5.209v4.818l4.157-2.408L6.4 5.209z"/>
                </svg>  
                {label}
            </a>
        </p>'''
    elif icon == 'twitter':
        button_code = f'''
        <p>
        <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
            <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-twitter" viewBox="0 0 16 16">
                <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
            </svg>
            {label}
        </a>
        </p>'''
    elif icon == 'linkedin':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-linkedin" viewBox="0 0 16 16">
                    <path d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'medium':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-medium" viewBox="0 0 16 16">
                    <path d="M9.025 8c0 2.485-2.02 4.5-4.513 4.5A4.506 4.506 0 0 1 0 8c0-2.486 2.02-4.5 4.512-4.5A4.506 4.506 0 0 1 9.025 8zm4.95 0c0 2.34-1.01 4.236-2.256 4.236-1.246 0-2.256-1.897-2.256-4.236 0-2.34 1.01-4.236 2.256-4.236 1.246 0 2.256 1.897 2.256 4.236zM16 8c0 2.096-.355 3.795-.794 3.795-.438 0-.793-1.7-.793-3.795 0-2.096.355-3.795.794-3.795.438 0 .793 1.699.793 3.795z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'newsletter':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-envelope" viewBox="0 0 16 16">
                    <path d="M0 4a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H2a2 2 0 0 1-2-2V4Zm2-1a1 1 0 0 0-1 1v.217l7 4.2 7-4.2V4a1 1 0 0 0-1-1H2Zm13 2.383-4.708 2.825L15 11.105V5.383Zm-.034 6.876-5.64-3.471L8 9.583l-1.326-.795-5.64 3.47A1 1 0 0 0 2 13h12a1 1 0 0 0 .966-.741ZM1 11.105l4.708-2.897L1 5.383v5.722Z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'cup':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor" class="bi bi-cup-fill" viewBox="0 0 16 16">
                    <path d="M1 2a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1v1h.5A1.5 1.5 0 0 1 16 4.5v7a1.5 1.5 0 0 1-1.5 1.5h-.55a2.5 2.5 0 0 1-2.45 2h-8A2.5 2.5 0 0 1 1 12.5V2zm13 10h.5a.5.5 0 0 0 .5-.5v-7a.5.5 0 0 0-.5-.5H14v8z"/>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'github':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize}>
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> 
                <path d="M18.6713 2.62664C18.5628 2.36483 18.3534 2.16452 18.0959 2.07627L18.094 2.07564L18.0922 2.07501L18.0884 2.07374L18.0805 2.07114L18.0636 2.06583C18.0518 2.06223 18.039 2.05856 18.0252 2.05487C17.9976 2.04749 17.966 2.04007 17.9305 2.03319C17.8593 2.01941 17.7728 2.00787 17.6708 2.00279C17.466 1.99259 17.2037 2.00858 16.8817 2.08054C16.3447 2.20053 15.6476 2.47464 14.7724 3.03631C14.7152 3.07302 14.6572 3.11096 14.5985 3.15016C14.5397 3.13561 14.4809 3.12155 14.422 3.108C12.8261 2.74083 11.1742 2.74083 9.57825 3.108C9.51933 3.12156 9.46049 3.13561 9.40173 3.15017C9.34298 3.11096 9.28499 3.07302 9.22775 3.03631C8.35163 2.47435 7.65291 2.20029 7.11455 2.08039C6.79179 2.00852 6.52891 1.99262 6.324 2.00278C6.22186 2.00784 6.13536 2.01931 6.06428 2.03299C6.0288 2.03982 5.99732 2.04717 5.96983 2.05447C5.95609 2.05812 5.94336 2.06176 5.93163 2.06531L5.91481 2.07056L5.90698 2.07311L5.9032 2.07437L5.90135 2.07499L5.89952 2.07561C5.63979 2.16397 5.42877 2.36623 5.32049 2.63061C4.91716 3.6154 4.8101 4.70134 5.00435 5.74306C5.01379 5.79367 5.02394 5.84418 5.0348 5.89458C4.99316 5.95373 4.9527 6.01368 4.91343 6.07439C4.30771 7.01089 3.98553 8.12791 4.00063 9.27493C4.00208 11.7315 4.71965 13.4139 5.9332 14.4965C6.62014 15.1093 7.41743 15.4844 8.21873 15.7208C8.31042 15.7479 8.40217 15.7731 8.49381 15.7967C8.48043 15.8432 8.46796 15.8901 8.45641 15.9373C8.40789 16.1357 8.37572 16.3394 8.36083 16.5461C8.35948 16.5648 8.35863 16.5835 8.35829 16.6022L8.32436 18.421L8.32417 18.4407C8.32417 18.4464 8.32417 18.4521 8.32417 18.4577C8.26262 18.473 8.20005 18.4843 8.13682 18.4916C7.942 18.5141 7.74467 18.4977 7.5561 18.4434C7.36752 18.3891 7.19127 18.2979 7.03752 18.1749C6.88377 18.0519 6.75553 17.8994 6.66031 17.7261L6.6505 17.7087C6.38836 17.2535 6.02627 16.8639 5.59142 16.5695C5.15656 16.275 4.6604 16.0836 4.14047 16.0099C3.59365 15.9324 3.08753 16.3128 3.01002 16.8597C2.93251 17.4065 3.31296 17.9126 3.85978 17.9901C4.07816 18.0211 4.28688 18.1015 4.47012 18.2256C4.65121 18.3482 4.80277 18.5103 4.9134 18.7C5.1346 19.0992 5.43165 19.4514 5.78801 19.7365C6.14753 20.0242 6.56032 20.2379 7.00272 20.3653C7.43348 20.4893 7.88392 20.5291 8.32949 20.4825C8.33039 20.7224 8.33103 20.9065 8.33103 21C8.33103 21.5523 8.75521 22 9.27847 22H14.7558C15.279 22 15.7032 21.5523 15.7032 21V17.2095C15.729 16.7802 15.685 16.3499 15.5738 15.9373C15.5585 15.8805 15.5419 15.824 15.5241 15.7679C15.5838 15.753 15.6435 15.7373 15.7032 15.7208C16.5277 15.4937 17.3513 15.1224 18.0588 14.4983C19.2791 13.4217 19.9982 11.7379 19.9996 9.27493C20.0147 8.12791 19.6925 7.01089 19.0868 6.07439C19.0475 6.01358 19.007 5.95354 18.9652 5.89429C18.976 5.84399 18.9861 5.79358 18.9955 5.74306C19.1893 4.69934 19.0795 3.61142 18.6713 2.62664Z" fill="currentColor"></path> </g>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'website':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg fill="currentColor" width={iconsize} height={iconsize} viewBox="0 0 100 100" version="1.1" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <g id="network"></g> <g id="connection"></g> <g id="page"></g> <g id="support"></g> <g id="configuration"></g> <g id="cloud_storage"></g> <g id="password"></g> <g id="search_engine"></g> <g id="history"></g> <g id="SEO"></g> <g id="optimization"></g> <g id="backlink"></g> <g id="performance"></g> <g id="analytics"></g> <g id="security"></g> <g id="dark_web"> <g> 
                <path d="M54.2,38.4c0.1,0.3,0.3,0.5,0.6,0.6c0.1,0,0.2,0,0.3,0c0.2,0,0.4,0,0.5-0.1l0.7-0.4C55.5,39.2,55,40,55,41 c0,2.2,2.6,4,6,4s6-1.8,6-4s-2.6-4-6-4c-1.2,0-2.3,0.2-3.2,0.6l9.7-5.8c0.4-0.2,0.6-0.7,0.4-1.2c-0.2-0.5-0.6-0.7-1.1-0.7l-14,2 c-0.3,0-0.6,0.2-0.7,0.5s-0.2,0.6,0,0.9L54.2,38.4z M65,41c0,0.9-1.7,2-4,2s-4-1.1-4-2s1.7-2,4-2S65,40.1,65,41z M62.2,32.7 l-6.5,3.9l-1.2-2.8L62.2,32.7z"></path> <path d="M32.5,31.9l9.7,5.8c-0.9-0.4-2-0.6-3.2-0.6c-3.4,0-6,1.8-6,4s2.6,4,6,4s6-1.8,6-4c0-1-0.5-1.8-1.3-2.5l0.7,0.4 c0.2,0.1,0.3,0.1,0.5,0.1c0.1,0,0.2,0,0.3,0c0.3-0.1,0.5-0.3,0.6-0.6l2.2-5c0.1-0.3,0.1-0.6,0-0.9s-0.4-0.5-0.7-0.5l-14-2 c-0.5-0.1-0.9,0.2-1.1,0.7C31.9,31.1,32.1,31.6,32.5,31.9z M39,43c-2.3,0-4-1.1-4-2s1.7-2,4-2s4,1.1,4,2S41.3,43,39,43z M45.6,33.8l-1.2,2.8l-6.5-3.9L45.6,33.8z"></path> <path d="M43.8,52.9C43.7,53,43.6,53,43.5,53h-3.6c-0.1,0-0.3-0.1-0.3-0.2l-3.1-4.7c-0.4-0.7-1.2-1.1-2-1.1c-0.8,0-1.6,0.4-2,1.1 c-0.5,0.7-0.5,1.6-0.2,2.3l3.6,8.1c0.4,0.9,1.3,1.4,2.2,1.4h4.1c0.3,0.7,1,1.6,2.6,2.2C46.2,62.7,48,63,50,63c3.2,0,7-0.8,7.8-3 h4.1c0.9,0,1.8-0.6,2.2-1.4l3.6-8.1c0.3-0.8,0.3-1.6-0.2-2.3c-0.4-0.7-1.2-1.1-2-1.1c-0.8,0-1.6,0.4-2,1.1l-3.1,4.7 c-0.1,0.1-0.2,0.2-0.3,0.2h-3.6c-0.1,0-0.2,0-0.3-0.1l-3.1-3.2C52.7,49.3,52,49,51.4,49h-2.8c-0.6,0-1.3,0.3-1.7,0.7L43.8,52.9z M50,61c-2.3,0-4.1-0.4-5.1-1h0.7c0.5,0,1-0.2,1.5-0.5l2.7-2.1c0.1-0.1,0.3-0.1,0.5,0l2.7,2.1c0.4,0.3,0.9,0.5,1.5,0.5h0.7 C54.1,60.6,52.3,61,50,61z M48.6,51h2.8c0.1,0,0.2,0,0.3,0.1l3.1,3.2c0.5,0.5,1.1,0.7,1.7,0.7h3.6c0.8,0,1.6-0.4,2-1.1l3.1-4.7 c0.1-0.1,0.2-0.2,0.3-0.2c0.2,0,0.3,0.1,0.3,0.2c0,0.1,0.1,0.2,0,0.4l-3.6,8.1c-0.1,0.2-0.2,0.3-0.4,0.3h-7.5 c-0.1,0-0.2,0-0.2-0.1l-2.7-2.1c-0.4-0.3-0.9-0.5-1.5-0.5s-1,0.2-1.5,0.5l-2.7,2.1C45.8,58,45.7,58,45.6,58h-7.5 c-0.2,0-0.3-0.1-0.4-0.3L34,49.6c-0.1-0.2,0-0.4,0-0.4c0-0.1,0.2-0.2,0.3-0.2c0.1,0,0.3,0.1,0.3,0.2l3.1,4.7 c0.4,0.7,1.2,1.1,2,1.1h3.6c0.6,0,1.3-0.3,1.7-0.7l3.1-3.2C48.4,51,48.5,51,48.6,51z"></path> <path d="M85.3,79.5C92,71.5,96,61.2,96,50c0-11.2-4-21.5-10.7-29.5c-0.1-0.1-0.1-0.2-0.2-0.3c0,0,0,0,0,0C76.6,10.3,64,4,50,4 c-14,0-26.6,6.3-35,16.2c0,0,0,0,0,0c-0.1,0.1-0.2,0.2-0.2,0.3C8,28.5,4,38.8,4,50c0,11.2,4,21.5,10.7,29.5 c0.1,0.1,0.1,0.2,0.2,0.3c0,0,0,0,0,0C23.4,89.7,36,96,50,96s26.6-6.3,35-16.2c0,0,0,0,0,0C85.2,79.7,85.2,79.6,85.3,79.5z M72.2,67.7c1.1-5.2,1.8-10.8,1.8-16.7h20c-0.2,10-3.8,19.2-9.6,26.4C80.9,73.5,76.7,70.2,72.2,67.7z M15.6,77.4 C9.8,70.2,6.2,61,6,51h20c0.1,5.9,0.7,11.5,1.8,16.7C23.3,70.2,19.1,73.5,15.6,77.4z M15.6,22.6c3,3.4,6.5,6.3,10.4,8.7v16.6 c0,0.3,0,0.6,0,0.8c0,0,0,0,0,0c0,0,0,0.1,0,0.2c0,0,0,0,0,0.1H6C6.2,39,9.8,29.9,15.6,22.6z M51,6.1c6.6,0.6,12.7,7.2,16.7,17.9 H51V6.1z M49,24H32.3C36.3,13.2,42.4,6.7,49,6.1V24z M72,26v21.9c0,11-6.5,20.8-16.6,25.1c-0.2,0.1-0.4,0.1-0.6,0.2L53,65.8 c-0.1-0.4-0.5-0.8-1-0.8h-2h-2c-0.5,0-0.9,0.3-1,0.8l-1.8,7.4c-0.2-0.1-0.4-0.1-0.6-0.2C34.5,68.7,28,58.9,28,47.9V26H72z M94,49 H74c0,0,0,0,0-0.1c0-0.1,0-0.2,0-0.2c0,0,0,0,0,0c0-0.3,0-0.5,0-0.8V31.2c3.9-2.4,7.3-5.3,10.4-8.7C90.2,29.9,93.8,39,94,49z M47.1,73.7l1.7-6.7H50h1.2l1.7,6.7C51,74.1,49,74.1,47.1,73.7z M28.6,59.8c0.9,2.1,2.1,4,3.5,5.8c-0.8,0.3-1.6,0.7-2.4,1.1 C29.2,64.5,28.8,62.2,28.6,59.8z M33.4,67.3c2.8,3.2,6.4,5.8,10.5,7.5c1.6,0.7,3.4,1.1,5.2,1.2v18c-8.3-0.8-15.5-10.8-18.9-25.2 C31.2,68.2,32.3,67.7,33.4,67.3z M51,75.9c1.8-0.1,3.5-0.5,5.2-1.2c4.1-1.7,7.7-4.3,10.5-7.5c1.1,0.5,2.2,1,3.3,1.5 C66.5,83.1,59.3,93.2,51,93.9V75.9z M68,65.7c1.4-1.8,2.5-3.8,3.5-5.8c-0.3,2.4-0.6,4.7-1.1,6.9C69.6,66.4,68.8,66,68,65.7z M83.1,21c-2.7,3-5.7,5.7-9.1,7.9V25c0-0.6-0.4-1-1-1h-3.2C67,16,62.9,10,58.3,6.8C68.1,8.7,76.7,13.8,83.1,21z M41.7,6.8 C37.1,10,33,16,30.2,24H27c-0.6,0-1,0.4-1,1v3.9c-3.4-2.2-6.4-4.8-9.1-7.9C23.3,13.8,31.9,8.7,41.7,6.8z M16.9,79 c3.3-3.7,7.1-6.8,11.4-9.3c2.7,10.8,7.5,19.3,13.5,23.5C32,91.4,23.3,86.2,16.9,79z M58.2,93.2c5.9-4.2,10.8-12.7,13.5-23.5 c4.3,2.4,8.1,5.6,11.4,9.3C76.7,86.2,68,91.4,58.2,93.2z"></path> </g> </g> <g id="video_player"></g> <g id="upload_download"></g> <g id="incognito_tab"></g> <g id="bookmark"></g> </g>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == 'api':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" width={iconsize} height={iconsize} fill="currentColor">
                <g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier">
                <path d="M21.3,19a2.42,2.42,0,0,1-2.5.56l-2.35,2.35a.34.34,0,0,1-.49,0l-1-1a.36.36,0,0,1,0-.49l2.36-2.35a2.39,2.39,0,0,1,3.39-2.91L19.12,16.8l1,1,1.62-1.62A2.39,2.39,0,0,1,21.3,19ZM22,8v5.76A4.47,4.47,0,0,0,19.5,13a4.57,4.57,0,0,0-1.29.19V9.29H16.66V14A4.5,4.5,0,0,0,15,17.5a4.07,4.07,0,0,0,0,.5H4a2,2,0,0,1-2-2V8A2,2,0,0,1,4,6H20A2,2,0,0,1,22,8ZM11,15,9.09,9.27H7L5.17,15h1.7l.29-1.07H9L9.29,15Zm4.77-3.89a1.67,1.67,0,0,0-.55-1.35,2.43,2.43,0,0,0-1.62-.47h-2V15h1.54V13.11h.44a2.75,2.75,0,0,0,1-.17,1.82,1.82,0,0,0,.67-.44,1.63,1.63,0,0,0,.36-.64A2.36,2.36,0,0,0,15.75,11.11Zm-7.3.62-.12-.44-.15-.58c0-.21-.08-.37-.11-.5a4.63,4.63,0,0,1-.1.48c0,.19-.08.38-.13.57s-.08.34-.12.47l-.24.93H8.69Zm5.59-1a.63.63,0,0,0-.5-.17h-.4v1.31h.31a.9.9,0,0,0,.37-.07.59.59,0,0,0,.27-.22.75.75,0,0,0,.11-.42A.57.57,0,0,0,14,10.71Z"></path><rect width="24" height="24" fill="none"></rect></g>
                </svg>
                {label}
            </a>
        </p>'''
    elif icon == '':
        button_code = f'''
        <p>
            <a href={url} class="btn btn-outline-primary btn-lg btn-block" type="button" aria-pressed="true">
                {label}
            </a>
        </p>'''
    return st.markdown(button_code, unsafe_allow_html=True)
