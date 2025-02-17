def card_printer(name, seat, plane_model, flight_number):
    text = f"| Passenger: {name}, Seat: {seat}, Model: {plane_model}, Flight number: {flight_number} |"
    frame = f"+{'-' * (len(text) - 2)}+"
    empty_frame = f"|{' ' * (len(text) - 2)}|"

    border = [frame, empty_frame, text, empty_frame, frame]
    border_text = "\n".join(border)
    print(border_text)
