alert_failure_count = 0
treshold = 180.50

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    # First step is to add a treshold value into code
    # to define de max ok temp.
    # Then add a if to change the return behavior
    if celcius < treshold :
        return 200
    else:
        return 500

def alert_in_celcius(farenheit):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = network_alert_stub(celcius)
    print(returnCode)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0
        # I going to check if failure count are different from 0 because
        # if the response are not 200 this means that the response is not-ok
        # meaning that alert_failure_count doesn't be 0
        assert(alert_failure_count != 0)


alert_in_celcius(400.5)
alert_in_celcius(303.6)
print(f'{alert_failure_count} alerts failed.')
print('All is well (maybe!)')
