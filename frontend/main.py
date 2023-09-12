from st_pages import Page, add_page_title, show_pages
import os


env = os.environ.get('ENVIRONMENT', 'Not Set')
if env == "Not Set":
    print(os.environ)
    print("Setting env variables")
    os.environ["ENVIRONMENT"] = 'local'  # 'dev' 'test' 'prod'

relative_path = "src/application/"
relative_pages_path = "src/application/pages/"

show_pages(
    [
        Page(relative_path + "home.py", "Home", "🏠"),
        Page(relative_pages_path + "page0_list.py", "Project List",
             ":books:"),
        Page(relative_pages_path + "page1_project1.py", "Demo Project", "👾"),
        Page(relative_pages_path + "page2_CoverLetterGenerator.py",
             "LLM - Cover Letter Generation", "📝"),
    ]
)
