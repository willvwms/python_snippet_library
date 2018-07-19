from datetime import datetime

# ("(%I hrs) %M m :%S s") # 10:10 AM

def report (item_page_list, other_page_list, start_time):

	elapsed_time = datetime.now() - start_time

	print(str(len(item_page_list)) + " Item pages crawled")
	print(str(len(other_page_list)) + " Non-item pages crawled")
	print(str(len(item_page_list) + len(other_page_list)) + " total pages crawled")
	print("Time: " + str(elapsed_time))


def report_zeros(URLstotal, start_time):

	elapsed_time = datetime.now() - start_time
	
	print("Checked " + str(URLstotal) + " URLS in " + str(elapsed_time))
	return str(elapsed_time)


def show_progress(counter, totalURLs, start_time):

	# Calculate perfectage of URLs already reviewed
	percentage_complete = float(counter) / float(totalURLs) 
	percentage_complete *= 100

	# Generate a new timedelta object, and tease out the minutes / seconds:
	# delta = abs(datetime.now() - start_time)
	# hours, remainder = divmod(delta.total_seconds(), 3600)
	# minutes, seconds = divmod(remainder, 60)
	# time = '{:02}:{:02}:{:02}'.format(int(hours), int(minutes), int(seconds))
	# time = '{:02}:{:02}'.format(int(minutes), int(seconds))

	time = datetime.now().strftime('%I:%M %p')

	# Formatted only for hours and minutes as requested
	# time = "%s:%s:%s" % (hours, minutes, seconds)
	print("\t" + time + '\t' +  format(percentage_complete, '2.0f') + '% complete')  
