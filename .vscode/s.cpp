#include <iostream>

using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int temp;

    cout << "Before swapping: a = " << a << ", b = " << b << endl;

    temp = a;
    a = b;
    b = temp;

    cout << "After swapping: a = " << a << ", b = " << b << endl;

    return 0;
}
