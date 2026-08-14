#include <iostream>
//using namespace std
    int main(){
        std::string name;
        std::cout << "what's your name? ";
        std::cin >> name;
        std::cout << "hello " << name << "!" << std::endl;
        return 0;
}
//g++ exemplo1.cpp -o ex01
//./ex01