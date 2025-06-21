from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import requests
import pytz
from datetime import datetime, timedelta
from rich.console import Console
from rich.table import Table

console = Console()


def get_lat_lon_from_place(place_name):
    geolocator = Nominatim(user_agent="my-python-geocoding-app")
    try:
        location = geolocator.geocode(place_name, timeout=10)
        if location:
            return location.latitude, location.longitude
        else:
            console.print(
                f"[bold red]Could not find coordinates for: '{place_name}'. Check spelling or try a more specific name.[/bold red]")
            return None, None
    except (GeocoderTimedOut, GeocoderServiceError) as e:
        console.print(f"[bold red]Geocoding error: {e}[/bold red]")
        return None, None
    except Exception as e:
        console.print(f"[bold red]Unexpected error: {e}[/bold red]")
        return None, None


def get_weather_meteo(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=sunrise,sunset,temperature_2m_max,temperature_2m_min,precipitation_hours,precipitation_sum&current=temperature_2m,apparent_temperature,is_day,weather_code&timezone=GMT&forecast_days=1"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        console.print(f"[bold red]Error fetching weather data: {e}[/bold red]")
        return None
    except Exception as e:
        console.print(f"[bold red]Unexpected error: {e}[/bold red]")
        return None


def parse_weather_data(weather_data):
    try:
        timezone = weather_data.get("timezone", "GMT")
        current = weather_data.get("current", {})
        daily = weather_data.get("daily", {})
        if not current or not daily:
            console.print("[bold red]No weather data available.[/bold red]")
            return None
        tz = pytz.timezone(timezone)
        tz_kolkata = pytz.timezone("Asia/Kolkata")
        sunrise = datetime.fromisoformat(daily.get("sunrise", [None])[0]).astimezone(tz_kolkata)
        sunset = datetime.fromisoformat(daily.get("sunset", [None])[0]).astimezone(tz_kolkata)
        table = Table(title="Weather Report", show_header=True, header_style="bold magenta")
        table.add_column("Parameter", style="cyan", no_wrap=True)
        table.add_column("Value", style="green")
        table.add_row("Current Temperature (°C)", str(current.get("temperature_2m", "N/A")))
        table.add_row("Apparent Temperature (°C)", str(current.get("apparent_temperature", "N/A")))
        table.add_row("Is Day", "Yes" if current.get("is_day") else "No")
        table.add_row("Sunrise", sunrise.strftime("%d-%m-%Y %H:%M"))
        table.add_row("Sunset", sunset.strftime("%d-%m-%Y %H:%M"))
        table.add_row("Max Temperature (°C)", str(daily.get("temperature_2m_max", [None])[0]))
        table.add_row("Min Temperature (°C)", str(daily.get("temperature_2m_min", [None])[0]))
        table.add_row("Precipitation Hours (h)", str(daily.get("precipitation_hours", [None])[0]))
        table.add_row("Precipitation Sum (mm)", str(daily.get("precipitation_sum", [None])[0]))
        console.print(table)
        return table
    except Exception as e:
        console.print(f"[bold red]Error parsing weather data: {e}[/bold red]")
        return None


def get_weather(place_name):
    lat, lon = get_lat_lon_from_place(place_name)
    if lat is None or lon is None:
        return None
    weather_data = get_weather_meteo(lat, lon)
    if weather_data is None:
        return None
    return parse_weather_data(weather_data)