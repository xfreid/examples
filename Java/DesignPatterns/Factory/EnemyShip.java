public abstract class EnemyShip {
    private String name;
    private double amtDamage;

    public String getName() {return name;}
    public void setName(String newName) {name = newName;}

    public double getDamage() {return amtDamage;}
    public void setDamage(double newDamage) {amtDamage = newDamage;}

    public void display() {
        System.out.println(getName() + "is on screen");
    }

    public void shoot() {
        System.out.println(getName() + "attacks and causes " + getDamage() + " damage");
    }

}