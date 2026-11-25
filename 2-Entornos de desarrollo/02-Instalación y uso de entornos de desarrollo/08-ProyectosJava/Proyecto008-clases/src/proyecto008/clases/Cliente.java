package proyecto008.clases;


public class Cliente {
    
    String nombre;
    String apellidos;
    int edad;
    
    public Cliente(String nuevonombre,String nuevosapellidos,int nuevaedad){
        nombre = nuevonombre;
        apellidos = nuevosapellidos;
        edad = nuevaedad;
    }
    
    public String getNombre(){
        return nombre + apellidos;
    }
    public int getEdad(){
        return edad;
    }
}
