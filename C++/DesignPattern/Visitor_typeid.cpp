
#include <iostream>
using namespace std;
  
class Visitor;

class Stock
{
  public:
    virtual void accept(class Visitor *) = 0;
    virtual void set_num_stocks (int num_stocks) = 0;
    virtual int get_num_stocks () = 0;
};
  
class Apple : public Stock
{
  public:
    /*virtual*/ void accept(Visitor *);

    void set_num_stocks (int num_stocks) {m_num_stocks = num_stocks;}
    int get_num_stocks () {return m_num_stocks;}

  private:
    static int m_num_stocks;
};
int Apple::m_num_stocks = 0;

class Google : public Stock
{
  public:
    /*virtual*/ void accept(Visitor *);

    void set_num_stocks (int num_stocks) {m_num_stocks = num_stocks;}
    int get_num_stocks () {return m_num_stocks;}

  private:
    static int m_num_stocks;
};
int Google::m_num_stocks = 0;

  

class Visitor
{
  public:
    virtual void visit(Stock *) = 0;
};

class BuyVisitor : public Visitor
{
  public:
    BuyVisitor()
    {
    }

    /*virtual*/ void visit(Stock *s)
    {
        int num_stocks = s->get_num_stocks();
        string stock_name = typeid(*s).name();
        if (typeid(*s) == typeid(Apple)) {
            num_stocks += 1;
            // stock_name = "Apple";
        } else if (typeid(*s) == typeid(Google)) {
            num_stocks += 2;
            // stock_name = "Google";
        } else {
          return;
        } 
        s->set_num_stocks(num_stocks);
        cout << "number of " << stock_name << " stocks: " << s->get_num_stocks() << '\n';
    }
};
  
class SellVisitor : public Visitor
{
  public:
    /*virtual*/ void visit(Stock *s)
    {
       int num_stocks = s->get_num_stocks();
        string stock_name;
        if (typeid(*s) == typeid(Apple)) {
            num_stocks -= 1;
            stock_name = "Apple";
        } else if (typeid(*s) == typeid(Google)) {
            stock_name = "Google";
            num_stocks -= 2;
        } else {
          return;
        }
        s->set_num_stocks(num_stocks);
        cout << "number of " << stock_name << " stocks: " << s->get_num_stocks() << '\n';;
    }
};

// in the same file, these two methods have 
// to be defined after the Visitor defintion  
void Apple::accept(Visitor *v)
{
    v->visit(this);
}
  
void Google::accept(Visitor *v)
{
    v->visit(this);
}

 
int main(int argc, char const *argv[])
{
    Stock *set[] = { new Apple, new Google, new Google,
                     new Apple, new Apple, 0 };
  
    BuyVisitor buy_operation;
    SellVisitor sell_operation;
    for (int i = 0; set[i]; i++)
    {
        set[i]->accept(&buy_operation);
    }
  
    for (int i = 0; set[i]; i++)
    {
        set[i]->accept(&sell_operation);
    }
}