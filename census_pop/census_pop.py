# Now: P224页操作普查表，正在进行时
import openpyxl
wb = openpyxl.load_workbook("censuspopdata.xlsx")
ws = wb.active
countyData = {}

# ToDo: fill in countyData with each county's population and trace.
print("{:.^20}".format("Reading rows"))
for row in range(2, ws.max_row() + 1):
    # Each row in the spreadsheet has data for one census tract.
    state = ws['B' + str(row)].value
    county = ws['C' + str(row)].value
    pop = sheet['D' + str(row)].value

# Todo:Open a new text file and write the contents of countyData to it.

# Make sure the key for this state exists
countyData.setdefault(state, {})
# Make sure the key for this county in this state exists.
countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})
# Each row represents one census tract, so increment by one.
countyData[state][county]['tracts'] += 1
# Increase the county pop by the pop in this census tract.

# Todo: Open a new text file and write the contents of countyData to it.
