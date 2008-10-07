from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from views import get_guy#, end_ga, get_info, manage_ga, reset_ga, start_ga, generate_ga_js

application = webapp.WSGIApplication(
    [
        #('/start_ga', start_ga),
        #('/end_ga', end_ga),
        #('/manage_ga', manage_ga),
        #('/reset_ga', reset_ga),
        #('/get_info', get_info),
        #('/generate_ga_js', generate_ga_js),
        ('/get_guy', get_guy),
    ],
    debug=True
)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()

