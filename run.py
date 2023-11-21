from booking.bookin_vacation import Booking

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.change_language()
    bot.select_location()
    bot.select_dates()
    bot.select_adults()
    bot.perform_search()


    # test test