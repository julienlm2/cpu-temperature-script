import psutil

def get_cpu_temperature():
    try:
        # This works on Linux with 'sensors' package installed
        temp = psutil.sensors_temperatures().get('coretemp', None)
        if temp:
            return temp[0].current
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    temperature = get_cpu_temperature()
    if temperature:
        print(f"CPU Temperature: {temperature}°C")
    else:
        print("Could not get CPU temperature.")
