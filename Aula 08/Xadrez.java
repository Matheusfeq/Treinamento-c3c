import java.util.Scanner;
public class Xadrez
{
    public static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) 
    {
        System.out.println("Digite a hora de início do jogo: ");
        int inicio = sc.nextInt();
        System.out.println("Digite a hora de término do jogo: ");
        int termino = sc.nextInt();
        int total;

        if(inicio < termino)
        {
            total = termino - inicio;
        }
        else if(inicio == termino)
        {
            total = 24;
        }
        else
        {
            total = (24 + termino) - inicio;
        }
        
        System.out.println("Duração total: " + total);  
    }
    
}