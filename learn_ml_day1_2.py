import datetime
now = datetime.datetime.now()
# What is the average lot size (rounded to nearest integer)?
avg_lot_size = int(round(home_data['LotArea'].mean()))

# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = now.year - home_data['YearBuilt'].max()

# Checks your answers
step_2.check()
