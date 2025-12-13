import datetime
from dateutil.relativedelta import relativedelta
from lxml import etree

START_DATE = "2025-01-01"


def get_uptime(start_date_str):
    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    diff = relativedelta(datetime.datetime.today(), start_date)
    return f"{diff.years}y {diff.months}m {diff.days}d"


def update_svg(file_path, uptime_value):
    tree = etree.parse(file_path)
    root = tree.getroot()

    element = root.find(".//*[@id='uptime']")
    if element is not None:
        element.text = uptime_value

    tree.write(file_path, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    uptime = get_uptime(START_DATE)

    update_svg("dark_mode.svg", uptime)
    update_svg("light_mode.svg", uptime)

    print("Uptime updated:", uptime)