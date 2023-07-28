# srm-rh-ui
User Interface for respondents to access ONS Survey Data Collection questionnaires and services



# A bit of explanation

## View functions

In the views folder we define our view functions as Flask Blueprints (following the pattern from ras-frontstage)

Then, in `views/__init__.py` they are then registered against the app object under the desired path

Then we have to bind the routes to the app in `rh_ui/__init__.py` like so:   
`from rh_ui import views`


### Something to consider:
Wouldn't it be better to register it against the Blueprint, rather then the app, like so:
`@hello_bp.route("/hello", methods=["GET"])` 

This would allow us to specify multiple paths and methods for a view function


# Questions
## Do we need the `static` folder? 

## How will we go about defining app configs? 
It seems that RASRM has some automatic way of picking up the correct config.
Also, in each config they add a boolean variable that describes what the config is supposed to be (TESTING, DEVELOPMENT etc.)
To do: investigate how that was done in the old RH-UI

# Things to do
## Logging config
## Do we need a static folder? 
## Deployment in Docker
## Copy over templates and i8n stuff 
including the Babel config
## Dev K8s deployment? 
## Docker push
To the GCR - is this of any use to us rn?
## Tests!
## GitHub Actions
https://github.com/ONSdigital/ssdc-rm-documentation/blob/main/guidelines/github-actions.md
orr just copy from the old rh

RAS frontstage link:
https://github.com/ONSdigital/ras-frontstage



