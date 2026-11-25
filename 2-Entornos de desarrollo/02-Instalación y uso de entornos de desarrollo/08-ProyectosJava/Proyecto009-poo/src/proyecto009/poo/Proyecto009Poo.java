package proyecto009.poo;


public class Proyecto009Poo {

    public static void main(String[] args) {
        
        CuentaBancaria Cuenta1 = new CuentaBancaria();
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.getSaldo());
        Cuenta1.imponerSaldo(1000000);
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.getSaldo());
        Cuenta1.imponerSaldo(1000);
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.getSaldo());
        Cuenta1.retirarSaldo(1000000);
        System.out.println("Cual es mi saldo?");
        System.out.println(Cuenta1.getSaldo());
        
    }

}
