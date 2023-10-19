from flask import Flask,render_template
import requests

response= requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
app= Flask(__name__)

@app.route("/")
def guess():
    return render_template("index.html",data=response)
   # return render_template("index.html",data=response[0]["title"])
#@app.route("/post")
#def say_bye():
    #return render_template("post.html")
@app.route("/post/<int:id>")
def say_bye(id):
    for blog in response:
        if blog['id']==id:
            req_blog=blog
    return render_template("post.html",x=req_blog)
#def say_bye(name):
 #    return f"bye {name}"
if __name__=="__main__":
    app.run(debug=True)


