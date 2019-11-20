public class AnimalFly {
    public static void main(String[] args) {
        Animal sparky = new Dog();
        Animal tweety = new Bird();

        System.out.println("Dog: " + sparky.doFly());
        System.out.println("Bird: " + tweety.doFly());
    }
}