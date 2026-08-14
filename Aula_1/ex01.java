import java.util.Scanner;

public class ex01 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("What's your name? ");
        String name = scanner.next();

        System.out.println("Hello " + name +"!");

        scanner.close();
    }
}
// javac ex01.java
// java ex01