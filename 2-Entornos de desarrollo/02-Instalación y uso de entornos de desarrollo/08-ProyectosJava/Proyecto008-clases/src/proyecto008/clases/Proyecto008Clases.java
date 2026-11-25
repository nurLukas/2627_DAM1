package proyecto008.clases;

public class Proyecto008Clases {

    
    
    public static void main(String[] args) {
        // En la instanciación hay que indicar el tipo de dato
        // Cliente es el tipo de datos del objeto
        // Cliente1 es el nombre de la instacncia, podemos poner lo que queramos (como una variable)
        // new es la palabra reservada que usamos para instanciar
        // Cliente es la llamada a clase (lleva parámetros)
        Cliente Cliente1 = new Cliente("Nacho","Hernández",24);
        //System.out.println(Cliente1);
        
        System.out.println(Cliente1.edad);
        System.out.println(Cliente1.getEdad());
    }
    
}
