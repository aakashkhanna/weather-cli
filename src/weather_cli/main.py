import typer
from weather_cli.models.config import Config
from weather_cli.services.weather_data_service import WeatherDataService

app = typer.Typer()
import os

@app.command()
def temparature():
    typer.echo("Checking Config")
    typer.echo("Checking Temparature")
    path = "~/.weather-cli"
    full_path = os.path.expanduser(path)
    if os.path.exists(full_path):
        typer.echo("Config Found.")
        config_content = Config.parse_file(full_path)
        temparature = WeatherDataService.get_temparature(config_content.latitude, config_content.longitude)
        if temparature > 30:
            temparature_style = typer.style(f"{temparature}", fg=typer.colors.RED, bold=True)
        elif temparature <= 30:
            temparature_style = typer.style(f"{temparature}", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"Temparature: {temparature_style}")
    else:
        typer.echo("Config Not Found.")
        typer.echo("Run weather-cli init {latitude} {longitude} to initialize.")
@app.command()
def windspeed():
    typer.echo("Checking Windspeed")
    path = "~/.weather-cli"
    full_path = os.path.expanduser(path)
    if os.path.exists(full_path):
        typer.echo("Config Found.")
        config_content = Config.parse_file(full_path)
        windspeed = WeatherDataService.get_windspeed(config_content.latitude, config_content.longitude)
        if windspeed > 30:
            windspeed_style = typer.style(f"{windspeed}", fg=typer.colors.RED, bold=True)
        elif windspeed > 20:
            windspeed_style = typer.style(f"{windspeed}", fg=typer.colors.YELLOW, bold=True)
        elif windspeed <= 20:
            windspeed_style = typer.style(f"{windspeed}", fg=typer.colors.GREEN, bold=True)
        typer.echo(f"Windspeed: {windspeed_style}")
    else:
        typer.echo("Config Not Found.")
        typer.echo("Run weather-cli init {latitude} {longitude} to initialize.")

@app.command()
def init(latitude, longitude):
    typer.echo("Checking Config")
    config = Config(latitude=latitude, longitude=longitude)
    path = "~/.weather-cli"
    full_path = os.path.expanduser(path)
    config_content = config.json()
    with open(full_path, "w") as config_file:
        config_file.write(config_content)
    typer.echo(f"Created Config at {full_path}")