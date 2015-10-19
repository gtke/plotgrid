from flask import Flask
import optparse

def create_app(default_time_window=120):
    parser = optparse.OptionParser()

    parser.add_option("-t", "--time",
                        help="Width of the time window in secs" + \
                        "[default %s]" % default_time_window,
                        default=default_time_window
                        )

    options, _ = parser.parse_args()

    app = Flask(__name__)
    app.config['time_window'] = int(options.time)
    return app
