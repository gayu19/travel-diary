from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import json

load_dotenv(verbose=True)

from service import DiaryService


app = Flask(__name__)

@app.route("/", methods=["GET"])
def list_places():
    all_places = DiaryService().get_all()    
    return render_template("home.html", all_places=list(all_places))
    #return DiaryService().get_all()


@app.route("/place", methods=["GET","POST"])
def create_place():
    placedict={}
    placelist=[]
    if request.method == "POST":
        placedict["name"] = request.form.get("name")
        placedict["location"] = request.form.get("location")
        placedict["type"] = request.form.get("type1")
        placedict["expenditure"] = request.form.get("expenditure")
        placedict["description"] = request.form.get("description")
        placelist.append(placedict)
        DiaryService().create(placelist)
        return render_template("thank_you.html", place=placedict.get("name"))
    return render_template("add_place.html")
    
    

@app.route("/place/<search_value>", methods=["GET"])
def get_place(search_value):    
    all_places = DiaryService().get(search_attribute="name",search_value=search_value)
    return render_template("show_place.html", all_places=list(all_places))

@app.route("/thankyou", methods=["GET"])
def thank_you():
    #return jsonify(DiaryService().create(request.get_json()))
    return render_template("thank_you.html")

if __name__ == "__main__":
    app.run(debug=True)