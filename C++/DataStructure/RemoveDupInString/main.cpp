// given a string S, remove all the duplicated chars in the string.
// https://www.geeksforgeeks.org/remove-duplicates-from-a-given-string/

// #include <bits/stdc++.h> 
#include <cstring>
#include <string>
#include <iostream>
using namespace std; 
  
char *removeDuplicate(char str[], int n) 
{ 
   // Used as index in the modified string 
   int index = 0;    
     
   // Traverse through all characters 
   for (int i=0; i<n; i++) { 
     // Check if str[i] is present before it   
     int j;
     for (j=0; j<i; j++)  
        if (str[i] == str[j]) 
           break; 
       
     // If not present, then add it to 
     // result. 
     if (j == i) { 
        std:: cout << "str[index] = " << str[i] << std::endl; 
        str[index++] = str[i];
     } 
   } 

   for (int i = index; i < n; i++) {
       // reset the remaining of the str
       std:: cout << "str[i] = " << '\0' << std::endl; 
       str[i] = '\0';
   }
     
   return str; 
} 
  
// Driver code 
int main() 
{ 
   // https://www.techiedelight.com/convert-string-char-array-cpp/
   // convert a string to char array
   std::string msg = "geeksforgeeks";
   char strArr[msg.size() + 1]; 
   strcpy(strArr, msg.c_str());
   // int n = sizeof(str) / sizeof(str[0]); 
   int n = msg.size();
   std::cout << "n is " << n << std::endl;
   std::cout << removeDuplicate(strArr, n) << std::endl; 
   return 0; 
} 




