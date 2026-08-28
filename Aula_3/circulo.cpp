#include <iostream>
#include <cmath>
using namespace std;

class circulo{
public:
    double raio;
    double area() {
        return M_PI * raio * raio;
    }
    double circumferencia() {
        return M_PI * raio * 2;
    }
};

int main() {
 circulo x;
 circulo y;
 cin >> x.raio >> y.raio;
 
 cout << x.raio << " " << x.area() << " " << x.circumferencia() << endl;
 cout << y.raio << " " << y.area() << " " << y.circumferencia() << endl;
}