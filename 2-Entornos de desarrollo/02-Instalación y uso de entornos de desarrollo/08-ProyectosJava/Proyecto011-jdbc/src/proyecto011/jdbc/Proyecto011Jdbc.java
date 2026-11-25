package proyecto011.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.sql.ResultSet;

public class Proyecto011Jdbc {

    public static void main(String[] args) {
        String direccion = "jdbc:mysql://localhost:3306/tiendaonlinetame";
        String usuario = "tiendaonlinetame";
        String contrasenia = "Tienda123$";
        
        //Intentamos conectarnos y si falla no te cuelgues
        try{
            Connection miconexion = DriverManager.getConnection(direccion, usuario, contrasenia);
            Statement sentencia = miconexion.createStatement(); // Te voy a pedir algo
            ResultSet miresultado = sentencia.executeQuery("SELECT * FROM productos");
            while(miresultado.next()){
                System.out.println(miresultado.getString("nombre"));
                System.out.println(miresultado.getString("descripcion"));
                System.out.println(miresultado.getDouble("precio"));
                System.out.println("-------------------------------------------------");
            }
            miconexion.close();
            miresultado.close();
            sentencia.close();
        }catch(Exception e){
            e.printStackTrace();
        }
    }
    
}
