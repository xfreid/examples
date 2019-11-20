// this is a Interface
// interface is a class with only abstract methods
// you can as many interfaces to a class using "implements" as you want

public interface Living {

    // all the methods in interface are abstract by default
    // so you don't need "abstract" keyword
    public String getName();
    public void setName(String newName);

    public double getWeight();
    public void setWeight(double newWeight);

    public String getFavFood();
    public void setFavFood(String newFavFood);

    public double getSpeed(); 
    public void setSpeed(double newSpeed);

    public String getSound(); 
    public void setSound(String newSound);

}