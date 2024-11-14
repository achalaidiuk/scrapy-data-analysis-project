import re
from autoria.colors import color_palette


def extract_engine_info(engine_text):
    if engine_text:
        if "електро" in engine_text.lower() or "electric" in engine_text.lower():
            return "Electric"
        engine_volume = re.search(r"([0-9.]+)\s*л", engine_text)
        if engine_volume:
            return engine_volume.group(1)
    return "Не вказано"

def extract_horsepower(horsepower_text):
    if horsepower_text:
        in_brackets = re.search(r"\((.*?)\)", horsepower_text)
        if in_brackets:
            horsepower = in_brackets.group(1)
            horsepower_value = re.search(r"(\d+)\s*к\.с\.", horsepower)
            return horsepower_value.group(1) if horsepower_value else None
    return "Не вказано"

def extract_color(color_texts):
    colors = [clean_color(text) for text in color_texts if text]
    valid_colors = [color for color in colors if color]
    return ", ".join(valid_colors) if valid_colors else "Не вказано"

def clean_color(value):
    value = re.sub(r"[^a-zа-яіїєґ0-9\s]", "", value.strip().lower())
    return next((color.capitalize() for color in color_palette if color in value), None)

def extract_fuel_type(fuel_text):
    if fuel_text:
        fuel_text = fuel_text.strip().lower()
        for fuel in ["електро", "дизель", "газ", "гібрид", "бензин"]:
            if fuel in fuel_text:
                return fuel.capitalize()
    return "Не вказано"

def extract_gearbox(gearbox_texts, fuel_type_text):
    gearboxes = []
    if fuel_type_text and "електро" in fuel_type_text.lower():
        gearboxes.append("Автомат")
    else:
        for text in gearbox_texts:
            if text:
                text = text.strip().lower()
                if "автомат" in text:
                    gearboxes.append("Автомат")
                elif "механіка" in text or "ручна" in text:
                    gearboxes.append("Механіка")
    return ", ".join(set(gearboxes)) if gearboxes else "Автомат"
