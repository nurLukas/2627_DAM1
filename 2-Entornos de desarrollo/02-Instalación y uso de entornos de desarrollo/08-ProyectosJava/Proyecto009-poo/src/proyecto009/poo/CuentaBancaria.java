package proyecto009.poo;


public class CuentaBancaria {
    private int saldo;
    public CuentaBancaria(){
        saldo = 0;
    }
    public void imponerSaldo(int cantidad){
        if (cantidad < 10000){
            saldo += cantidad;
        }else{
            System.out.println("Cantidad inválida, tienes que pasar por oficina");
        }
        
        // En vez de pooner un return 0, void dice que no devuelve nada y así no es necesario un return.
    }
    public void retirarSaldo(int cantidad){
        if (saldo - cantidad > 0){
            saldo -= cantidad;
        }else{
            System.out.println("No ves que no tienes tanto dinero??");
        }
        
    }
    public int getSaldo(){
        return saldo;
    }
}
