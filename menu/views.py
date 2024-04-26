from flask import Blueprint

menu = Blueprint(
    "menu",
    __name__,
    template_folder="templates",
    static_folder="static",
)

@menu.route("/")
def index():

    # render_template : 내가 만든 HTML 문서를 화면에 표시할 수 있다 
    return "여기에다 뭘 제공할건지 써야한다"


# @menu.route("/sandwitch")
# def sandwitch():
#     return "샌드위치"
