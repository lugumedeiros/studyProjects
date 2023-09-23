#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>

int main(){
  //This is a program that will give the calendar for any year you want, there's no need to give
  //more inormation, this works because leap years obey a simple formula.
  //By giving any year +  the correct first day, we can then fix the offset to find any calendar for any year.
  //This code is a bit of a mess because I'm just learning C++, and I'm also very new to programming.
  
  int year = 0;
  std::string weekday[7] = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"};
  std::string month[12] = {"January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December"};
  std::string shorted_weekday[7] = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
  
  std::cout << "Welcome to the calendar of future and past!\nWhat year would you like to see?" << std::endl;
  std::cin >> year;
  if (year < 0)
  {
    year += 1;
  }
  
  int div_100 = std::ceil(year / 100.0); 
  int div_400 = std::ceil(year / 400.0);
  int div_4 = std::ceil(year / 4.0);
  int formula = (6 + year + div_4 - div_100 + div_400) % 7;
  
  std::cout << "\nThe first day of the week in the year " << year << " is " << weekday[formula] << std::endl;
  
  bool is_leap = (year % 4 == 0) & !((year % 100 == 0) ^ (year % 400 == 0));
  int day = 1;
  int dayweek = 0;
  bool end_month = false;
  int max_days = 0;
  
  //Loop for the calendar
  for (int i = 0; i < 12 ; ++i)
  {
    std::cout << "        -- " << month[i] << " " << year << " --" << std::endl;
    std::cout << "  ";
    for (int j = 0; j < 7; ++j) 
    {
      std::cout << shorted_weekday[j] << "  ";
    }
    std::cout << std::endl;
    
    switch (i) 
    {
      case 0: case 2: case 4: case 6: case 7: case 9: case 11:
      {
        max_days = 31;
        break;
      }
      case 3: case 5: case 8: case 10:
      {
        max_days = 30;
        break;
      }
      case 1:
      {
        if (is_leap){
          max_days = 29;
          break;
        } 
        else 
        {
          max_days = 28;
          break;
        }
      }
    }
    int fix_cal = 0;
    while (end_month == false)
      {
        for (dayweek = 0; dayweek < 7; ++dayweek)
        {
          //end of loop
          if (day > max_days)
          {
            formula = ((formula + max_days) % 7);
            day = 1;
            dayweek = 0;
            end_month = true;
            fix_cal = 0;
            break;
          }
          if (fix_cal >= formula) 
          {
            std::cout << "" << std::setw(5) << day++ << "";
          } else 
          {
            std::cout << std::setw(5) << "-";
            ++fix_cal;
          }
        }
        std:: cout << std::endl;
      }
      std::cout << std::endl;
      end_month = false;
    }
    std::cout << "\n" << std::endl;
}
