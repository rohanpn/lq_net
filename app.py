
import db

from datetime import datetime
from flask import Flask, request, render_template, jsonify
from sqlalchemy import func

from db import BookDetails, UserRequest

app = db.app

@app.route('/')
def home_page():
    try:
        # import ipdb;ipdb.set_trace()
        return "Page Loaded Successfully", 200
    except Exception as ex:
        return "Home Page Error!!!!", 400


@app.route('/request/',  methods=["GET", "POST", "DELETE"])
def get_book_info():
    try:
        error = None
        


        if request.method == "POST":
            book_title = request.values['title']
            email = request.values['email']

            book_data = BookDetails.query.filter(func.lower(BookDetails.title) == func.lower(book_title)).all()
            if len(book_data) > 0:
                if len(UserRequest.query.filter(func.lower(UserRequest.email) == func.lower(email),
                                                func.lower(UserRequest.book_title) == func.lower(book_title)).all()) == 0:

                    user_request = UserRequest(book_id=book_data[0].id,
                                               book_title=book_title,
                                               email=email,
                                               timestamp=datetime.now())
                    db.db.session.add(user_request)
                    db.db.session.commit()
                    print(UserRequest.email)
                book_details = UserRequest.query.filter(UserRequest.book_id == book_data[0].id,
                                                        func.lower(UserRequest.email) == func.lower(email)).all()
                return jsonify(book_data=[i.serialize for i in book_details])
            else:
                return jsonify(error="Sorry, No Book with such title available!!!")
    
        elif request.method == "GET":
            id = request.args.get('id') or None
            if not id:
                book_details = UserRequest.query.all()
            else:
                id = request.values['id']
                book_details = UserRequest.query.filter_by(id=id).all()
                if len(book_details) == 0:
                    error = "No such ID exist in the database!!!!!"
                    return jsonify(error)
            return jsonify(book_data=[i.serialize for i in book_details])

        elif request.method == "DELETE":
            id = request.values['id'] or None
            if id:
                user_request = UserRequest.query.get(id)
                if user_request:
                    db.db.session.delete(user_request)
                    db.db.session.commit()
                    # return render_template("home.html", book_data=book_details, error=error)
                    error = "User request with id : %s deleted successfully" % (id)
                else:
                    error = "User request with id : %s does not exist" % (id)
            # book_details = UserRequest.query.all()
            return jsonify(error)

    except Exception as ex:
        return "Request Page Error!!!!", 400




if __name__ =="__main__":
    app.run(host='0.0.0.0', debug=True, port=8081)