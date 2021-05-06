import pandas as pd
import plotly.express as px 
data = {
    'roll_no.':[1,2,3,4,5],
    'marks':[230,230,242,234,243]
}
df = pd.read_csv('line_chart.csv')
fig = px.line(df,x = 'Year',y = 'Per capita income',color='Country',title = 'Per capita income')
fig.show()