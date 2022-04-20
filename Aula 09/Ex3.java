import java.util.Scanner;
public class Ex3
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        int contador = 0;
        System.out.println("Insira um nome de usuário: ");
        String usuario = sc.next();

        while(!usuario.equals("admin"))
        {
            System.out.println("Insira um usuário válido: ");
            usuario = sc.next();
        }
        
        System.out.println("Insira a senha: ");
        String senha = sc.next();

        while(!senha.equals("c3c") && contador < 2)
        {
            System.out.println("Tente inserir outra senha: ");
            senha = sc.next();
            contador++;
        }

        if(senha.equals("c3c"))
        {
            System.out.println("Usuário autorizado!");
        }
        else
        {
            System.out.println("Usuário bloqueado!");
        }
    }
}
