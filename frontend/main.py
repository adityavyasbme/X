from st_pages import Page, add_page_title, show_pages

relative_path = "src/application/"
relative_pages_path = "src/application/pages/"

show_pages(
    [
        Page(relative_path + "home.py", "Home", "🏠"),
        Page(relative_pages_path + "page1_project1.py", "project", ":books:"),
    ]
)
