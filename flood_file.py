# AI BASED REAL TIME FLOOD MONITORING AND EARLY WARNING SYSTEM FOR BEAS RIVER


import numpy as np
import pandas as pd
import random
from flask import Flask, render_template_string
from sklearn.ensemble import RandomForestClassifier


data=[]
for i in range(1500):
    rainfall=random.uniform(0,200)
    river_level=random.uniform(2,10)
    flow_rate=random.uniform(50,500)
    soil_moisture=random.uniform(10,80)
    flood=1 if (rainfall>120 and river_level>7) else 0
    data.append([rainfall,river_level,flow_rate,soil_moisture,flood])

df=pd.DataFrame(data,columns=["rainfall","river_level","flow_rate","soil_moisture","flood"])
X=df.drop("flood",axis=1)
y=df["flood"]

model=RandomForestClassifier()
model.fit(X,y)


def generate_sensor_data():
    rainfall=random.uniform(0,200)
    river_level=random.uniform(2,10)
    flow_rate=random.uniform(50,500)
    soil_moisture=random.uniform(10,80)
    return [rainfall,river_level,flow_rate,soil_moisture]
     

def predict_flood(data):
    prediction=model.predict([data])[0]
    if prediction==1:
        return "FLOOD RISK "
    else:
        return "SAFE "


def send_alert(status):
    if status=="FLOOD RISK ":
        print("ALERT: Possible Flood in Beas River Basin!")


app=Flask(__name__)

HTML="""
<!DOCTYPE html>
<html>
<head>s
<title>Beas River Flood Monitoring</title>
<style>
body{font-family:Arial;text-align:center;background:#eef;}
.card{background:white;padding:20px;margin:40px auto;width:400px;border-radius:10px;box-shadow:0 0 10px gray;}
</style>
</head>
<body>
<div class="card">
<h1>AI Flood Monitoring</h1>
<h2>Beas River Basin</h2>
<p><b>Rainfall:</b> {{rain}}</p>
<p><b>River Level:</b> {{level}}</p>
<p><b>Flow Rate:</b> {{flow}}</p>
<p><b>Soil Moisture:</b> {{soil}}</p>
<h2>Status: {{status}}</h2>
</div>
</body>
</html>
"""

@app.route("/")
def dashboard():

    sensor_data=[150,8.5,300,60]   

    status=predict_flood(sensor_data)

    send_alert(status)

    return render_template_string(
        HTML,
        rain=round(sensor_data[0],2),
        level=round(sensor_data[1],2),
        flow=round(sensor_data[2],2),
        soil=round(sensor_data[3],2),
        status=status
    )


if __name__=="__main__":
    print("AI Flood Monitoring System Started...")
    app.run(debug=True)