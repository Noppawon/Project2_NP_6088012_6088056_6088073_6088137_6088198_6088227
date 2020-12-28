import faust
class Greeting(faust.Record):
    from_name: str
    to_name: str
    van_color: str
    station_number: int
app = faust.App('VanHubBusTerminal-app', broker='kafka://localhost:9092')
topic = app.topic('VanHubBusTerminal-topic', value_type=Greeting)

@app.agent(topic)
async def hello(greetings):
    async for greeting in greetings:
        print(f'Van which is color {greeting.van_color} arrived from {greeting.from_name} hub to {greeting.to_name} hub at the station number {greeting.station_number}')

@app.timer(interval=1.0)
async def example_sender_one(app):
    await hello.send(
        value=Greeting(from_name='A Building', station_number='103-111', van_color='Blue', to_name='Phuket'),
    )
@app.timer(interval=2.0)
async def example_sender_two(app):
    await hello.send(
        value=Greeting(from_name='B Building', station_number='112-120', van_color='Green', to_name='Nakorn Pathom'),
    )
@app.timer(interval=3.0)
async def example_sender_three(app):
    await hello.send(
        value=Greeting(from_name='C Building', station_number='121-132', van_color='Orange', to_name='Loey'),
    )
@app.timer(interval=4.0)
async def example_sender_four(app):
    await hello.send(
        value=Greeting(from_name='D Building', station_number='133-144', van_color='Violet', to_name='Pathum Thani'),
    )

if __name__ == '__main__':
    app.main()