import requests

gas = {
    "carbon monoxide": "42101",
    "sulfur dioxide": "42401",
    "nitrogen dioxide (NO2)": "42602",
    "ozone": "44201",
    "pm10": "81102"
}


def extract_sample_measurements(response):
    data = response.json().get("Data", [])
    sample_measurements = [entry.get("sample_measurement") for entry in data if entry.get(
        "sample_measurement") is not None]
    return sample_measurements


def current_data(day, month, year, state, gas_name) -> float:
    gas_name = gas_name.lower()

    if month < 10:
        date = str(year - 1) + "0" + str(month) + str(day)
    elif 10 <= month <= 12:
        date = str(year - 1) + str(month) + str(day)

    if state < 10:
        state = "0" + str(state)

    url_template = "https://aqs.epa.gov/data/api/sampleData/byState?email=test@aqs.api&key=test&param={}&bdate={}&edate={}&state={}"
    url = url_template.format(gas[gas_name], date, date, state)

    response = requests.get(url)

    if response.status_code == 200:
        sample_measurements = extract_sample_measurements(response)

        if sample_measurements:
            mean_sample_measurement = sum(
                sample_measurements) / len(sample_measurements)
            return mean_sample_measurement
        else:
            print("No valid sample measurements found.")
            return None
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None