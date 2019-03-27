import openpyxl, pprint
print('Opening workbook...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData  ={}
#TODO : fill in countydata with each county's population and tracts.
for row in range(2,sheet.get_highest_row()+1):
	state = sheet['B' + str(row)].value
	county = sheet['C'+str(row)].value
	pop = sheet['D'+str(row)].value
	countyData.setDefault(state,{})
	countyData[state].setDefault(county,{'tracts':0,'pop':0})
	countyData[state][county]['tracts']+=1
	countyData[state][county]['pop']+=int(pop)
print('Writing results')
resultFile = open('census2010.py','w')
resultFile.write('allData ='+ pprint.pformat(countyData))
resultFile.close()
print('Done:)')
