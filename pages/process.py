import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## **Process**

            """
        ),
	dcc.Markdown(
	    """
	    #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The [data](https://www.kaggle.com/drgilermo/nba-players-stats) for my project consisted of 24,691 observations and 64 features. When I was done cleaning the data, I ended up with 24,691 observations, seven features, and a mean baseline of 63.4%. I wanted to find out if it was possible to accurately predict what percentage of a season an NBA player should play based on prior stats of similar athletes. It came as no surprise that points were the most significant indicator of season gameplay when looking at the permutation importance on the right. Permutation importance served as a quick way to understand what features have the most significant effect on our predictions. 
 	    """
	)	

    ]
)

column2 = dbc.Col(
    [                                                                                               
	html.Img(src='assets/permutation.png',
		className='img-fluid', 
		style={'margin-left': '50px', 'margin_right': 'auto','margin-top':'15px' ,'display':'block'})
    ]
)

column3 = dbc.Col(
    [
	dcc.Markdown(
	    """
	    #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Looking below, we can see a partial dependency plot that shows the marginal effect of "PTS" (Points) had on the predicted outcome of our model. These PDP plots are great for understanding if the target and feature are linear,  monotonic, or more complex. We can see there is a monotonic relationship between "PTS" and our target "season_pct_played". We can see the most significant marginal increase when going from 0-99 points scored in a season
	    """
	)
    ]
)

column4 = dbc.Col(
    [
	html.Img(src='assets/pdp.png',className='img-fluid')
]
)

column5 = dbc.Col(
    [
	dcc.Markdown(
	    """
	    #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The target of my model was "season_pct_played". I divided the number of games played by the total amount of season games to determine what percent of the season was played by a player in my data set. My model used an [XGBRegressor](https://xgboost.readthedocs.io/en/latest/python/python_api.html) model that allowed me to achieve an R^2 score of ~0.81 and a root mean squared error (RMSE) of ~0.14. With these two scores, we can tell the model explains about 81%(R^2) of the variance seen in the data, and the RMSE tells us how far our predictions deviate from the actual values, about 14%.
	    """
	)
    ]
)

column6 = dbc.Col(
    [
	html.Img(src='assets/normal.png',className='img-fluid'),
	html.Img(src='assets/zoom.png',className='img-fluid', style={'margin-left':'75px'})
    ]
)

column7 = dbc.Col(
    [
	dcc.Markdown(
	    """
	    #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; To assure myself that the model I had chosen was the best, I decided to open up the model and look at how many trees it took my ensemble to achieve the best RMSE. What I found out was at 25 trees; my model could no longer improve its score significantly enough to impact my predictions substantially. Looking at the two graphs above, we can see precisely when the benefit of boosting subsided, and I had reached my best model. Zooming in, we can see the fluctuation that took place before reaching my best model at 25 trees in my ensemble. 
	    """
	)
    ]
)

row1 = dbc.Row([column1,column2])
row2 = dbc.Row(column3)
row3 = dbc.Row(column4)
row4 = dbc.Row(column5)
row5 = dbc.Row(column6)
row6 = dbc.Row(column7)
layout = dbc.Row([row1,row2,row3,row4,row5,row6])
