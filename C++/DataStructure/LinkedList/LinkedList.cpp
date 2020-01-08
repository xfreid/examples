#include <iostream>
#include <cstdlib>

using namespace std;

// this is a single linked list
class Node
{
public:
    Node* next;
    int data;
};

class LinkedList
{
public:
    int length;
    Node* head;

    LinkedList();
    ~LinkedList();
    void push(int data);
    void append(int data);
    void print();
};

LinkedList::LinkedList(){
    this->length = 0;
    this->head = nullptr;
}

LinkedList::~LinkedList(){
    std::cout << "LIST DELETED";
}

// Given a reference (pointer to pointer)  
// to the head of a list and an int,  
// inserts a new node on the front of the list. */
void LinkedList::push(int data)  
{  
    Node* new_node = new Node();  
    new_node->data = data;  
    // point next of new node to the existing head node 
    // this also holds if the current list is empty
    // i.e. this->head == nullptr
    new_node->next = this->head;  
    // move the head to point to the new node 
    this->head = new_node;  
    this->length++;
}  

// append an item to the end of list
void LinkedList::append(int data){
    Node* new_node = new Node();
    new_node->data = data;
    // This new node is going to be the last node, so make next  
    // of it as NULL
    new_node->next = nullptr; 
  
    if (this->head == nullptr) {
        this->head = new_node;
        this->length++;
        return;
    }

    Node *last = this->head;
    // traverse till the last node
    while (last->next != NULL) 
        last = last->next; 
   
    // update the next of last node
    last->next = new_node; 
    // std::cout << "new_node is " << new_node << std::endl;
    // std::cout << "new_node data is " << new_node->data << std::endl;
    // std::cout << "new_node next is " << new_node->next << std::endl;
    this->length++;
}

// print the whole list
void LinkedList::print(){
    Node* node = this->head;
    int i = 1;
    while(node){
        std::cout << i << ": " << node->data << std::endl;
        node = node->next;
        i++;
    }
}

int main(int argc, char const *argv[])
{
    LinkedList* list = new LinkedList();
    /*
    // generate a list of 100 integer numbers in the range of 0 - 99
    // append them to the linked list
    for (int i = 0; i < 100; ++i)
    {
        // rand() returns a pseudo-random number in the range of 0 to RAND_MAX.
        list->add(rand() % 100);
    }
    */
    list->push(1);
    list->append(3);
    list->append(5);

    list->print();
    std::cout << "List Length: " << list->length << std::endl;
    delete list;
    return 0;
}