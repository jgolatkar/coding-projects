from flask import Flask, render_template, flash, request, redirect, send_file
import pandas
import datetime
from geopy.geocoders import Nominatim

app = Flask(__name__)
app.secret_key = '864dfds331'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/success-table', methods=['POST'])
def success_table():
	global filename
	if request.method == 'POST':
		if 'file' not in request.files:
			flash('No file part')
			return render_template('index.html')	
		else:
			fl = request.files['file']
			try:
				gc = Nominatim()			
				df = pandas.read_csv(fl)
				df['coordinates'] = df['Address'].apply(gc.geocode)
				df['Latitude'] = df['coordinates'].apply(lambda x: x.latitude if x != None else None)
				df['Longitude'] = df['coordinates'].apply(lambda x: x.longitude if x != None else None)
				df = df.drop('coordinates',1)
				filename = datetime.datetime.now().strftime('geocoded_files/%Y-%m-%d %H-%M-%S-%f'+'.csv')
				df.to_csv(filename,index=None)
				return render_template('index.html',text=df.to_html(),btn='download.html')		
			except Exception as e:
				return render_template('index.html',text="Column Address/address does not exist in your CSV file!")
@app.route('/download-file/')
def download():
	return send_file(filename, as_attachment=True)
	
	
if __name__ == '__main__':
	app.debug = True
	app.run()
