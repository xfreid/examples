// this is a abstract class
// you can't create object of abstract class
abstract public class Creature {
    // protected fields can be accessed by sub-classes
    protected String name;
    protected int weight;
    protected String sound;

    // abstract method
    public abstract void setName(String newName);
    public abstract String getName();

    public abstract int getWeight();
    public abstract void setWeight(int newWeight);
}