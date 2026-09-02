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
        double saldo_atual(){
            return saldo;
        }
};
int main(){
    ContaBancaria x;
    int operacao;
    int lop;
    lop = 1;
    cout << "qual é o nome do titular? " ;
    cin >> x.titular;
    cout << "qual é o numero da conta? " ;
    cin >> x.conta;
    cout << "qual é o saldo da conta? ";
    cin >> x.saldo;
    while(lop==1){
   cout << "Operações: " << endl;
   cout << "1 - Depositar" << endl << "2 - Sacar" << endl << "3 - Ver Saldo" << endl;
   cin  >> operacao;
   if( operacao==1){
    cout << "insira o Valor a Depositar: ";
    cin >> x.valor;
    if(x.valor<0){
        cerr << "impossivel depositar valores negativos! ";
    }
    else{
        cout << x.depositar() << endl;
    }
   }
   else if( operacao==2){
    cout << "insira o Valor a Sacar: ";
    cin >> x.valor;
    if(x.valor>x.saldo || x.saldo<0){
        cerr << "impossivel sacar este valor, ";
    }
    else{
        cout << x.sacar() << endl;
    }
   }
   else {
    cout << "seu saldo é: R$" << x.saldo_atual() << endl;
   }
   cout << "deseja realizar mais uma operação?" << endl << "1 - SIM     0 - NÂO" << endl;
   cin >> lop;
}
 return 0;
}