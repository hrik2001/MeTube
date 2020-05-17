from flask import Flask, request, render_template, redirect
import re
from urllib.parse import urlparse as o

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("main.html")

@app.route("/q" , methods=["GET" , "POST"])
def query():
    if request.method == "POST":
#        return request.form["link"]
        link = request.form["link"]
        if "youtube.com" in link:
            pattern = re.compile(r"watch?.*")
            try:
                return redirect(pattern.findall(link)[0])
            except:
                pattern=re.compile(r"playlist?.*")
                return redirect(pattern.findall(link)[0])
        elif "youtu.be" in link:
            link = o(link)
            return redirect("/watch?v="+link.path[1:len(link.path)] +"&" + link.query)
@app.route("/watch")
def watch():
    #return str(request.args)
    #return render_template("views.html")
    if "list" in request.args:
        mode = 1
    else:
        mode = 0
    if "t" in request.args:
        start=request.args["t"]
    else:
        start="0"
    if mode:
        return render_template("views.html" , mode=mode, args = {**{"timer":start},**request.args} , v=request.args["v"] , lis = request.args["list"])
    else:
        return render_template("views.html" , mode=mode, args = {**{"timer":start},**request.args} , v=request.args["v"], lis = "")


@app.route("/playlist")
def watch_playlist():
    return render_template("views_playlist.html" ,  args = {**request.args,**{"v":""}} , lis=request.args["list"])

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'),404

@app.errorhandler(500)
def not_foound_error(error):
    return render_template('500.html'),500

