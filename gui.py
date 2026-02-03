from nicegui import ui

from godelizer import *

def create_app() -> None:
    ui.markdown("## Gödelizer")
    ui.label(
        "Enter a space-separated expression using your defined symbols in godelizer.py"
        "(e.g. `∀ x ( x = S 0 )`) to get its gödel number, or decode a "
        "gödel number back into tokens."
    )

    with ui.row().classes("w-full gap-10 mt-6"):
        #  Encoding
        with ui.column().classes("w-1/2"):
            ui.markdown("### expression → gödel number")
            expr_input = ui.input(
                label="Expression (space-separated tokens)",
                placeholder="∀ x ( x = S 0 )",
            ).classes("w-full")

            encode_output = ui.label().classes("mt-2 text-sm")

            def on_encode() -> None:
                expr = (expr_input.value or "").strip()
                if not expr:
                    encode_output.text = "Enter your expression."
                    return
                try:
                    g = godel_number(expr)
                    encode_output.text = f"Gödel number: {g}"
                except Exception as e:  # pragma: no cover - UI path
                    encode_output.text = f"Error: {e}"

            ui.button("Encode", on_click=on_encode)

        #Decoding
        with ui.column().classes("w-1/2"):
            ui.markdown("### gödel number → expression")
            num_input = ui.input(
                label="Gödel number",
                placeholder="e.g. 123456789",
            ).classes("w-full")

            decode_output = ui.label().classes("mt-2 text-sm")

            def on_decode() -> None:
                raw = (num_input.value or "").strip()
                if not raw:
                    decode_output.text = "Enter your gödel number."
                    return
                try:
                    n = int(raw)
                    expr = godel_number_decoder(n)
                    decode_output.text = f"Expression: {expr or '(empty)'}"
                except ValueError as e:
                    decode_output.text = f"invalid gödel number: {e}"
                except Exception as e:  # pragma: no cover - UI path
                    decode_output.text = f"Error: {e}"

            ui.button("Decode", on_click=on_decode)


@ui.page("/")
def index_page() -> None:  #UI entry point
    create_app()

if __name__ in {"__main__", "__mp_main__"}:
    # run with default settings
    ui.run()

