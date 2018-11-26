import dash_html_components as html
import dash_core_components as dcc
import dash_table_experiments as dt

mylayout = html.Div(
	html.Div(
		html.Div(
			html.Button('Submit', id='button', className="navbar-toggle"),
			className="navbar-header"), 
		className="container-fluid"),
	className="navbar navbar-inverse")