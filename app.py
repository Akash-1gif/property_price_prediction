from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LinearRegression

with open('variables/model.pkl','rb') as pkl_file:
    model=pickle.load(pkl_file)

with open('variables/location.pkl','rb') as pkl_file:
    locations=pickle.load(pkl_file)

print('pickle files loaded')

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    op=None
    locs=list(locations.keys())
    if request.method=='POST':
        num_of_bhk=request.form.get('num_of_bhk')
        selected_area=request.form.get('selected_area')
        num_of_bath=request.form.get('num_of_bath')
        num_of_bal=request.form.get('num_of_bal')
        area_size=float(request.form.get('area_size'))
       
        if num_of_bhk=='5 or more':
            num_of_bhk=5
        else:
            num_of_bhk=int(num_of_bhk)

        if num_of_bal=='5 or more':
            num_of_bal=5
        else:
            num_of_bal=int(num_of_bal)        

        if num_of_bath=='5 or more':
            num_of_bath==5
        else:
            num_of_bath=int(num_of_bath)
    
        loc=locations[selected_area]
        op=model.predict([[num_of_bhk,area_size,num_of_bath,num_of_bal,loc]])
        op=op[0]
        # return f"{op} Lakhs"

    return render_template('index.html',locs=locs,op=op)

if __name__ == '__main__':
    app.run()
