#include <iostream>
#include <vector>
#include <string>
#include <cmath>

void number_to_base() {
	unsigned long int value{};
	unsigned long int base{};
	std::cout << "Please, give the value and desired base with a space in between: ";
	std::cin >> value >> base;
	std::cout << std::endl;
	if (base <= 1) { std::cout << "base less than 2 is not allowed."; return; };
	std::vector<unsigned long int> number{};
	while (value >= base * base) {

		number.push_back(value % base);
		value = value / base;
	}
	number.push_back(value % base);
	number.push_back(value / base);

	std::reverse(number.begin(), number.end());
	std::cout << "Result: ";
	for (auto i : number) {
			std::cout << i << " ";
	}
};

void base_to_number() {
	unsigned long int value{};
	unsigned long int base{};
	std::cout << "Please, give the value and it's base with a space in between: ";
	std::cin >> value >> base;
	if (base <= 1) { std::cout << "base less than 2 is not allowed."; return; };
	unsigned long int number{0};
	unsigned int base_size{};
	base_size = pow(10,std::to_string(base).length());

	unsigned long int base_potency{ 1 };
	while (value > base) {
		unsigned int n = value % base_size;
		value = value / base_size;
		number += n * base_potency;
		base_potency *= base;
	}
	number += value*base_potency;
	std::cout << "Result: " << number;
}

int main() {
	std::cout << "Simple number to base converter:";
	while (true) {
		std::cout << "\n\n1.Convert from decimal to any base.\n"
			<< "2.Convert from any base to decimal.\n"
			<< "3.Quit.\n"
			<< "Answer: ";
		unsigned int option{};
		std::cin >> option;
		switch (option) {
			case 1: number_to_base(); continue;
			case 2: base_to_number(); continue;
			default: std::cout << "Invalid number.";
		}
	}
	return 0;
}
