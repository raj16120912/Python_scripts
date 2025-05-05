import seasons as s

months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

for month in months:
    if month >= "March" and month <= "May":
        print(f"{month}={s.season2}")
    elif month == "February":
        print(f"{month}={s.season1}")
    elif month >= "June" and month <= "September":
        print(f"{month}={s.season3}")
    else:
        print(f"{month}={s.season4}")
