import java.util.Scanner;
public class Main
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) 
    {
        System.out.println("Digite a quantidade de maçãs compradas: ");
        int macas = sc.nextInt();
        double total;

        if(macas < 12)
        {
            total = 2.50*macas;
        }
        else
        {
            total = 1.90*macas;
        }
        
        System.out.println("Valor total: " + total);  
    }
    
}