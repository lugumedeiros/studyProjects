//Refiz o projeto no C++ para aprendizado.
#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main(){
// Calculadora de IMC / IMC Calculator

    double peso;
    double altura;
    cout << "Calculadora de IMC para Adultos" << endl;
    cout << "Informe seu peso (kg) (exemplo 60.15):" << endl;
    cin >> peso;
    cout << "informe sua altura (m) (exemplo 1.78):" << endl;
    cin >> altura;
    cout << endl;

    //Formula para descobrir o IMC e calcular max e min peso
    double imc = peso / pow(altura, 2);
    double pesoIdealMin = 18.5 * pow(altura, 2);
    double pesoIdealMax = 24.9 * pow(altura, 2);

    //Teste para descobrir em que nível de IMC usuário está
    cout << setprecision(4);
    cout << "O seu IMC é: " << imc << endl;
    cout << "Você está ";
    if (imc < 18.5){
        cout << "Abaixo do peso" << endl;
    } else if (imc < 24.9){
        cout << "com Peso Normal" << endl;
    } else if (imc < 29.9){
        cout << "com Sobrepeso" << endl;
    } else if (imc < 34.9){
        cout << "com Obesidade Grau 1" << endl;
    } else if (imc < 39.9) {
        cout << "com Obesidade Grau 2" << endl;
    } else{
        cout << "com Obesidade Grau 3" << endl;
    }
    //Teste para sugerir pesos ideais
    if (imc < 18.5 || imc > 24.9){
        cout << "Seu peso ideal é de " << pesoIdealMin << " kg à "
        << pesoIdealMax << "kg" << endl;
    }


    //Seu peso ideal é imc: 25 a 29.9
    //25 = x / altura ** 2
}
