# srm-rh-ui
User Interface for respondents to access ONS Survey Data Collection questionnaires and services


# A bit of explanation

## View functions

In the views folder we define our view functions as Flask Blueprints (following the pattern from ras-frontstage)

Then (and this is a change from the ras ui pattern explained below) we register the blueprints against our Flask app in the `create_app` function

# Questions
## How will we go about defining app configs? 
It seems that RAS UI picks up the app config through env variables, but at the same time in each config they add a boolean variable that describes what the config is supposed to be (TESTING, DEVELOPMENT etc.)
To do: investigate how that was done in the old RH-UI, decide what works for us better

# Comments

## Global `app` object
It seems that RASRM create the app in the __init__.py file making it avaiable in the whole project
I didn't see any benefit in that for us, and it entails some complications (for example in tests), so I decided to leave the app creation in the run.py script 
All the app configuration happens in the `create_app` function instead

## Error blueprints 
For HTML error handling we could consider registering error blueprints, something like:
```
@blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html')
```
(I got the inspiration from the microblog tutorial)

## Logging config
I've implemented simple logging, but we'll definetely have to review it and make sure that it suits our needs and matches the Stackdriver layout
It'd also be good to add some tests for the log config