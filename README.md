# plotgrid
PlanGrid take-home challenge

### Description:
This simple webapp fetches data from ```http://my-sensor-api.herokuapp.com/meter``` endpoint and displays a rolling graph.

### Technologies Used:
- Python/Flask
- D3.js

####How to run:


1. Install dependencies from ```requirements.txt``` file.
2. ``` python app.py ``` or ``` python app.py -t [time_window]``` where ```time_window``` is a width of the time window in seconds. This defaults to ```time_window=120``` if not specified.
3. Go to ```http://localhost:5000/```
4. Yay!

### Live demo:
* [PlotGrid on Heroku](https://plotgrid.herokuapp.com/)
