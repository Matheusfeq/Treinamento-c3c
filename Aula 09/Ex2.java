import java.util.Scanner;
public class Ex2
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        System.out.println("Insira o numerador da divisão: ");
        int x = sc.nextInt();
        
        System.out.println("Insira um valor para o denominador da divisão(diferente de 0): ");
        int y = sc.nextInt();
        
        while(y == 0)
        {
            System.out.println("Tente inserir um valor diferente de 0 para o denominador: ");
            y = sc.nextInt();
        }

        System.out.println("O resultado da divisão é "+(x/y));
    }
}
