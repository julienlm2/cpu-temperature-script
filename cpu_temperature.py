import psutil
import xml.etree.ElementTree as ET

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

def create_junit_report(temperature):
    testsuite = ET.Element("testsuite", name="CPU Temperature Suite", tests="1", errors="0", failures="0")
    testcase = ET.SubElement(testsuite, "testcase", classname="cpu_temperature", name="test_cpu_temperature")
    if temperature is not None:
        ET.SubElement(testcase, "system-out").text = f"CPU Temperature: {temperature}°C"
    else:
        ET.SubElement(testcase, "failure", message="Could not get CPU temperature").text = "Could not get CPU temperature."

    tree = ET.ElementTree(testsuite)
    tree.write("cpu_temperature_report.xml")

if __name__ == "__main__":
    temperature = get_cpu_temperature()
    create_junit_report(temperature)
    if temperature:
        print(f"CPU Temperature: {temperature}°C")
    else:
        print("Could not get CPU temperature.")
