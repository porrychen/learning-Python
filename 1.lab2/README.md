Lab 2  Simple calculations
------------------

First
  declare a class Convertor

  declare input_us_measures method
    get self.__us
    try except ValueError
    return self.__us

  declare output_metric_measures method
    display and format a converted result

  declare miles_to_kilometers method
    call self.input_us_measures
    Calculate self.__metric = self.__us * 1.6
    call output_metric_measures

  declare fahrenheit_to_celsius method
    call self.input_us_measures
    Calculate self.__metric = (self.__us - 32) * 5//9
    call output_metric_measures

  declare gallons_to_liters method
    call self.input_us_measures
    Calculate self.__metric = self.__us * 3.9
    call output_metric_measures

  declare pounds_to_kilograms method
    call self.input_us_measures
    Calculate self.__metric = self.__us * 0.45
    call output_metric_measures

  declare inches_to_centimeters method
    call self.input_us_measures
    Calculate self.__metric = self.__us * 2.54
    call output_metric_measures

Second
  declare Global constants

  declare get_menu_data function
    return a Dictionary

  declare get_menu_choice function
    get menudata = get_menu_data
    display a menu
    return a choice

  declare main function
    declare a Convertor object convertor

    loop verifty the user's choice
      if choice == 1, call convertor.miles_to_kilometers method
      if choice == 2, call convertor.fahrenheit_to_celsius method
      if choice == 3, call convertor.gallons_to_liters method
      if choice == 4, call convertor.pounds_to_kilograms method
      if choice == 5, call convertor.inches_to_centimeters method
      if choice == 9, quit this program

Finally
  call main function
