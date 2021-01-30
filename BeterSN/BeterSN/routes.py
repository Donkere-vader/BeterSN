from flask import current_app as app
from flask import render_template, request, jsonify
from .models import db, Civilian, Bsn
from datetime import datetime as dt


###################
# SETUP
###################
@app.context_processor
def inject_stage_and_region():
    return dict(
        enumerate=enumerate,
        len=len
    )

###################
# ROUTES
###################
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/bsn/generate", methods=["POST", "GET"])
def generate_bsn():
    if request.method == "POST":
        civ_id = request.form['id']
        usecase = request.form['usecase']
        expiry_date = dt.strptime(request.form['expiry_date'], "%Y-%m-%d")

        civ = Civilian.query.get(int(civ_id))
        key = civ.generate_key(usecase, expiry_date)

        return jsonify(
            key=key.bsn
        )

    return render_template("generate.html")

@app.route("/bsn/validate", methods=["GET", "POST"])
def verify_bsn():
    if request.method == "POST":
        bsn = request.form['bsn']
        bsn = Bsn.query.filter_by(bsn=bsn.encode()).first()

        valid = bsn.owner.verify_bsn(bsn.bsn)

        if valid:
            return valid

        return jsonify(error="Invalid!")
    return render_template("validate.html")

@app.route("/new_civilian", methods=["POST", "GET"])
def new_civilian():
    if request.method == "POST":
        name = request.form['name']
        birthday = dt.strptime(request.form['birthday'], "%Y-%m-%d")

        new_civ = Civilian(name, birthday)
        db.session.add(new_civ)
        db.session.commit()

        return jsonify(
            id=new_civ.id,
            name=new_civ.name,
            birthday=new_civ.birthday
        )

    return render_template("new_user.html")

@app.route("/database")
def database():
    return render_template("database.html", civilians=Civilian.query.all())
