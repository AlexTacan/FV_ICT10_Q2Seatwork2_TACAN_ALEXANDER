from pyscript import document, display


def general_weighted_average(e):
    subjects = ['Science', 'Math', 'English', 'Filipino', 'ICT', 'PE']
    Science = float(document.getElementById('Science').value)#gets the value of the science grade from the html
    Math = float(document.getElementById('Math').value)#gets the value of the math grade from the html
    English = float(document.getElementById('English').value)#gets the value of the english grade from the html
    Filipino = float(document.getElementById('Filipino').value)#gets the value of the filipino grade from the html
    ICT = float(document.getElementById('ICT').value)#gets the value of the pe grade from the html
    PE = float(document.getElementById('PE').value)#gets the value of the pe grade from the html
    FirstName = str(document.getElementById('FirstName').value)#gets the first name from the html
    LastName = str(document.getElementById('LastName').value)#gets the last name from the html
    weighted_sum = (Science * 5 + Math * 5 + English * 5 + Filipino * 3 + ICT * 2 + PE * 1)
    total_units = (5 * 3) + 3 + 2 + 1
    gwa = weighted_sum / total_units #GWA is computed by multiplying all the subjects and its weight then getting the sum, then dividing by the total weight

    summary = f"""{subjects[0]}: {Science:.0f}
{subjects[1]}: {Math:.0f}
{subjects[2]}: {English:.0f}
{subjects[3]}: {Filipino:.0f}
{subjects[4]}: {ICT:.0f}
{subjects[5]}: {PE:.0f}
    """
    display(f'Name: {FirstName} {LastName}', target="student_info")
    display(summary, target='summary')
    display(f'Your general weighted average is {gwa:.2f}', target='output')

