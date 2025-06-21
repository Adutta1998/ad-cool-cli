from utils.weather import get_weather
from utils.random_quote import get_random_quote
import typer

app = typer.Typer()


@app.command(name="get-weather")
def get_weather_command(place: str):
    weather_info = get_weather(place)


@app.command(name="test")
def test_command():
    get_random_quote()



if __name__ == "__main__":
    app()
