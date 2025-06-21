import requests
from rich import print as rprint

def get_random_quote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    try:
        response = requests.get(url, headers={'response-type': 'json'})
        response.raise_for_status()
        try:
            data = response.json()["data"]
        except Exception as e:
            rprint(f"[bold red]Error parsing response JSON:[/bold red] {e}")
            return
        quote = data.get('content', 'No quote found')
        author = data.get('author', 'Unknown')
        return rprint(f"[bold green]Quote:[/bold green] {quote}\n[bold blue]Author:[/bold blue] {author}")
    except requests.RequestException as e:
        rprint(f"[bold red]Error fetching quote:[/bold red] {e}")
        return