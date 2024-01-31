def add_time(time, addition, current_day=None):
  time = time.split()
  timebyminute = time[0].split(":")
  hours = int(timebyminute[0])
  minutes = int(timebyminute[1])

  addition = addition.split(":")
  hours_add = int(addition[0])
  minutes_add = int(addition[1])

  if time[1] == "PM":
    hours += 12

  sum_minutes = minutes + minutes_add
  additional_hours = int(sum_minutes / 60)
  sum_minutes = sum_minutes % 60 

  sum_hours = hours + hours_add + additional_hours
  additional_days = int(sum_hours / 24)
  sum_hours = sum_hours % 24

  if sum_hours > 12:
    sum_hours += -12
    sum_PM = "PM"
  elif sum_hours == 12:
    sum_PM = "PM"
  elif sum_hours == 0:
    sum_hours = 12
    sum_PM = "AM"
  else:
    sum_PM = "AM"

  sum_hours = str(sum_hours)

  if sum_minutes < 10:
    sum_minutes = str(sum_minutes)
    sum_minutes = "0" + sum_minutes
  else:
    sum_minutes = str(sum_minutes)
  
  day_dict_letters = {"Monday":1,"Tuesday":2, "Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6, "Sunday":7}
  day_dict_sum = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
  
  if current_day != None:
    current_day = current_day.capitalize()
    day_num = day_dict_letters.get(current_day)
    final_day_num = day_num + additional_days
    final_day_num = final_day_num % 7
    if final_day_num == 0:
      final_day_num = 7
    final_day_letters = day_dict_sum.get(final_day_num)
    final_day_letters = ", " + final_day_letters

  day_print = ""
  if additional_days == 1:
    day_print = " (next day)"
  if additional_days > 1:
    additional_days = str(additional_days)
    day_print = " ("+ additional_days + " days later)"
  
  if current_day == None:
    answer = sum_hours + ":" + sum_minutes + " " + sum_PM + day_print
  else:
    answer = sum_hours + ":" + sum_minutes + " " + sum_PM + final_day_letters + day_print
  return answer


