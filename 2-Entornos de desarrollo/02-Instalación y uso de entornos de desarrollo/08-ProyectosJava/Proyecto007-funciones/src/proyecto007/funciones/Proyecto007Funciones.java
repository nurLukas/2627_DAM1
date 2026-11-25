package proyecto007.funciones;

public class Proyecto007Funciones {
    static int suma(int num1,int num2){
        int suma = num1 + num2;
        return suma;
    }
    

    public static void main(String[] args) {
        int num1 = 9;
        int num2 = 5;
        int suma = num1 + num2;
        System.out.println(suma);
        
        System.out.println(suma(9,5));
        System.out.println(suma(9,8));
    }
    
}
