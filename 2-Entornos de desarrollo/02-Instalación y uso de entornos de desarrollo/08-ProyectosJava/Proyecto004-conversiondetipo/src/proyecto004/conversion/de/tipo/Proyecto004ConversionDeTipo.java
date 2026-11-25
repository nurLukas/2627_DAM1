package proyecto004.conversion.de.tipo;

import static java.lang.Integer.parseInt;
import java.util.Scanner;

public class Proyecto004ConversionDeTipo {

    public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          
          System.out.print("Introduce tu edad: ");
          String edad = sc.nextLine();
          
          int edadnumero = parseInt(edad);
          int doble = edadnumero*2;
          
          System.out.println("El doble de tu edad es "+doble+" años");
          
    }
    
}
