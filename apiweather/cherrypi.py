import cherrypy
from api_weather import getWeather
class WeatherDashboardHTML:
    def __init__(self, currentWeather):
        self.currentWeather = currentWeather
    @cherrypy.expose
    def index(self):
        return """
            <!DOCTYPE html>
            <html lang="en">
            <head><title>Weather Dashboard</title>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/css/bootstrap.min.css"
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.0/umd/popper.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.1.0/js/bootstrap.min.js"></script>
            <style>
            .element-box {
            border-radius: 10px;
            border: 2px solid #C8C8C8;
            padding: 20px;
            }
            .card {
            width: 600px;
            }
            .col {
            margin: 10px;
            }
            </style>
            </head>
            <body>
            <div class="container">
            <br/>
            <div class="card">
            <div class="card-header">
            <h3>Weather Conditions for """ + self.currentWeather.get_city() + """
            </h3></div>
            <div class="card-body">
            <div class="row">
            <div class="col element-box">
            <h5>Temperature</h5>
            <p>""" + self.currentWeather.get_temperature() + """</p>
            </div>
            <div class="col element-box">
            <h5>Conditions</h5>
            <p>""" + self.currentWeather.get_condition() + """</p>
            </div>
            <div class="col element-box">
            <h5>Wind Speed</h5>
            <p>""" + self.currentWeather.get_wind() + """</p>
            </div>
            </div>
            </div>
            <div class="card-footer"><p>""" + self.currentWeather.get_time() + """</p></div>
            </div>
            </div>
            </body>
            </html>
            """
if __name__=="__main__":
    currentWeather = getWeather('Thai Nguyen')
    cherrypy.quickstart(WeatherDashboardHTML(currentWeather))