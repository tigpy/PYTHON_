#include <iostream>
using namespace std;

// Recursive function to calculate the factorial of a number
int factorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * factorial(n-1);
    }
}

// Main function to get user input and output the result
int main() {
    int n;
    cout << "Enter a non-negative integer: ";
    cin >> n;
    cout << n << "! = " << factorial(n) << endl;
    return 0;
}
