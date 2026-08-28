#include <iostream>
#include <cmath>
using namespace std;

class ContaBancaria{
    public:
        string titular;
        string conta;
        double saldo;
        double valor;
        double depositar(){
              return  saldo = saldo + valor;
        }
        double sacar(){
           return saldo = saldo - valor;
        }
};
int main(){
    ContaBancaria x;
    cout << "qual é o nome do titular? " ;
    cin >> x.titular;
    cout << "qual é o numero da conta? " ;
    cin >> x.conta;
    cout << "qual é o valor que você quer depositar? "; 
    cin >> x.valor;
    cout << "qual é o seu saldo? " ;
    cin >> x.saldo;
    cout << x.titular << ", " << "conta número " << x.conta << ", " <<"o saldo é " << x.depositar() << endl; 
}