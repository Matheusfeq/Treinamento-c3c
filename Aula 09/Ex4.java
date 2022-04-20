import java.util.Scanner;
public class Ex4
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.println("Insira um nome de usuário: ");
        String usuario = sc.next();
        while(!usuario.equals("admin"))
        {
            System.out.println("Insira um usuário válido: ");
            usuario = sc.next();
        }
        
        System.out.println("Insira a senha: ");
        String senha = sc.next();

        if(!senha.equals("c3c"))
        {
            for(int i = 0; i < 2; i++)
            {
                System.out.println("Tente inserir outra senha: ");
                senha = sc.next();
                if(senha.equals("c3c"))
                {
                    break;
                }
            }
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
