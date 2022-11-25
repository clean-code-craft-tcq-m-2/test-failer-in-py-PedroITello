# This is the file created for test alerter.py functionality
from alerter_prod import alert_in_celcius, clear_failures

# List to save responses
network_responses = []

# Function for read fails from server response
# With this we can know how many times fails server
def count_fails(responses):
    # Define a counter to made internal control of failures
    internal_failure_count = 0
    for response in responses:
        if response != 200:
            internal_failure_count += 1
    return internal_failure_count

# Testing case without fails
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(350.5)
network_responses.append(response_code)
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(303.6)
network_responses.append(response_code)

fails = count_fails(network_responses)
print(f'{alert_failure_count} alerts (stub) failed.')
print(f'{fails} alerts failed.')
# First test the predefined scenary in where nothing fails
# Check local responses failures
assert(fails == 0)
# Check network failures
assert(alert_failure_count == 0)
# Test network alerter failure count using the local count created using response_code
# to know if the alert count from network stub is working
assert(alert_failure_count == fails)
clear_failures()
network_responses.clear()
print('All is well (maybe!)')

# Testing case with one fail
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(400.5)
network_responses.append(response_code)
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(303.6)
network_responses.append(response_code)

fails = count_fails(network_responses)
print(f'{alert_failure_count} alerts (stub) failed.')
print(f'{fails} alerts failed.')
# Check local responses failures
assert(fails == 1)
# Check network failures (Because the functionality doesn't count errors in stub this launch an AssertionError)
assert(alert_failure_count == 1)
# Test network alerter failure count using the local count created using response_code
# to know if the alert count from network stub is working
assert(alert_failure_count == fails)
clear_failures()
network_responses.clear()
print('All is well (maybe!)')

# Testing case with multiple fails
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(400.5)
network_responses.append(response_code)
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(398.2)
network_responses.append(response_code)
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(303.6)
network_responses.append(response_code)
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(300.7)
network_responses.append(response_code)
alert_failure_count, response_code, network_temp_treshold = alert_in_celcius(366.3)
network_responses.append(response_code)

fails = count_fails(network_responses)
print(f'{alert_failure_count} alerts (stub) failed.')
print(f'{fails} alerts failed.')
# Check local responses failures
assert(fails == 3)
# Check network failures (Because the functionality doesn't count errors in stub this launch an AssertionError)
assert(alert_failure_count == 3)
# Test network alerter failure count using the local count created using response_code
# to know if the alert count from network stub is working
assert(alert_failure_count == fails)
clear_failures()
network_responses.clear()
print('All is well (maybe!)')