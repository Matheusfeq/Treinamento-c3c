import java.util.Scanner;
public class Ex1 
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args)
    {
        int y;
        System.out.println("Insira o numerador da divisão: ");
        int x = sc.nextInt();
        do
        {   
            System.out.println("Insira um valor para o denominador da divisão(diferente de 0): ");
             y = sc.nextInt();
        }while(y == 0);

        System.out.println("O resultado da divisão é "+(x/y));
    }
}
