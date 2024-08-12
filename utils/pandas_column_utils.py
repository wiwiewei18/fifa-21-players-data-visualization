def contain_character(column, character):
    column_in_string = column.astype(str)

    return column_in_string.str.contains(character).any()


def remove_character(column, character):
    character_to_remove = f"[{character}]"

    return column.str.replace(character_to_remove, "", regex=True)


def convert_currency_to_number(column, currency):
    def currency_to_number(value):
        if isinstance(value, str):
            value = value.replace(currency, "").strip()

            if "K" in value:
                return int(float(value.replace("K", "")) * 1000)
            elif "M" in value:
                return int(float(value.replace("M", "")) * 1000000)
            else:
                return int(value)
        else:
            return value

    return column.apply(currency_to_number)
