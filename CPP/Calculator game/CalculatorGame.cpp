#include <string>
#include <iostream>

// Simple game where user must answer calculations of +, - * or /.

int main() {
	std::string answer{};
	std::cout << "Welcome to the Amazing Calculator, where you're the amazing one!" << std::endl;
	std::cout << "Do you prefer to calculate numbers of 2, 3 or 4 digits?" << std::endl;
	while (answer != "2" && answer != "3" && answer != "4")
	{
		std::cin >> answer;
		if (answer != "2" && answer != "3" && answer != "4")
		{
			std::cout << "Wrong answer, try again!" << std::endl;
		}
	}
	std::cout << "Let's start! \n" << std::endl;

	int decimal_size = 0;
	if (answer == "2")
	{
		decimal_size = 100;
	}
	else if (answer ==  "3")
	{
		decimal_size = 1000;
	}
	else
	{
		decimal_size = 10000;
	}

	std::srand(0);

	bool winning = true;
	int user_count = 0;
	while (winning)
	{
		int number_1 = std::rand() % decimal_size;
		int number_2 = std::rand() % decimal_size;
		int random_operator = std::rand() % 4;
		int result = 0;
		int user_result = 0;
		switch (random_operator)
		{
		case 0:
			result = number_1 + number_2;
			std::cout << "What is " << number_1 << " + " << number_2 << " ? ";
			std::cin >> user_result;
			break;
		case 1:
			result = number_1 - number_2;
			std::cout << "What is " << number_1 << " - " << number_2 << " ? ";
			std::cin >> user_result;
			break;
		case 2:
			result = number_1 / number_2;
			std::cout << "What is " << number_1 << " / " << number_2 << " ? Use integers only: ";
			std::cin >> user_result;
			break;
		case 3:
			result = number_1 * number_2;
			std::cout << "What is " << number_1 << " * " << number_2 << " ? ";
			std::cin >> user_result;
			break;
		}
		if (user_result == result)
		{
			++user_count;
			std::cout << "Congratulations, you got it right! Your total points is " << user_count << std::endl;
			std::cout << "\n Next One is:" << std::endl;
		}
		else
		{
			std::cout << "Sadly you got it wrong and your streak ended with " << user_count << " rigth answers!";
			winning = false;
		}
	}
}
