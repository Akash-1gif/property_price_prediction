from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

with open('variables/model.pkl','rb') as pkl_file:
    model=pickle.load(pkl_file)

with open('variables/location.pkl','rb') as pkl_file:
    locations=pickle.load(pkl_file)

print('pickle files loaded')

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def home():
    locs=list(locations.keys())
    if request.method=='POST':
        num_of_bhk=request.form.get('num_of_bhk')
        selected_area=request.form.get('selected_area')
        num_of_bath=request.form.get('num_of_bath')
        num_of_bal=request.form.get('num_of_bal')
        area_size=float(request.form.get('area_size'))
        # Do something with the selected city, for example, redirect or render a new page
        print(num_of_bhk)
        print(selected_area)
        print(num_of_bath)
        print(num_of_bal)
        print(area_size)
        loc=locations[selected_area]



    return render_template('index.html',locs=locs)

if __name__ == '__main__':
    app.run()
