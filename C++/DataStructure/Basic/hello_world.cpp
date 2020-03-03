
// Simple C++ program to display "Hello World" 
  
// Header file for input output functions 
#include<iostream>  
#include<fstream>
#include<vector>
  
// main function - 
// where the execution of program begins 
int main() 
{ 
    // prints hello world 
    std::cout <<"Hello World" << std::endl; 

    std::vector<int> v= {1, 2, 3, 4, 5, 6};
    auto it = v.begin();
    std::cout << "it :" << *it << std::endl;
    it --;
    std::cout << "it :" << *it << std::endl;
    it ++;
    std::cout << "it :" << *it << std::endl;
    
    auto it2 = v.end();
    it2 --;
    std::cout << "it2 :" << *it2 << std::endl;
    it2 ++;
    std::cout << "it2 :" << *it2 << std::endl;
    it2 --;
    std::cout << "it2 :" << *it2 << std::endl;

#if 0
    for (auto it = v.begin(); it != v.end(); it++) {
        if (*it < 4) {
            it = v.erase(it);
            it --;
        }
    } 

    for (const int &i: v) {
        std::cout << i << " ";
    }
#endif

    // write integer to a binary file
    std::ofstream f("data.bin", std::ofstream::out  | std::ofstream::binary);
    // 0x0000FFAA (32bit integer)
    int iNumber = 65450;
    // f.write((char*)&nI, sizeof(int));
    f << iNumber;
    f.close();

    return 0; 
} 