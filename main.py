import csv
import re

#We have 4 steps to get an abbreviated table of all employees:

#1 - open csv file
#2 - fill dates and workers no repeat
#2.1 -  filling firstline with date
#3 - getting lists of work hours for each worker
#4 - write new csv file



#correct date format
def correctDate(mounths, date):
		mounth = mounths.index(re.search(r'\w+', date).group(0)) + 1
		day = re.search(r'\d+', date).group(0)
		year = re.search(r'\d{4}', date).group(0)
		return '{}-{:02}-{}'.format(year, mounth, day)

#default values
lines = []
dates = []
workers = []
writeLines = []
firstLine = []
mounths = ['Jan', 'Feb', 'Mar', 'Apr', 'May' , 'Jun', 'Jul', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

#write header firstline 
firstLine.append('Name / Date')

#1 - open csv file
with open('acme_worksheet.csv') as inputfile:
	reader = csv.DictReader(inputfile, delimiter  = ',')
	for row in reader:
		lines.append(row)


#2 - fill dates and workers no repeat
for line in lines:
	if line['Date'] not in dates:
		dates.append(line['Date'])
		firstLine.append(correctDate(mounths, line['Date'])) #2.1 - Filling firstline with date
	if line['Employee Name'] not in workers:
		workers.append(line['Employee Name'])


workers.sort()

#add firstline in writelines
writeLines.append(firstLine)


#3 - getting lists of work hours for each worker
for worker in workers:
	workerWorkDates = [] # WORKER WORK DATES
	workerWorkHours = [] # WORKER WORK HOURS with dates
	workerWorkHours.append(worker) #add worker name
	for line in lines:
		if line['Employee Name'] == worker:
			workerWorkDates.append(line['Date']) #filling workerWorkDates for current worker
	for date in dates:
		if date in workerWorkDates: #Checking for work these dates
			for line in lines:
				if line['Employee Name'] == worker and line['Date'] == date:
					workerWorkHours.append(line['Work Hours'])
		else:
			workerWorkHours.append(0)
	writeLines.append(workerWorkHours) #add workhours to writelines

#4 write new csv file
with open('output.csv', "w", newline="") as file: 
    writer = csv.writer(file)
    writer.writerows(writeLines)

inputfile.close()
file.close()