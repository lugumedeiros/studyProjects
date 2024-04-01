#include <iostream>
#include <vector>

int main() {
	unsigned long int value{};
	unsigned long int base{};
	std::cout << "Please, give the value and base wanted with a space in between: ";
	std::cin >> value >> base;
	std::cout << std::endl;
	if (base <= 1) { std::cout << "base less than 2 is not allowed."; exit; };
	std::vector<unsigned long int> number{};
	while (value >= base*base){

		number.push_back(value % base);
		value = value / base;
	}
	number.push_back(value % base);
	number.push_back(value / base);

	std::reverse(number.begin(),number.end());
	for (auto i : number) {
		if (base != 16) {
			std::cout << i << " ";
		} else {
			switch (i) {
			case 10: std::cout << 'A' << " "; continue;
			case 11: std::cout << 'B' << " "; continue;
			case 12: std::cout << 'C' << " "; continue;
			case 13: std::cout << 'D' << " "; continue;
			case 14: std::cout << 'E' << " "; continue;
			case 15: std::cout << 'F' << " "; continue;
			default: std::cout << i << " ";
			}
		}
	}
	return 0;
}
