import java.util.Scanner;  // keyboard input

public class EnemyShipFactTest {

    public static void main(String[] args) {
        // new way of construting the EnemyShip objects using Factory
        EnemyShipFactory shipFactory = new EnemyShipFactory();
        EnemyShip enemyShip = null;
        Scanner userInput = new Scanner(System.in);
        String enemyShipType = "";
        System.out.println("What type of ship (U / R / B)?");
        if (userInput.hasNextLine()) {
            enemyShipType = userInput.nextLine();
            enemyShip = shipFactory.makeEnemyShip(enemyShipType);
        }

        if (enemyShip != null) {
            doStuffEnemy(enemyShip);
        }
    }

    public static void doStuffEnemy(EnemyShip anEnemyShip) {
        anEnemyShip.display();
        anEnemyShip.shoot();
    }

}