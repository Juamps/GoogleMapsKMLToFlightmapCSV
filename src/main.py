from bs4 import BeautifulSoup
from datetime import date, datetime

## Flightmap required headers ALL MANDATORY
csv_header = '"ID","Name","Address","Phone Number","Date","Start Time","End Time","Latitude","Longitude"'
# csv_header = "".join(csv_header.split())  # Remove weird tabs from header FIX

phone_number = "5555555555"  # Phone number filler
today = date.today()
delivery_date = today.strftime("%m/%d/%y")  # Prompt user for date, default today
start_time = (
    "00:01"  # Required, start at beginning of day [change if time restrictions]
)
end_time = "23:59"  # Required, finish at end of day [change if time restrictions]
id = 0  # Required, incremental

kml_file = "../files/18DeAbril.kml"  # Google Maps generated kml file path
file_date = today.strftime("%d %b, %Y")  ##Get date usable for file name
file_date = "".join(file_date.split())
file_date = "".join(file_date.split(","))
csv_file = "../files/" + file_date + ".csv"  # Write file path (CSV)

with open(kml_file) as f:
    soup = BeautifulSoup(f)

with open(csv_file, "w+") as f:
    print(csv_header)
    f.write(csv_header + "\n")
    for tag in soup.find_all("placemark"):
        id += 1

        name = tag.find("name").text
        name = name.strip()

        address = tag.find("description").text
        address = address.strip()

        coordinates = tag.find("coordinates").text
        latitude = coordinates.split(",")[1]
        longitude = coordinates.split(",")[0]

        row = (
            '"' + str(id) + '",'
            '"' + name + '",'
            '"' + address + '",'
            '"' + phone_number + '",'
            '"' + delivery_date + '",'
            '"' + start_time + '",'
            '"' + end_time + '",'
            '"' + str(latitude).strip() + '",'
            '"' + str(longitude).strip() + '"\n'
        )
        print(row)
        f.write(row)
