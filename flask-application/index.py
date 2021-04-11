from flask import *

app=Flask(__name__)

@app.route("/")
@app.route("/<file>")
@app.route("/<file>/<fp>/<lp>")
@app.route("/<file>/<fp>")
def home(file="file1",fp=0,lp=-1):
	try:
		fp=int(fp)
		lp=int(lp)
		with open(file+".txt","r",encoding="cp437")as f1:
			d=f1.readlines()
		if lp==-1:
			lp=len(d)
		return render_template("index.html",data=d[fp:lp+1])
	except (FileNotFoundError):
		return "File Not Found "
	


# last lines
if __name__ =="__main__":
	app.run(debug=True)


