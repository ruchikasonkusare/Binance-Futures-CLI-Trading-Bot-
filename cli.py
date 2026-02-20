import typer
from bot.client import BinanceFutureCLients
from bot.orders import create_order_payload
from bot.validators import validate_inputs

app = typer.Typer()
client = BinanceFutureCLients()


def place_order_interactive():

    typer.secho("\nPlace New Order\n", fg=typer.colors.CYAN)

    symbol = typer.prompt("Enter Symbol (e.g. BTCUSDT)").upper()
    side = typer.prompt("Side (BUY/SELL)").upper()
    order_type = typer.prompt("Order Type (MARKET/LIMIT/STOP)").upper()

    try:
        quantity = float(typer.prompt("Quantity"))
    except ValueError:
        typer.secho("Quantity must be a number.", fg=typer.colors.RED)
        return

    price = None
    stop_price = None

    if order_type in ["LIMIT", "STOP"]:
        try:
            price = float(typer.prompt("Limit Price"))
        except ValueError:
            typer.secho("Price must be a number.", fg=typer.colors.RED)
            return

    if order_type == "STOP":
        try:
            stop_price = float(typer.prompt("Stop Price"))
        except ValueError:
            typer.secho("Stop Price must be a number.", fg=typer.colors.RED)
            return

    try:
        validate_inputs(
            symbol,
            side,
            order_type,
            quantity,
            price,
            stop_price
        )
    except ValueError as e:
        typer.secho(f"\nValidation Error: {e}", fg=typer.colors.RED)
        return

    payload = create_order_payload(
        symbol,
        side,
        order_type,
        quantity,
        price,
        stop_price
    )

    typer.secho("\nOrder Summary", fg=typer.colors.YELLOW)
    typer.echo("----------------------------------")
    for k, v in payload.items():
        typer.echo(f"{k}: {v}")
    

    if not typer.confirm("\nConfirm order?"):
        typer.secho("Order cancelled.", fg=typer.colors.YELLOW)
        return

    response = client.place_order(payload)

    if response.get("orderId"):
        typer.secho("\nOrder Placed Successfully!", fg=typer.colors.GREEN)
        typer.echo(f"Order ID: {response.get('orderId')}")
        typer.echo(f"Status: {response.get('status')}")
        typer.echo(f"Executed Qty: {response.get('executedQty')}")
        typer.echo(f"Avg Price: {response.get('avgPrice')}")
    else:
        typer.secho("\nOrder Failed", fg=typer.colors.RED)
        typer.echo(response)


@app.command()
def menu():
    """
    Interactive Trading Menu
    """

    while True:

        typer.secho("\n=================================", fg=typer.colors.CYAN)
        typer.secho("   Binance Futures Trading Bot", fg=typer.colors.CYAN)
        typer.secho("=================================\n", fg=typer.colors.CYAN)

        typer.echo("1. Place Order")
        typer.echo("2. Exit\n")

        choice = typer.prompt("Select an option")

        if choice == "1":
            place_order_interactive()
        elif choice == "2":
            typer.secho("Existing..!!", fg=typer.colors.GREEN)
            break
        else:
            typer.secho("Invalid option.", fg=typer.colors.RED)


if __name__ == "__main__":
    app()
