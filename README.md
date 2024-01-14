# Realtime Price Updater and Number of Trades Viewer

In this project, I tried to use websocket connection provided by Binance to get real time aggregated trade information about the BTCUSDT pair. I then displayed the current price of the pair, which updates every 200ms ( this can be reduced further by tweaking the update_frequency variable in the code ) along with a graph which lets us know the number of trades at any point of time ( in the last 1 min - updates 200ms as well).

I focused on using websockets here to get realtime data and didn't really focus on styling or visualizing the project much. If you want to see a visualization project where I styled data from Binance API into an orderbook, please click here :
https://github.com/justAcoderguy/OrderBook-Visualization
or to check out another visualization project where I visualized how a virus spreads in a population, click here:
https://github.com/justAcoderguy/VirusSimulation

#### How?
I've used Binance's websocket to get realtime trade updates of the BTCUSDT pair. The trades are then put in a buffer, once the buffer reaches 10 trades, it is written into an sqlite3 database. This buffer is necessary as sqlite3 isnt the best at concurrency. In real world applications, we would use better suited databases. The database has an index which is the time field so its faster to query later on.
I've used **Plotly Dash** in python to query the data from the database at an interval of 200ms and shown the current price and number of trades for the last 1 minute at any given point in time

#### Why?
Because why not? I've been trading the forex and crypto market for more than 4 years now. Although I'm not the best trader out there ( I'm working on it :joy: ), I loved the visualisations we are 
provided with. And I wanted to do it myself! AND I wanted to try out the realtime websocket data :))
#### Lets see it?
Sure! - Please note this was recorded on a Sunday so the number of trades are a bit low and the price doesnt update as quick. 

https://github.com/justAcoderguy/Realtime-AssetPrice-Update-WSockets/assets/52568587/849b037e-a9fe-4e26-8743-29a33595b2d5
