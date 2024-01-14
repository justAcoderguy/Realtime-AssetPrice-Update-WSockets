"""Grab data from Binance WS and saving to sqlite3 file"""

from websockets import connect
import asyncio
import sys
import sqlite3
import aiosqlite3
import json

conn = sqlite3.connect("./data.db")
cursor = conn.cursor()

# Dropping table between reruns of program
cursor.execute("DROP TABLE IF EXISTS trades")
cursor.execute("""CREATE TABLE trades(
               id int PRIMARY KEY,
               time int, 
               quantity int, 
               price float)""")
cursor.execute("CREATE INDEX index_time ON trades(time)")

conn.commit()
conn.close()

url = "wss://stream.binance.com:9443/ws/btcusdt@aggTrade"

async def save_down(url):
    async with connect(url) as websocket:

        # To reduce the times we open and close a conn to the db we keep a buffer
        trades_buffer = [] 

        while True:
            data = await websocket.recv()
            data = json.loads(data)
            # tuple (id, time, quantity, price)
            trades_buffer.append((data['a'], data['T'], data['q'], data['p'])) 
            
            # Saves to database when trades buffer is full
            if len(trades_buffer) > 10:
                async with aiosqlite3.connect("./data.db") as db:
                    await db.executemany(""" 
                                        INSERT INTO trades
                                         (id, time, quantity, price) VALUES 
                                         (?,?,?,?)
                                         """, trades_buffer)
                    await db.commit()
                trades_buffer = []

asyncio.run(save_down(url))

