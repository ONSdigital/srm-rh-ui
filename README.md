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
## How will we go about defining app configs? 
It seems that RASRM has some automatic way of picking up the correct config.
Also, in each config they add a boolean variable that describes what the config is supposed to be (TESTING, DEVELOPMENT etc.)
To do: investigate how that was done in the old RH-UI

# Things to do
## Logging config
## Tests!

## Add packages in the dependabot config
## Uncoment bits in GH actions

RAS frontstage link:
https://github.com/ONSdigital/ras-frontstage

## Comments
It seems that RASRM create the app in the __init__ file making it avaiable in the whole package
I didn't see any use of that in our case, so I decided to leave the app creation in the run.py script 
leaving all the configuration in the create_app function



